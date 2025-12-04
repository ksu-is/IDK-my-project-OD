"""Practice Plan model for storing training sessions"""
from app import db
from datetime import datetime

class PracticePlan(db.Model):
    """Model for practice plans/training sessions"""
    __tablename__ = 'practice_plans'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)  # Total session duration
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.Column(db.Text)
    is_completed = db.Column(db.Boolean, default=False)
    completed_at = db.Column(db.DateTime)

    # Relationship to team
    team = db.relationship('Team', backref=db.backref('practice_plans', lazy=True))

    # Relationship to drills (many-to-many through PlanDrill)
    plan_drills = db.relationship('PlanDrill', backref='practice_plan', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<PracticePlan {self.name}>'

    @property
    def total_drill_time(self):
        """Calculate total time allocated to drills"""
        return sum(pd.duration_minutes for pd in self.plan_drills)

    @property
    def drills_count(self):
        """Get the number of drills in this plan"""
        return len(self.plan_drills)


class PlanDrill(db.Model):
    """Association model for practice plans and drills with ordering and duration"""
    __tablename__ = 'plan_drills'

    id = db.Column(db.Integer, primary_key=True)
    plan_id = db.Column(db.Integer, db.ForeignKey('practice_plans.id'), nullable=False)
    drill_id = db.Column(db.Integer, db.ForeignKey('drills.id'), nullable=False)
    order = db.Column(db.Integer, nullable=False)  # Order in the practice plan
    duration_minutes = db.Column(db.Integer, nullable=False)  # How long to run this drill
    notes = db.Column(db.Text)  # Specific notes for this drill in this plan

    # Relationship to drill
    drill = db.relationship('Drill', backref=db.backref('plan_drills', lazy=True))

    def __repr__(self):
        return f'<PlanDrill plan={self.plan_id} drill={self.drill_id} order={self.order}>'
