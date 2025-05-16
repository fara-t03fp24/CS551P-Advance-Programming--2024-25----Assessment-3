from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CyberEvent(db.Model):
    """Stores info about each security event.
    
    I split this into two tables (events and responses) because it's cleaner
    and lets us add response info later if we need to.
    """
    __tablename__ = 'data'
    
    # Using strings for all IDs and IPs to keep it simple
    EventID = db.Column(db.String(50), primary_key=True)  # Primary key for linking tables
    SourceIP = db.Column(db.String(15))     # Where the attack came from
    DestinationIP = db.Column(db.String(15)) # Target of the attack
    AttackType = db.Column(db.String(50))    # What kind of attack it was
    AttackSeverity = db.Column(db.String(20)) # How bad the attack was (High/Medium/Low)
    
    # Links to the response info - one event has one response
    response = db.relationship('EventResponse', backref='event', uselist=False)

    def __repr__(self):
        # Just for debugging - shows event ID when we print it
        return f'<CyberEvent {self.EventID}>'

class EventResponse(db.Model):
    """Stores how we responded to each security event.
    
    This table has all the response info - separate from the event details
    to keep things organized. EventID links it back to the main event.
    """
    __tablename__ = 'response'
    
    EventID = db.Column(db.String(50), db.ForeignKey('data.EventID'), primary_key=True)
    AttackType = db.Column(db.String(50))
    DataExfiltrated = db.Column(db.String(100))   # What data was taken
    ThreatIntelligence = db.Column(db.String(200)) # What we know about the threat
    ResponseAction = db.Column(db.String(200))      # What we did about it

    def __repr__(self):
        return f'<EventResponse {self.EventID}>'