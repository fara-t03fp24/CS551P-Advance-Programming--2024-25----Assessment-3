from flask import Blueprint, render_template, request, abort
from app.models import CyberEvent, EventResponse, db
from sqlalchemy import desc, func

# Blueprint helps organize the routes better
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Homepage - shows dashboard with stats and recent events.
    
    I added pagination because we have lots of events and loading
    them all at once would be too slow!
    """
    # Get which page we want to show (starts at page 1)
    page = request.args.get('page', 1, type=int)
    per_page = 50  # Show 50 events per page - not too many, not too few
    
    # Get a page of events, newest first
    events = CyberEvent.query.order_by(
        desc(CyberEvent.EventID)  # Newest events on top
    ).paginate(page=page, per_page=per_page, error_out=False)
    
    # Count different types of events for the dashboard cards
    stats = {
        'total_events': CyberEvent.query.count(),
        'high_severity': CyberEvent.query.filter_by(AttackSeverity='High').count(),
        'medium_severity': CyberEvent.query.filter_by(AttackSeverity='Medium').count(),
        'low_severity': CyberEvent.query.filter_by(AttackSeverity='Low').count()
    }
    
    return render_template('index.html', events=events, stats=stats)

@main_bp.route('/event/<event_id>')
def event_detail(event_id):
    """Shows all details about one specific event.
    
    Uses get_or_404 to show a nice error page if event isn't found.
    """
    event = CyberEvent.query.get_or_404(event_id)
    return render_template('event_detail.html', event=event)

@main_bp.route('/analysis')
def analysis():
    """Shows charts and stats about all our security events.
    
    Uses SQLAlchemy's func.count to count things directly in the database
    instead of loading everything into Python first - way faster!
    """
    # Count how many of each attack type we have
    attack_types = db.session.query(
        CyberEvent.AttackType,
        func.count(CyberEvent.EventID).label('count')
    ).group_by(CyberEvent.AttackType).all()
    
    # Count how many High/Medium/Low severity events
    severity_dist = db.session.query(
        CyberEvent.AttackSeverity,
        func.count(CyberEvent.EventID).label('count')
    ).group_by(CyberEvent.AttackSeverity).all()
    
    return render_template('analysis.html', 
                         attack_types=attack_types,
                         severity_dist=severity_dist)