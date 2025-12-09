"""Team model for storing team information"""
from app import db
from datetime import datetime

class Team(db.Model):
    """Model representing a soccer team"""
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age_group = db.Column(db.String(10), nullable=False)  # U9, U10, U12, U14, U16
    skill_level = db.Column(db.String(20), nullable=False)  # Beginner, Intermediate, Advanced
    num_players = db.Column(db.Integer, nullable=False)
    focus_areas = db.Column(db.Text)  # Comma-separated areas (passing, shooting, defending, etc.)
    additional_notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship with players
    players = db.relationship('Player', backref='team', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Team {self.name} - {self.age_group}>'

    @property
    def recommended_session_duration(self):
        """Return recommended practice duration in minutes based on age"""
        duration_map = {
            'U9': 60,
            'U10': 75,
            'U12': 90,
            'U14': 90,
            'U16': 105
        }
        return duration_map.get(self.age_group, 90)

    @property
    def focus_areas_list(self):
        """Convert focus areas string to list"""
        if self.focus_areas:
            return [area.strip() for area in self.focus_areas.split(',')]
        return []
