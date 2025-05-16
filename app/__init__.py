from typing import Union, Dict, Any, Optional
from flask import Flask, render_template, Response
from config import config
from app.models import db
from flask_bootstrap import Bootstrap
from app.utils.logger import logger
from flask_migrate import Migrate

# Set up Bootstrap for nice looking pages
bootstrap = Bootstrap()

def create_app(config_name: str = 'default') -> Flask:
    """Create and configure a Flask application instance.
    
    Args:
        config_name: The name of the configuration to use (default, testing, production)
        
    Returns:
        A configured Flask application instance
        
    Note:
        This function implements the application factory pattern and sets up:
        - Database connection
        - Bootstrap for templates
        - Logging configuration
        - Error handlers
        - Blueprint registration
    """
    # Create the basic Flask app
    app = Flask(__name__)
    
    # Load the right settings (development/testing/production)
    app.config.from_object(config[config_name])
    
    # Set up our extra features
    db.init_app(app)        # Database connection
    bootstrap.init_app(app) # Nice looking templates
    migrate = Migrate(app, db) # Flask-Migrate initialization
    
    # Add our page routes
    from app.routes.main import main_bp
    app.register_blueprint(main_bp)
    
    # Add handlers for when things go wrong
    @app.errorhandler(404)
    def not_found_error(error: Any) -> Union[Response, tuple[str, int]]:
        """Handle 404 Not Found errors.
        
        Args:
            error: The error that occurred
            
        Returns:
            A tuple containing the error page and status code
        """
        logger.warning(f"Page not found: {error}")
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_error(error: Any) -> Union[Response, tuple[str, int]]:
        """Handle 500 Internal Server errors.
        
        Args:
            error: The error that occurred
            
        Returns:
            A tuple containing the error page and status code
            
        Note:
            This handler also rolls back any pending database transactions
            to maintain data consistency.
        """
        logger.error(f"Server error: {error}", exc_info=True)
        db.session.rollback()
        return render_template('errors/500.html'), 500

    @app.errorhandler(400)
    def bad_request_error(error: Any) -> Union[Response, tuple[str, int]]:
        """Handle 400 Bad Request errors.
        
        Args:
            error: The error that occurred
            
        Returns:
            A tuple containing the error page and status code
        """
        logger.warning(f"Bad request: {error}")
        return render_template('errors/400.html'), 400

    return app