from __future__ import annotations
from typing import Optional
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class CyberEvent(db.Model):
    """Model for cybersecurity events data."""
    __tablename__ = 'data'
    
    EventID: Mapped[str] = mapped_column(db.String(50), primary_key=True)
    SourceIP: Mapped[str] = mapped_column(db.String(15))
    DestinationIP: Mapped[str] = mapped_column(db.String(15))
    AttackType: Mapped[str] = mapped_column(db.String(50))
    AttackSeverity: Mapped[str] = mapped_column(db.String(20))
    
    # One-to-one relationship with EventResponse
    response: Mapped[Optional[EventResponse]] = relationship('EventResponse', backref='event', uselist=False)

    def __repr__(self) -> str:
        """String representation of the event."""
        return f'<CyberEvent {self.EventID}>'

class EventResponse(db.Model):
    """Model for event response data."""
    __tablename__ = 'response'
    
    EventID: Mapped[str] = mapped_column(db.String(50), db.ForeignKey('data.EventID'), primary_key=True)
    AttackType: Mapped[str] = mapped_column(db.String(50))
    DataExfiltrated: Mapped[Optional[str]] = mapped_column(db.String(100))
    ThreatIntelligence: Mapped[Optional[str]] = mapped_column(db.String(200))
    ResponseAction: Mapped[Optional[str]] = mapped_column(db.String(200))

    def __repr__(self) -> str:
        """String representation of the response."""
        return f'<EventResponse {self.EventID}>'