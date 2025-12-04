"""Populate database with pre-built session templates"""
from app import create_app, db
from app.models import SessionTemplate, TemplateDrill, Drill

def create_templates():
    app = create_app()

    with app.app_context():
        # Check if templates already exist
        if SessionTemplate.query.count() > 0:
            print("Session templates already exist. Skipping...")
            return

        # Get existing drills
        drills = {drill.name: drill for drill in Drill.query.all()}

        # Template 1: Building Out of the Back
        template1 = SessionTemplate(
            name="Building Out of the Back",
            description="Focus on playing out from the goalkeeper and defensive third. Emphasis on composure under pressure and creating passing lanes.",
            category="Possession",
            recommended_age_groups="U12, U14, U16",
            skill_level="Intermediate",
            total_duration=90,
            focus_areas="Passing, Possession, Tactical Awareness"
        )
        db.session.add(template1)
        db.session.flush()

        # Add drills to template 1
        if 'Passing Square' in drills:
            db.session.add(TemplateDrill(
                template_id=template1.id,
                drill_id=drills['Passing Square'].id,
                order=0,
                duration_minutes=15,
                notes="Warm-up with focus on quick passing"
            ))

        if '4v4+2 Possession' in drills:
            db.session.add(TemplateDrill(
                template_id=template1.id,
                drill_id=drills['4v4+2 Possession'].id,
                order=1,
                duration_minutes=25,
                notes="Main drill - maintain possession and switch play"
            ))

        if '3v2 Defending Shape' in drills:
            db.session.add(TemplateDrill(
                template_id=template1.id,
                drill_id=drills['3v2 Defending Shape'].id,
                order=2,
                duration_minutes=20,
                notes="Practice defensive organization when ball is lost"
            ))

        if 'World Cup Tournament' in drills:
            db.session.add(TemplateDrill(
                template_id=template1.id,
                drill_id=drills['World Cup Tournament'].id,
                order=3,
                duration_minutes=30,
                notes="Small-sided games to apply building out concepts"
            ))

        # Template 2: High-Intensity Attacking
        template2 = SessionTemplate(
            name="High-Intensity Attacking",
            description="Fast-paced session focused on attacking speed, finishing, and exploiting space in the final third.",
            category="Attacking",
            recommended_age_groups="U10, U12, U14, U16",
            skill_level="All Levels",
            total_duration=75,
            focus_areas="Shooting, Speed, Attacking"
        )
        db.session.add(template2)
        db.session.flush()

        # Add drills to template 2
        if '1v1 Dribbling Race' in drills:
            db.session.add(TemplateDrill(
                template_id=template2.id,
                drill_id=drills['1v1 Dribbling Race'].id,
                order=0,
                duration_minutes=15,
                notes="High-intensity warm-up"
            ))

        if 'Shooting from Distance' in drills:
            db.session.add(TemplateDrill(
                template_id=template2.id,
                drill_id=drills['Shooting from Distance'].id,
                order=1,
                duration_minutes=25,
                notes="Focus on technique and power"
            ))

        if 'World Cup Tournament' in drills:
            db.session.add(TemplateDrill(
                template_id=template2.id,
                drill_id=drills['World Cup Tournament'].id,
                order=2,
                duration_minutes=35,
                notes="Competitive games with focus on attacking"
            ))

        # Template 3: Defensive Organization
        template3 = SessionTemplate(
            name="Defensive Organization & Shape",
            description="Structured session on maintaining defensive shape, pressing triggers, and recovering positions.",
            category="Defending",
            recommended_age_groups="U12, U14, U16",
            skill_level="Intermediate",
            total_duration=85,
            focus_areas="Defending, Tactical Awareness, Teamwork"
        )
        db.session.add(template3)
        db.session.flush()

        # Add drills to template 3
        if 'Agility Ladder Drills' in drills:
            db.session.add(TemplateDrill(
                template_id=template3.id,
                drill_id=drills['Agility Ladder Drills'].id,
                order=0,
                duration_minutes=10,
                notes="Footwork and agility warm-up"
            ))

        if '3v2 Defending Shape' in drills:
            db.session.add(TemplateDrill(
                template_id=template3.id,
                drill_id=drills['3v2 Defending Shape'].id,
                order=1,
                duration_minutes=25,
                notes="Core defensive positioning drill"
            ))

        if '4v4+2 Possession' in drills:
            db.session.add(TemplateDrill(
                template_id=template3.id,
                drill_id=drills['4v4+2 Possession'].id,
                order=2,
                duration_minutes=20,
                notes="Press and win the ball back"
            ))

        if 'World Cup Tournament' in drills:
            db.session.add(TemplateDrill(
                template_id=template3.id,
                drill_id=drills['World Cup Tournament'].id,
                order=3,
                duration_minutes=30,
                notes="Apply defensive principles in game situations"
            ))

        # Template 4: Fun & Games Session (for younger/beginner teams)
        template4 = SessionTemplate(
            name="Fun & Games Session",
            description="Engaging, game-based session perfect for younger players. Focus on enjoyment while developing skills.",
            category="Fun",
            recommended_age_groups="U9, U10",
            skill_level="Beginner",
            total_duration=60,
            focus_areas="Ball Control, Teamwork, Fun"
        )
        db.session.add(template4)
        db.session.flush()

        # Add drills to template 4
        if 'Sharks and Minnows' in drills:
            db.session.add(TemplateDrill(
                template_id=template4.id,
                drill_id=drills['Sharks and Minnows'].id,
                order=0,
                duration_minutes=15,
                notes="Fun warm-up game"
            ))

        if '1v1 Dribbling Race' in drills:
            db.session.add(TemplateDrill(
                template_id=template4.id,
                drill_id=drills['1v1 Dribbling Race'].id,
                order=1,
                duration_minutes=15,
                notes="Competition and skill development"
            ))

        if 'World Cup Tournament' in drills:
            db.session.add(TemplateDrill(
                template_id=template4.id,
                drill_id=drills['World Cup Tournament'].id,
                order=2,
                duration_minutes=30,
                notes="Tournament-style games"
            ))

        db.session.commit()
        print("✓ Created 4 session templates with drills!")
        print("  1. Building Out of the Back (Possession)")
        print("  2. High-Intensity Attacking")
        print("  3. Defensive Organization & Shape")
        print("  4. Fun & Games Session")

if __name__ == '__main__':
    create_templates()
