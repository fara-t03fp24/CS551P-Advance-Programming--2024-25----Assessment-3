import os
from app import create_app

# Create our Flask app - uses development settings by default
# Can change to 'production' by setting FLASK_ENV environment variable
app = create_app(os.getenv('FLASK_ENV', 'default'))

if __name__ == '__main__':
    # Only run this when we run this file directly
    # For production we use gunicorn instead
    # Using 0.0.0.0 so I can test it from other computers on my network
    app.run(host='0.0.0.0', port=5000)