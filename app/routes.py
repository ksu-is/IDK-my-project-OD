"""Application routes for Soccer Practice Planner"""
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import Team, Player, Drill

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    """Welcome screen / landing page"""
    return render_template('welcome-v3.html')

@bp.route('/team/new', methods=['GET', 'POST'])
def new_team():
    """Create a new team"""
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        age_group = request.form.get('age_group')
        skill_level = request.form.get('skill_level')
        num_players = request.form.get('num_players')
        focus_areas = ','.join(request.form.getlist('focus_areas'))
        additional_notes = request.form.get('additional_notes')

        # Create new team
        team = Team(
            name=name,
            age_group=age_group,
            skill_level=skill_level,
            num_players=int(num_players),
            focus_areas=focus_areas,
            additional_notes=additional_notes
        )

        db.session.add(team)
        db.session.commit()

        flash(f'Team "{name}" created successfully!', 'success')
        return redirect(url_for('main.team_dashboard', team_id=team.id))

    return render_template('team_form.html')

@bp.route('/team/<int:team_id>/dashboard')
def team_dashboard(team_id):
    """Team dashboard showing team info and options"""
    team = Team.query.get_or_404(team_id)
    return render_template('team_dashboard.html', team=team)

@bp.route('/teams')
def teams_list():
    """List all teams"""
    teams = Team.query.order_by(Team.created_at.desc()).all()
    return render_template('teams_list.html', teams=teams)

@bp.route('/drills')
def drills_catalog():
    """Drill catalog - browse all drills"""
    category = request.args.get('category', 'All')
    skill_level = request.args.get('skill_level', 'All')

    query = Drill.query

    if category != 'All':
        query = query.filter_by(category=category)

    if skill_level != 'All':
        query = query.filter_by(skill_level=skill_level)

    drills = query.order_by(Drill.name).all()

    return render_template('drills_catalog.html', drills=drills,
                         selected_category=category,
                         selected_skill=skill_level)

@bp.route('/drill/<int:drill_id>')
def drill_detail(drill_id):
    """View detailed information about a specific drill"""
    drill = Drill.query.get_or_404(drill_id)
    return render_template('drill_detail.html', drill=drill)
