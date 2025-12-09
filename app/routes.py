"""
Application routes for Soccer Practice Planner

This module contains all Flask routes for the application, organized into sections:
- Home/Landing
- Team Management
- Drill Catalog
- Practice Plan Management
- Session Templates
- Utility/API Routes
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, send_file
from app import db
from app.models import Team, Player, Drill, PracticePlan, PlanDrill, SessionTemplate, TemplateDrill
from datetime import datetime
import csv
import io

bp = Blueprint('main', __name__)

# ============================================================================
# HOME / LANDING
# ============================================================================

@bp.route('/')
def index():
    """Welcome screen / landing page"""
    return render_template('welcome-v3.html')


# ============================================================================
# TEAM MANAGEMENT
# ============================================================================

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


# ============================================================================
# DRILL CATALOG
# ============================================================================

@bp.route('/drills')
def drills_catalog():
    """Drill catalog - browse all drills"""
    category = request.args.get('category', 'All')
    skill_level = request.args.get('skill_level', 'All')
    search_query = request.args.get('search', '')
    age_group = request.args.get('age_group', 'All')

    query = Drill.query

    if category != 'All':
        query = query.filter_by(category=category)

    if skill_level != 'All':
        query = query.filter_by(skill_level=skill_level)

    # Apply search filter
    if search_query:
        query = query.filter(
            db.or_(
                Drill.name.ilike(f'%{search_query}%'),
                Drill.description.ilike(f'%{search_query}%')
            )
        )

    # Apply age group filter
    if age_group != 'All':
        query = query.filter(Drill.recommended_age_groups.ilike(f'%{age_group}%'))

    drills = query.order_by(Drill.name).all()

    return render_template('drills_catalog.html', drills=drills,
                         selected_category=category,
                         selected_skill=skill_level)

@bp.route('/drill/<int:drill_id>')
def drill_detail(drill_id):
    """View detailed information about a specific drill"""
    drill = Drill.query.get_or_404(drill_id)
    return render_template('drill_detail.html', drill=drill)


# ============================================================================
# SESSION TEMPLATES
# ============================================================================

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
            'category': td.drill.category,
            'diagram': td.drill.diagram_url if td.drill.diagram_url else ''
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


# ============================================================================
# PRACTICE PLAN MANAGEMENT
# ============================================================================

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


# ============================================================================
# UTILITY & API ROUTES
# ============================================================================

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


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

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

@bp.route('/drills/import', methods=['GET', 'POST'])
def import_drills():
    """Import drills from CSV file"""
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file selected', 'danger')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('No file selected', 'danger')
            return redirect(request.url)

        if not file.filename.endswith('.csv'):
            flash('Please upload a CSV file', 'danger')
            return redirect(request.url)

        try:
            # Read CSV file
            stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
            csv_reader = csv.DictReader(stream)

            imported_count = 0
            skipped_count = 0
            errors = []

            for row_num, row in enumerate(csv_reader, start=2):  # Start at 2 (header is row 1)
                try:
                    # Check if drill with same name already exists
                    existing = Drill.query.filter_by(name=row['name'].strip()).first()
                    if existing:
                        skipped_count += 1
                        continue

                    # Create new drill
                    drill = Drill(
                        name=row['name'].strip(),
                        category=row['category'].strip(),
                        sub_category=row.get('sub_category', '').strip() if row.get('sub_category') else None,
                        description=row['description'].strip(),
                        equipment_needed=row.get('equipment_needed', '').strip() if row.get('equipment_needed') else None,
                        min_players=int(row['min_players']) if row.get('min_players') and row['min_players'].strip() else 4,
                        max_players=int(row['max_players']) if row.get('max_players') and row['max_players'].strip() else 20,
                        recommended_age_groups=row.get('recommended_age_groups', '').strip() if row.get('recommended_age_groups') else None,
                        skill_level=row.get('skill_level', '').strip() if row.get('skill_level') else 'All',
                        duration_minutes=int(row['duration_minutes']) if row.get('duration_minutes') and row['duration_minutes'].strip() else None,
                        focus_areas=row.get('focus_areas', '').strip() if row.get('focus_areas') else None,
                        diagram_url=row.get('diagram_url', '').strip() if row.get('diagram_url') else None
                    )

                    db.session.add(drill)
                    imported_count += 1

                except Exception as e:
                    errors.append(f"Row {row_num}: {str(e)}")
                    continue

            # Commit all drills
            db.session.commit()

            # Show results
            if imported_count > 0:
                flash(f'Successfully imported {imported_count} drill(s)!', 'success')
            if skipped_count > 0:
                flash(f'Skipped {skipped_count} duplicate drill(s)', 'info')
            if errors:
                flash(f'Errors: {"; ".join(errors[:5])}', 'warning')  # Show first 5 errors

            return redirect(url_for('main.drills'))

        except Exception as e:
            flash(f'Error processing CSV file: {str(e)}', 'danger')
            return redirect(request.url)

    return render_template('import_drills.html')

@bp.route('/drills/import/template')
def download_import_template():
    """Download CSV template for importing drills"""
    # Create CSV template
    output = io.StringIO()
    writer = csv.writer(output)

    # Write header
    writer.writerow([
        'name', 'category', 'sub_category', 'description', 'equipment_needed',
        'min_players', 'max_players', 'recommended_age_groups', 'skill_level',
        'duration_minutes', 'focus_areas', 'diagram_url'
    ])

    # Write example rows
    writer.writerow([
        'Passing Triangle',
        'Technical',
        'Passing',
        'Players form a triangle and practice one-touch passing. Focus on accuracy and weight of pass.',
        'Balls, cones',
        '3',
        '6',
        'U9,U10,U11,U12',
        'Beginner',
        '15',
        'Passing accuracy, First touch, Communication',
        ''
    ])

    writer.writerow([
        'Rondo 4v1',
        'Technical',
        'Possession',
        'Four players keep possession from one defender in a small grid. Develop quick decision-making.',
        'Balls, cones',
        '5',
        '10',
        'U10,U11,U12,U13',
        'Intermediate',
        '20',
        'Possession, Passing, Awareness',
        ''
    ])

    # Create response
    output.seek(0)
    return send_file(
        io.BytesIO(output.getvalue().encode('utf-8')),
        mimetype='text/csv',
        as_attachment=True,
        download_name='drill_import_template.csv'
    )

@bp.route('/plan/<int:plan_id>/delete', methods=['POST'])
def delete_practice_plan(plan_id):
    """Delete a practice plan"""
    plan = PracticePlan.query.get_or_404(plan_id)
    team_id = plan.team_id

    # Delete associated plan drills first
    PlanDrill.query.filter_by(plan_id=plan_id).delete()

    # Delete the plan
    db.session.delete(plan)
    db.session.commit()

    flash(f'Practice plan "{plan.name}" deleted successfully!', 'success')
    return redirect(url_for('main.team_practice_plans', team_id=team_id))

@bp.route('/plan/<int:plan_id>/duplicate', methods=['POST'])
def duplicate_practice_plan(plan_id):
    """Duplicate a practice plan"""
    original_plan = PracticePlan.query.get_or_404(plan_id)

    # Create new plan with copied data
    new_plan = PracticePlan(
        team_id=original_plan.team_id,
        name=f"{original_plan.name} (Copy)",
        practice_date=original_plan.practice_date,
        duration_minutes=original_plan.duration_minutes,
        focus_areas=original_plan.focus_areas,
        notes=original_plan.notes
    )
    db.session.add(new_plan)
    db.session.flush()

    # Copy all drills
    for plan_drill in original_plan.plan_drills:
        new_plan_drill = PlanDrill(
            plan_id=new_plan.id,
            drill_id=plan_drill.drill_id,
            order=plan_drill.order,
            duration_minutes=plan_drill.duration_minutes,
            notes=plan_drill.notes
        )
        db.session.add(new_plan_drill)

    db.session.commit()

    flash(f'Practice plan duplicated successfully!', 'success')
    return redirect(url_for('main.practice_plan_detail', plan_id=new_plan.id))

@bp.route('/plan/<int:plan_id>/print')
def print_practice_plan(plan_id):
    """Print-friendly view of practice plan"""
    plan = PracticePlan.query.get_or_404(plan_id)
    return render_template('practice_plan_print.html', plan=plan)

@bp.route('/plan/<int:plan_id>/edit', methods=['GET', 'POST'])
def edit_practice_plan(plan_id):
    """Edit an existing practice plan"""
    plan = PracticePlan.query.get_or_404(plan_id)
    team = plan.team

    if request.method == 'POST':
        # Update plan details
        plan.name = request.form.get('name')
        plan.duration_minutes = int(request.form.get('duration_minutes'))
        plan.notes = request.form.get('notes')

        # Delete existing plan drills
        PlanDrill.query.filter_by(plan_id=plan.id).delete()

        # Add updated drills
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

        flash(f'Practice plan "{plan.name}" updated successfully!', 'success')
        return redirect(url_for('main.practice_plan_detail', plan_id=plan.id))

    # GET request - show edit form with existing data
    suggested_drills = get_suggested_drills(team)
    return render_template('practice_plan_edit.html', plan=plan, team=team, suggested_drills=suggested_drills)
