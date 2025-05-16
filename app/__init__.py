"""
Main app setup for my cybersecurity tracker
Student ID: [Your ID]
May 17, 2025
"""

from flask import Flask, render_template
from config import config
from app.models import db
from flask_bootstrap import Bootstrap
from app.utils.logger import logger

# Set up Bootstrap for nice looking pages
bootstrap = Bootstrap()

def create_app(config_name='default'):
    """Creates and sets up our Flask app.
    
    Made this a function so we can create different versions of the app
    (like one for testing and one for real use).
    """
    # Create the basic Flask app
    app = Flask(__name__)
    
    # Load the right settings (development/testing/production)
    app.config.from_object(config[config_name])
    
    # Set up our extra features
    db.init_app(app)        # Database connection
    bootstrap.init_app(app) # Nice looking templates
    
    # Add our page routes
    from app.routes.main import main_bp
    app.register_blueprint(main_bp)
    
    # Add handlers for when things go wrong
    @app.errorhandler(404)
    def not_found_error(error):
        """Show nice message when page isn't found"""
        logger.warning(f"Page not found: {error}")
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        """Handle server errors - cancels any database changes"""
        logger.error(f"Server error: {error}", exc_info=True)
        db.session.rollback()
        return render_template('errors/500.html'), 500

    @app.errorhandler(400)
    def bad_request_error(error):
        """Handle bad request errors"""
        logger.warning(f"Bad request: {error}")
        return render_template('errors/400.html'), 400

    return app