"""Database models for the cybersecurity events tracker.

This module defines the SQLAlchemy models for storing cybersecurity events
and their corresponding response actions.

Author: [Your Name]
Student ID: [Your ID]
Date: May 17, 2025
"""
from __future__ import annotations
from typing import Optional
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class CyberEvent(db.Model):
    """Model for cybersecurity events data.
    
    Attributes:
        EventID: Unique identifier for the event
        SourceIP: IP address where the attack originated
        DestinationIP: Target IP address of the attack
        AttackType: Type of cyber attack
        AttackSeverity: Severity level (High/Medium/Low)
        response: Related response action details
    """
    __tablename__ = 'data'
    
    EventID: str = db.Column(db.String(50), primary_key=True)
    SourceIP: str = db.Column(db.String(15))
    DestinationIP: str = db.Column(db.String(15))
    AttackType: str = db.Column(db.String(50))
    AttackSeverity: str = db.Column(db.String(20))
    CreatedAt: datetime = db.Column(db.DateTime, default=datetime.utcnow)
    UpdatedAt: datetime = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # One-to-one relationship with EventResponse
    response: Optional[EventResponse] = db.relationship('EventResponse', backref='event', uselist=False)

    def __repr__(self) -> str:
        """String representation of the event."""
        return f'<CyberEvent {self.EventID}>'

class EventResponse(db.Model):
    """Model for event response data.
    
    Attributes:
        EventID: Foreign key linking to CyberEvent
        AttackType: Type of attack identified
        DataExfiltrated: Description of any data stolen
        ThreatIntelligence: Intelligence gathered about the threat
        ResponseAction: Actions taken to address the threat
    """
    __tablename__ = 'response'
    
    EventID: str = db.Column(db.String(50), db.ForeignKey('data.EventID'), primary_key=True)
    AttackType: str = db.Column(db.String(50))
    DataExfiltrated: Optional[str] = db.Column(db.String(100))
    ThreatIntelligence: Optional[str] = db.Column(db.String(200))
    ResponseAction: Optional[str] = db.Column(db.String(200))
    CreatedAt: datetime = db.Column(db.DateTime, default=datetime.utcnow)
    UpdatedAt: datetime = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self) -> str:
        """String representation of the response."""
        return f'<EventResponse {self.EventID}>'