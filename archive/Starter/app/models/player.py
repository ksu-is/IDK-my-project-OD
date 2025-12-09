"""Player model for storing individual player information"""
from app import db

class Player(db.Model):
    """Model representing a player on a team"""
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(50))  # Forward, Midfielder, Defender, Goalkeeper
    skill_level = db.Column(db.String(20))  # Beginner, Intermediate, Advanced
    special_needs = db.Column(db.Text)  # Any specific training needs or considerations
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)

    def __repr__(self):
        return f'<Player {self.name} - {self.position}>'
