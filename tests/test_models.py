import pytest
from app.models import CyberEvent, EventResponse

def test_new_cyber_event(app):
    """Test creating a new cyber event."""
    with app.app_context():
        event = CyberEvent(
            EventID='TEST002',
            SourceIP='192.168.1.2',
            DestinationIP='10.0.0.2',
            AttackType='XSS Attack',
            AttackSeverity='Medium'
        )
        assert event.EventID == 'TEST002'
        assert event.SourceIP == '192.168.1.2'
        assert event.AttackType == 'XSS Attack'
        assert event.AttackSeverity == 'Medium'

def test_new_event_response(app):
    """Test creating a new event response."""
    with app.app_context():
        response = EventResponse(
            EventID='TEST002',
            DataExfiltrated='Customer Data',
            ThreatIntelligence='Medium Risk',
            ResponseAction='IP Blocked'
        )
        assert response.EventID == 'TEST002'
        assert response.DataExfiltrated == 'Customer Data'
        assert response.ResponseAction == 'IP Blocked'

def test_cyber_event_response_relationship(app):
    """Test the relationship between CyberEvent and EventResponse."""
    with app.app_context():
        # Test data is already added in conftest.py
        event = CyberEvent.query.filter_by(EventID='TEST001').first()
        assert event is not None
        assert event.response is not None
        assert event.response.EventID == event.EventID
        assert event.response.ResponseAction == 'Blocked'