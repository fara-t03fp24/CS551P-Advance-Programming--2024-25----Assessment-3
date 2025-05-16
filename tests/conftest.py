import pytest
from app import create_app
from app.models import db, CyberEvent, EventResponse

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app('testing')
    
    # Create tables
    with app.app_context():
        db.create_all()
        
        # Add some test data
        test_event = CyberEvent(
            EventID='TEST001',
            SourceIP='192.168.1.1',
            DestinationIP='10.0.0.1',
            AttackType='SQL Injection',
            AttackSeverity='High'
        )
        
        test_response = EventResponse(
            EventID='TEST001',
            DataExfiltrated='None',
            ThreatIntelligence='Test Intelligence',
            ResponseAction='Blocked'
        )
        
        db.session.add(test_event)
        db.session.add(test_response)
        db.session.commit()
    
    yield app
    
    # Clean up / reset resources
    with app.app_context():
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()