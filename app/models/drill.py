"""Drill model for storing soccer drill information"""
from app import db
from datetime import datetime

class Drill(db.Model):
    """Model representing a soccer drill"""
    __tablename__ = 'drills'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # Technical, Tactical, Physical, Fun
    sub_category = db.Column(db.String(50))  # Passing, Shooting, Dribbling, etc.
    description = db.Column(db.Text, nullable=False)
    equipment_needed = db.Column(db.Text)  # Balls, cones, goals, etc.
    min_players = db.Column(db.Integer, default=4)
    max_players = db.Column(db.Integer, default=20)
    recommended_age_groups = db.Column(db.String(100))  # e.g., "U9,U10,U12"
    skill_level = db.Column(db.String(20))  # Beginner, Intermediate, Advanced, All
    duration_minutes = db.Column(db.Integer)  # Recommended duration
    focus_areas = db.Column(db.Text)  # What this drill trains (passing accuracy, first touch, etc.)
    setup_instructions = db.Column(db.Text)  # How to set up the drill
    coaching_points = db.Column(db.Text)  # Key coaching points
    variations = db.Column(db.Text)  # Drill variations to increase/decrease difficulty
    diagram_url = db.Column(db.String(200))  # Path to diagram image
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Drill {self.name} - {self.category}>'

    @property
    def age_groups_list(self):
        """Convert age groups string to list"""
        if self.recommended_age_groups:
            return [age.strip() for age in self.recommended_age_groups.split(',')]
        return []

    @property
    def is_suitable_for_age(self, age_group):
        """Check if drill is suitable for a specific age group"""
        return age_group in self.age_groups_list or self.skill_level == 'All'
