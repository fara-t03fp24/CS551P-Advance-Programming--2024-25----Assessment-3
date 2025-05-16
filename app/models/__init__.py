from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CyberEvent(db.Model):
    """Model for cybersecurity events data"""
    __tablename__ = 'data'
    
    EventID = db.Column(db.String(50), primary_key=True)
    SourceIP = db.Column(db.String(15))
    DestinationIP = db.Column(db.String(15))
    AttackType = db.Column(db.String(50))
    AttackSeverity = db.Column(db.String(20))
    
    # Relationship with EventResponse
    response = db.relationship('EventResponse', backref='event', lazy=True)

    def __repr__(self):
        return f'<CyberEvent {self.EventID}>'

class EventResponse(db.Model):
    """Model for event response data"""
    __tablename__ = 'response'
    
    EventID = db.Column(db.String(50), db.ForeignKey('data.EventID'), primary_key=True)
    AttackType = db.Column(db.String(50))
    DataExfiltrated = db.Column(db.String(100))
    ThreatIntelligence = db.Column(db.String(200))
    ResponseAction = db.Column(db.String(200))

    def __repr__(self):
        return f'<EventResponse {self.EventID}>'