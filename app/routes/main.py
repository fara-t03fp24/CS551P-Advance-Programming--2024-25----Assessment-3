from flask import Blueprint, render_template, request, abort
from app.models import CyberEvent, EventResponse, db
from sqlalchemy import desc, func

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Home page - displays a paginated list of cyber events"""
    page = request.args.get('page', 1, type=int)
    per_page = 50  # Number of items per page
    
    # Get events with pagination
    events = CyberEvent.query.order_by(
        desc(CyberEvent.EventID)
    ).paginate(page=page, per_page=per_page, error_out=False)
    
    # Get statistics for the dashboard
    stats = {
        'total_events': CyberEvent.query.count(),
        'high_severity': CyberEvent.query.filter_by(AttackSeverity='High').count(),
        'medium_severity': CyberEvent.query.filter_by(AttackSeverity='Medium').count(),
        'low_severity': CyberEvent.query.filter_by(AttackSeverity='Low').count()
    }
    
    return render_template('index.html', events=events, stats=stats)

@main_bp.route('/event/<event_id>')
def event_detail(event_id):
    """Detail page for a specific cyber event"""
    event = CyberEvent.query.get_or_404(event_id)
    return render_template('event_detail.html', event=event)

@main_bp.route('/analysis')
def analysis():
    """Analysis page showing attack statistics"""
    # Get attack type distribution using func for aggregation
    attack_types = db.session.query(
        CyberEvent.AttackType,
        func.count(CyberEvent.EventID).label('count')
    ).group_by(CyberEvent.AttackType).all()
    
    # Get severity distribution
    severity_dist = db.session.query(
        CyberEvent.AttackSeverity,
        func.count(CyberEvent.EventID).label('count')
    ).group_by(CyberEvent.AttackSeverity).all()
    
    return render_template('analysis.html', 
                         attack_types=attack_types,
                         severity_dist=severity_dist)