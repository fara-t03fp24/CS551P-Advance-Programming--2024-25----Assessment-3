from app import create_app
import os

app = create_app('development')

if __name__ == '__main__':
    # Get port from environment variable or default to 4555
    port = int(os.environ.get('PORT', 4555))
    # Run the app on port 4555 which is standard for Codio
    app.run(host='0.0.0.0', port=port, debug=True)