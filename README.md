# Cybersecurity Events Tracker Application

## Student Information
- **Module:** CS551P Advanced Programming (2024-25)
- **Assessment:** 3
- **Student ID:** 52427848

## Project Overview
I developed a web-based application using Flask framework to track and analyze cybersecurity events. This project demonstrates my understanding of advanced programming concepts, database management, and web development principles learned during the CS551P module.

## Key Features
1. **Interactive Dashboard**
   - Real-time display of cybersecurity events
   - Quick statistics showing total events and severity distributions
   - Responsive design for both desktop and mobile viewing

2. **Event Management**
   - Detailed view of individual security incidents
   - Tracking of source/destination IPs
   - Attack type and severity classification

3. **Analysis Tools**
   - Statistical breakdown of attack types
   - Severity level distribution graphs
   - Visual representation using progress bars

4. **Data Organization**
   - Event response tracking
   - Threat intelligence information
   - Automated data exfiltration logging

## Technical Implementation

### Technology Stack
- **Backend:** Python 3.8+ with Flask 3.0.0
- **Database:** SQLite3 with SQLAlchemy ORM
- **Frontend:** Bootstrap CSS framework
- **Testing:** pytest framework
- **Version Control:** Git

### Database Design
I implemented two main tables:

1. **data table**
   ```
   - EventID (Primary Key)
   - SourceIP
   - DestinationIP
   - AttackType
   - AttackSeverity
   ```

2. **response table**
   ```
   - EventID (Foreign Key)
   - AttackType
   - DataExfiltrated
   - ThreatIntelligence
   - ResponseAction
   ```

## Project Structure
```
.
├── app/                  # Main application directory
│   ├── models/          # Database models
│   ├── routes/          # URL routing handlers
│   ├── templates/       # HTML templates
│   ├── static/          # CSS and static files
│   └── utils/           # Utility functions
├── tests/               # Test cases
├── migrations/          # Database migrations
└── config.py           # Configuration settings
```

## Setup Instructions

1. Clone the repository and create virtual environment:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python run.py
   ```

4. Access the application at: http://localhost:3000

## Testing
I implemented comprehensive tests to ensure application reliability:

```bash
# Run all tests
pytest

# Generate coverage report
coverage run -m pytest
coverage report
```
