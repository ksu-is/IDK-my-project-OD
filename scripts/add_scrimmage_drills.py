"""Add proper scrimmage drills to the database"""
from app import create_app, db
from app.models import Drill

def add_scrimmage_drills():
    app = create_app()
    
    with app.app_context():
        # Check if scrimmage drills already exist
        existing = Drill.query.filter(Drill.name.like('%Scrimmage%')).all()
        if existing:
            print(f"Found {len(existing)} existing scrimmage drills. Skipping...")
            return
        
        scrimmage_drills = [
            {
                'name': '7v7 Scrimmage',
                'description': 'Full-field 7v7 game for U9-U10 (Academy). Regular soccer rules, let players apply session concepts in game context.',
                'category': 'Game',
                'min_players': 14,
                'equipment': 'Full field, goals, pinnies',
                'diagram_url': None
            },
            {
                'name': '9v9 Scrimmage',
                'description': 'Full-field 9v9 game for U11-U12 (Academy). Regular soccer rules, let players apply session concepts in game context.',
                'category': 'Game',
                'min_players': 18,
                'equipment': 'Full field, goals, pinnies',
                'diagram_url': None
            },
            {
                'name': '11v11 Scrimmage',
                'description': 'Full-field 11v11 game for U13+ (Select). Regular soccer rules with minimal intervention, allow players to apply tactical and technical concepts.',
                'category': 'Game',
                'min_players': 22,
                'equipment': 'Full field, goals, pinnies',
                'diagram_url': None
            },
            {
                'name': '4v4 Small-Sided Game',
                'description': 'Small-sided game with small goals or target goals. Great for ending technical sessions, high touches per player.',
                'category': 'Game',
                'min_players': 8,
                'equipment': 'Small field (30x40 yards), small goals or cones, pinnies',
                'diagram_url': None
            },
            {
                'name': '6v6 Small-Sided Game',
                'description': 'Medium small-sided game. Can be used as scrimmage for younger age groups or as progression game for Select.',
                'category': 'Game',
                'min_players': 12,
                'equipment': 'Medium field (40x50 yards), goals, pinnies',
                'diagram_url': None
            },
            {
                'name': '8v8 Scrimmage',
                'description': 'Three-quarter field scrimmage. Good for Select teams to practice in slightly constrained space before full 11v11.',
                'category': 'Game',
                'min_players': 16,
                'equipment': 'Three-quarter field, goals, pinnies',
                'diagram_url': None
            }
        ]
        
        for drill_data in scrimmage_drills:
            drill = Drill(**drill_data)
            db.session.add(drill)
            print(f"Added: {drill.name}")
        
        db.session.commit()
        print(f"\n✓ Successfully added {len(scrimmage_drills)} scrimmage drills!")

if __name__ == '__main__':
    add_scrimmage_drills()
