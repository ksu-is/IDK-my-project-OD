"""Generate diagrams for all drills in the database"""
from app import create_app, db
from app.models import Drill
from app.utils.diagram_generator import save_drill_diagram

def generate_all_diagrams():
    """Generate diagrams for all drills"""
    app = create_app()

    with app.app_context():
        drills = Drill.query.all()

        print(f"Generating diagrams for {len(drills)} drills...")

        for drill in drills:
            print(f"  - Generating diagram for: {drill.name}")
            diagram_url = save_drill_diagram(drill.name, drill.id)

            if diagram_url:
                drill.diagram_url = diagram_url
                print(f"    ✓ Saved to {diagram_url}")
            else:
                print(f"    ⚠ No diagram generator for this drill yet")

        db.session.commit()
        print("\n✓ All diagrams generated successfully!")

if __name__ == '__main__':
    generate_all_diagrams()
