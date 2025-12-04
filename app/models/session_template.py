"""Session Template model for pre-built practice sessions"""
from app import db

class SessionTemplate(db.Model):
    """Model for pre-built practice session templates"""
    __tablename__ = 'session_templates'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)  # e.g., "Building Out of the Back"
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)  # Attacking, Defending, Transition, Possession
    recommended_age_groups = db.Column(db.String(100))  # U9, U10, U12, etc.
    skill_level = db.Column(db.String(20))  # Beginner, Intermediate, Advanced
    total_duration = db.Column(db.Integer, nullable=False)  # Total minutes
    focus_areas = db.Column(db.Text)  # Comma-separated

    # Relationship to template drills
    template_drills = db.relationship('TemplateDrill', backref='session_template', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<SessionTemplate {self.name}>'

    @property
    def drills_count(self):
        """Get the number of drills in this template"""
        return len(self.template_drills)


class TemplateDrill(db.Model):
    """Association model for session templates and drills"""
    __tablename__ = 'template_drills'

    id = db.Column(db.Integer, primary_key=True)
    template_id = db.Column(db.Integer, db.ForeignKey('session_templates.id'), nullable=False)
    drill_id = db.Column(db.Integer, db.ForeignKey('drills.id'), nullable=False)
    order = db.Column(db.Integer, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text)

    # Relationship to drill
    drill = db.relationship('Drill', backref=db.backref('template_drills', lazy=True))

    def __repr__(self):
        return f'<TemplateDrill template={self.template_id} drill={self.drill_id}>'
