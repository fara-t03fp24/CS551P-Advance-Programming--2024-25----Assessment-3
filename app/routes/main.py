"""Route handlers for the cybersecurity events tracker.

This module contains all the route handlers for the main application pages,
including the dashboard, event details, and analysis views.

Author: [Your Name]
Student ID: [Your ID]
Date: May 17, 2025
"""
from typing import Dict, Any, List, Tuple, Union
from flask import Blueprint, render_template, request, abort
from app.models import CyberEvent, EventResponse, db
from sqlalchemy import desc, func
from werkzeug.wrappers import Response

# Blueprint helps organize the routes better
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index() -> str:
    """Display the main dashboard with event listing and statistics.
    
    Returns:
        str: Rendered HTML template for the dashboard page
        
    Note:
        This view implements pagination with 50 items per page and
        shows summary statistics for events by severity level.
    """
    page: int = request.args.get('page', 1, type=int)
    per_page: int = 50
    
    # Get events with pagination
    events = CyberEvent.query.order_by(
        desc(CyberEvent.EventID)
    ).paginate(page=page, per_page=per_page, error_out=False)
    
    # Get statistics for the dashboard
    stats: Dict[str, int] = {
        'total_events': CyberEvent.query.count(),
        'high_severity': CyberEvent.query.filter_by(AttackSeverity='High').count(),
        'medium_severity': CyberEvent.query.filter_by(AttackSeverity='Medium').count(),
        'low_severity': CyberEvent.query.filter_by(AttackSeverity='Low').count()
    }
    
    return render_template('index.html', events=events, stats=stats)

@main_bp.route('/event/<event_id>')
def event_detail(event_id: str) -> Union[str, Tuple[Dict[str, str], int]]:
    """Display detailed information about a specific event.
    
    Args:
        event_id: The unique identifier of the event to display
        
    Returns:
        str: Rendered HTML template for the event detail page
        tuple: Error response if event not found
        
    Raises:
        404: If the event_id doesn't exist in the database
    """
    event = CyberEvent.query.get_or_404(event_id)
    return render_template('event_detail.html', event=event)

@main_bp.route('/analysis')
def analysis() -> str:
    """Display analysis page showing attack statistics.
    
    Returns:
        str: Rendered HTML template for the analysis page
        
    Note:
        This view shows distributions of attack types and severity levels
        using database aggregation for efficient processing.
    """
    # Get attack type distribution using func for aggregation
    attack_types: List[Any] = db.session.query(
        CyberEvent.AttackType,
        func.count(CyberEvent.EventID).label('count')
    ).group_by(CyberEvent.AttackType).all()
    
    # Get severity distribution
    severity_dist: List[Any] = db.session.query(
        CyberEvent.AttackSeverity,
        func.count(CyberEvent.EventID).label('count')
    ).group_by(CyberEvent.AttackSeverity).all()
    
    return render_template('analysis.html', 
                         attack_types=attack_types,
                         severity_dist=severity_dist)