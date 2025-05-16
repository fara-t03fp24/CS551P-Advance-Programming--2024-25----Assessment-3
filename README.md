# Cybersecurity Events Tracker

A Flask-based web application for tracking and analyzing cybersecurity events. This application allows users to view, analyze, and monitor cybersecurity incidents and their corresponding responses.

## Features

- Dashboard showing recent cybersecurity events
- Detailed view of individual security incidents
- Statistical analysis of attack types and severity levels
- Linked data between events and response actions
- Error handling and user-friendly interface
- No JavaScript dependencies - pure Flask and Python

## Technical Stack

- Python 3.8+
- Flask 3.0.0
- SQLite3 Database
- Flask-SQLAlchemy for ORM
- pytest for testing

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python run.py
```

The application will be available at `http://localhost:5000`

## Project Structure

```
.
├── app/
│   ├── __init__.py
│   ├── models/
│   ├── routes/
│   ├── templates/
│   ├── static/
│   └── utils/
├── tests/
├── migrations/
├── config.py
├── run.py
└── requirements.txt
```

## Database Schema

The application uses two linked tables:

1. `data` table:
   - EventID (Primary Key)
   - SourceIP
   - DestinationIP
   - AttackType
   - AttackSeverity

2. `response` table:
   - EventID (Foreign Key)
   - AttackType
   - DataExfiltrated
   - ThreatIntelligence
   - ResponseAction

## Testing

Run the test suite using:
```bash
pytest
```

For test coverage report:
```bash
coverage run -m pytest
coverage report
```

## Deployment

The application is deployed on Render and can be accessed at: [Your-Render-URL]

### Deployment Steps on Render:
1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Set the following:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn run:app`

## Development Process

This project was developed following these key principles:
- Test-Driven Development (TDD)
- Clean Code practices
- RESTful design
- Proper error handling
- Git version control

## Maintenance

To maintain the application:
1. Regularly update dependencies
2. Monitor error logs
3. Back up the database
4. Run tests before deploying updates

## License

This project is created for educational purposes as part of the CS551P Advanced Programming course at the University.

## Author

[Your Name]
Student ID: [Your Student ID]