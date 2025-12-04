"""Application routes for Soccer Practice Planner"""
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app import db
from app.models import Team, Player, Drill, PracticePlan, PlanDrill, SessionTemplate, TemplateDrill
from datetime import datetime

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

@bp.route('/team/<int:team_id>/plan/start')
def start_practice_plan(team_id):
    """Session selection screen - choose custom or template"""
    team = Team.query.get_or_404(team_id)
    return render_template('practice_plan_start.html', team=team)

@bp.route('/team/<int:team_id>/plan/templates')
def view_session_templates(team_id):
    """View available session templates"""
    team = Team.query.get_or_404(team_id)

    # Get templates matching team's attributes
    query = SessionTemplate.query

    if team.skill_level:
        query = query.filter(
            (SessionTemplate.skill_level == team.skill_level) |
            (SessionTemplate.skill_level == None)
        )

    if team.age_group:
        query = query.filter(
            (SessionTemplate.recommended_age_groups.contains(team.age_group)) |
            (SessionTemplate.recommended_age_groups == None)
        )

    templates = query.all()

    return render_template('session_templates.html', team=team, templates=templates)

@bp.route('/team/<int:team_id>/plan/from-template/<int:template_id>')
def create_from_template(team_id, template_id):
    """Create a practice plan from a template (pre-populated for editing)"""
    team = Team.query.get_or_404(team_id)
    template = SessionTemplate.query.get_or_404(template_id)

    # Get all drills for the custom builder
    all_drills = Drill.query.order_by(Drill.category, Drill.name).all()

    # Pre-populate with template drills
    selected_drills = []
    for td in sorted(template.template_drills, key=lambda x: x.order):
        selected_drills.append({
            'id': td.drill.id,
            'name': td.drill.name,
            'duration': td.duration_minutes,
            'category': td.drill.category
        })

    return render_template('practice_plan_form.html',
                         team=team,
                         all_drills=all_drills,
                         template=template,
                         selected_drills=selected_drills)

@bp.route('/team/<int:team_id>/plan/custom')
def custom_practice_plan(team_id):
    """Custom practice plan builder"""
    team = Team.query.get_or_404(team_id)

    # Get all drills for selection
    all_drills = Drill.query.order_by(Drill.category, Drill.name).all()

    return render_template('practice_plan_form.html', team=team, all_drills=all_drills)

@bp.route('/team/<int:team_id>/plan/new', methods=['GET', 'POST'])
def new_practice_plan(team_id):
    """Create a new practice plan for a team"""
    team = Team.query.get_or_404(team_id)

    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        duration = int(request.form.get('duration_minutes'))
        notes = request.form.get('notes')

        # Create practice plan
        plan = PracticePlan(
            name=name,
            team_id=team.id,
            duration_minutes=duration,
            notes=notes
        )

        db.session.add(plan)
        db.session.flush()  # Get the plan ID

        # Add drills to the plan
        drill_ids = request.form.getlist('drill_ids[]')
        drill_durations = request.form.getlist('drill_durations[]')

        for order, (drill_id, drill_duration) in enumerate(zip(drill_ids, drill_durations)):
            plan_drill = PlanDrill(
                plan_id=plan.id,
                drill_id=int(drill_id),
                order=order,
                duration_minutes=int(drill_duration)
            )
            db.session.add(plan_drill)

        db.session.commit()

        flash(f'Practice plan "{name}" created successfully!', 'success')
        return redirect(url_for('main.practice_plan_detail', plan_id=plan.id))

    # GET request - show the practice plan builder
    # Get suggested drills based on team attributes
    suggested_drills = get_suggested_drills(team)

    return render_template('practice_plan_form.html', team=team, suggested_drills=suggested_drills)

@bp.route('/plan/<int:plan_id>')
def practice_plan_detail(plan_id):
    """View a practice plan"""
    plan = PracticePlan.query.get_or_404(plan_id)
    return render_template('practice_plan_detail.html', plan=plan)

@bp.route('/team/<int:team_id>/plans')
def team_practice_plans(team_id):
    """List all practice plans for a team"""
    team = Team.query.get_or_404(team_id)
    plans = PracticePlan.query.filter_by(team_id=team_id).order_by(PracticePlan.created_at.desc()).all()
    return render_template('team_practice_plans.html', team=team, plans=plans)

@bp.route('/api/drills/suggest/<int:team_id>')
def api_suggest_drills(team_id):
    """API endpoint to get suggested drills for a team"""
    team = Team.query.get_or_404(team_id)
    drills = get_suggested_drills(team)

    return jsonify([{
        'id': d.id,
        'name': d.name,
        'category': d.category,
        'skill_level': d.skill_level,
        'duration_minutes': d.duration_minutes,
        'description': d.description
    } for d in drills])

def get_suggested_drills(team):
    """Get drills suggested for a team based on their attributes"""
    query = Drill.query

    # Filter by skill level
    if team.skill_level:
        query = query.filter(Drill.skill_level == team.skill_level)

    # Filter by age group (check if team's age group is in recommended_age_groups)
    if team.age_group:
        query = query.filter(Drill.recommended_age_groups.contains(team.age_group))

    # Get all matching drills
    drills = query.all()

    # If we have focus areas, prioritize drills that match
    if team.focus_areas:
        focus_list = team.focus_areas_list
        scored_drills = []

        for drill in drills:
            score = 0
            if drill.focus_areas:
                drill_focus = [f.strip() for f in drill.focus_areas.split(',')]
                # Count matching focus areas
                matches = len(set(focus_list) & set(drill_focus))
                score = matches
            scored_drills.append((drill, score))

        # Sort by score (descending) and return
        scored_drills.sort(key=lambda x: x[1], reverse=True)
        return [d[0] for d in scored_drills]

    return drills
