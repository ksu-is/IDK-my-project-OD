"""Populate database with improved session templates based on coaching best practices"""
from app import create_app, db
from app.models import SessionTemplate, TemplateDrill, Drill

def create_improved_templates():
    app = create_app()

    with app.app_context():
        # Clear existing templates
        print("Clearing existing session templates...")
        SessionTemplate.query.delete()
        db.session.commit()

        # Get existing drills
        drills = {drill.name: drill for drill in Drill.query.all()}

        # ============================================================================
        # ACADEMY TEMPLATES (U9-U12) - Focus on Technical Development
        # ============================================================================

        # Template 1: Academy - Dribbling Fundamentals
        template1 = SessionTemplate(
            name="Academy: Dribbling Fundamentals",
            description="Technical session focused on dribbling technique, close control, and 1v1 moves. Progressive activities building from basic ball control to game application.",
            category="Technical",
            recommended_age_groups="U9, U10, U11, U12",
            skill_level="Beginner",
            total_duration=90,
            focus_areas="Dribbling, Ball Control, 1v1"
        )
        db.session.add(template1)
        db.session.flush()

        # Warm-up: Fun ball touches (12 min)
        if 'Sharks and Minnows' in drills:
            db.session.add(TemplateDrill(
                template_id=template1.id,
                drill_id=drills['Sharks and Minnows'].id,
                order=0,
                duration_minutes=12,
                notes="Warm-up: Get comfortable with ball at feet, basic dribbling"
            ))

        # Activity 1: Technical repetition (20 min)
        if '1v1 Dribbling Race' in drills:
            db.session.add(TemplateDrill(
                template_id=template1.id,
                drill_id=drills['1v1 Dribbling Race'].id,
                order=1,
                duration_minutes=20,
                notes="Activity 1: Focus on dribbling technique - demonstrate proper touches, body position"
            ))

        # Activity 2: Small-sided with dribbling emphasis (28 min)
        if '4v4+2 Possession' in drills:
            db.session.add(TemplateDrill(
                template_id=template1.id,
                drill_id=drills['4v4+2 Possession'].id,
                order=2,
                duration_minutes=28,
                notes="Activity 2: Modified - bonus points for successful dribbles past opponent. 4v4 small-sided game."
            ))

        # Scrimmage: Apply in game (30 min)
        if '7v7 Scrimmage' in drills:
            db.session.add(TemplateDrill(
                template_id=template1.id,
                drill_id=drills['7v7 Scrimmage'].id,
                order=3,
                duration_minutes=30,
                notes="Scrimmage: 7v7 game - let them apply dribbling skills in real game situations"
            ))

        # Template 2: Academy - Passing Technique
        template2 = SessionTemplate(
            name="Academy: Passing Technique & Vision",
            description="Develop proper passing technique with inside of foot, receiving skills, and basic awareness. Small-sided games emphasize accurate passing.",
            category="Technical",
            recommended_age_groups="U9, U10, U11, U12",
            skill_level="Beginner",
            total_duration=90,
            focus_areas="Passing, First Touch, Vision"
        )
        db.session.add(template2)
        db.session.flush()

        # Warm-up: Passing rondo (15 min)
        if 'Passing Square' in drills:
            db.session.add(TemplateDrill(
                template_id=template2.id,
                drill_id=drills['Passing Square'].id,
                order=0,
                duration_minutes=15,
                notes="Warm-up: Focus on technique - inside of foot, proper weight on pass"
            ))

        # Activity 1: Passing patterns (25 min)
        if '4v4+2 Possession' in drills:
            db.session.add(TemplateDrill(
                template_id=template2.id,
                drill_id=drills['4v4+2 Possession'].id,
                order=1,
                duration_minutes=25,
                notes="Activity 1: 4v2 possession - emphasize quick passing and receiving technique"
            ))

        # Activity 2: Passing to score (20 min)
        if '3v2 Defending Shape' in drills:
            db.session.add(TemplateDrill(
                template_id=template2.id,
                drill_id=drills['3v2 Defending Shape'].id,
                order=2,
                duration_minutes=20,
                notes="Activity 2: Small-sided game with targets - must complete passes before scoring"
            ))

        # Scrimmage (30 min)
        if '9v9 Scrimmage' in drills:
            db.session.add(TemplateDrill(
                template_id=template2.id,
                drill_id=drills['9v9 Scrimmage'].id,
                order=3,
                duration_minutes=30,
                notes="Scrimmage: 9v9 game - encourage passing combinations and vision in game context"
            ))

        # Template 3: Academy - Introduction to Building Out
        template3 = SessionTemplate(
            name="Academy: Introduction to Building Out",
            description="Simplified tactical session on playing out from the back. Focus on basic positioning and passing out of pressure. Smaller numbers, simpler concepts.",
            category="Tactical",
            recommended_age_groups="U11, U12",
            skill_level="Intermediate",
            total_duration=90,
            focus_areas="Passing, Possession, Tactical Awareness"
        )
        db.session.add(template3)
        db.session.flush()

        # Warm-up: Basic possession (12 min)
        if 'Passing Square' in drills:
            db.session.add(TemplateDrill(
                template_id=template3.id,
                drill_id=drills['Passing Square'].id,
                order=0,
                duration_minutes=12,
                notes="Warm-up: Keep-away game to get touches"
            ))

        # Activity 1: 3v2 out of back (20 min)
        if '3v2 Defending Shape' in drills:
            db.session.add(TemplateDrill(
                template_id=template3.id,
                drill_id=drills['3v2 Defending Shape'].id,
                order=1,
                duration_minutes=20,
                notes="Activity 1: Simplified - 3 defenders pass through 2 opponents. Teach basic positioning."
            ))

        # Activity 2: Small-sided with building emphasis (28 min)
        if '4v4+2 Possession' in drills:
            db.session.add(TemplateDrill(
                template_id=template3.id,
                drill_id=drills['4v4+2 Possession'].id,
                order=2,
                duration_minutes=28,
                notes="Activity 2: 5v5 with GK - must complete 3 passes before attacking. Score in small goals."
            ))

        # Scrimmage (30 min)
        if '6v6 Small-Sided Game' in drills:
            db.session.add(TemplateDrill(
                template_id=template3.id,
                drill_id=drills['6v6 Small-Sided Game'].id,
                order=3,
                duration_minutes=30,
                notes="Scrimmage: 6v6 game - observe if they use building out concepts from session"
            ))

        # ============================================================================
        # SELECT TEMPLATES (U13+) - Focus on Tactical Development
        # ============================================================================

        # Template 4: Select - Building Out of the Back (Advanced)
        template4 = SessionTemplate(
            name="Select: Building Out of the Back",
            description="Advanced tactical session on playing out from defensive third into midfield. Emphasizes positioning, passing patterns, and decision-making under pressure.",
            category="Tactical",
            recommended_age_groups="U13, U14, U15, U16",
            skill_level="Intermediate",
            total_duration=90,
            focus_areas="Passing, Possession, Tactical Awareness, Building Out"
        )
        db.session.add(template4)
        db.session.flush()

        # Warm-up: Rondo (12 min)
        if 'Passing Square' in drills:
            db.session.add(TemplateDrill(
                template_id=template4.id,
                drill_id=drills['Passing Square'].id,
                order=0,
                duration_minutes=12,
                notes="Warm-up: 4v2 Rondo - quick passing, movement off ball"
            ))

        # Activity 1: Pattern play with targets (20 min)
        if '4v4+2 Possession' in drills:
            db.session.add(TemplateDrill(
                template_id=template4.id,
                drill_id=drills['4v4+2 Possession'].id,
                order=1,
                duration_minutes=20,
                notes="Activity 1: 4v2 +2 wide +2 forward. Must play to wide/forward targets to establish pattern."
            ))

        # Activity 2: Half-field progression (28 min)
        if '3v2 Defending Shape' in drills:
            db.session.add(TemplateDrill(
                template_id=template4.id,
                drill_id=drills['3v2 Defending Shape'].id,
                order=2,
                duration_minutes=28,
                notes="Activity 2: 6+GK v 6 on half field. Score in 3 small goals on halfway line. Apply building out concepts."
            ))

        # Scrimmage (30 min)
        if '11v11 Scrimmage' in drills:
            db.session.add(TemplateDrill(
                template_id=template4.id,
                drill_id=drills['11v11 Scrimmage'].id,
                order=3,
                duration_minutes=30,
                notes="Scrimmage: 11v11 game. Minimal intervention - let them apply building out concepts."
            ))

        # Template 5: Select - Attacking in Final Third
        template5 = SessionTemplate(
            name="Select: Attacking in the Final Third",
            description="Tactical session focused on creating and exploiting space in attacking third. Emphasizes combination play, movement off ball, and finishing.",
            category="Tactical",
            recommended_age_groups="U13, U14, U15, U16",
            skill_level="Intermediate",
            total_duration=90,
            focus_areas="Attacking, Shooting, Combination Play, Movement"
        )
        db.session.add(template5)
        db.session.flush()

        # Warm-up: Possession (12 min)
        if 'Passing Square' in drills:
            db.session.add(TemplateDrill(
                template_id=template5.id,
                drill_id=drills['Passing Square'].id,
                order=0,
                duration_minutes=12,
                notes="Warm-up: Quick passing rondo to get touches"
            ))

        # Activity 1: Shooting combinations (20 min)
        if 'Shooting from Distance' in drills:
            db.session.add(TemplateDrill(
                template_id=template5.id,
                drill_id=drills['Shooting from Distance'].id,
                order=1,
                duration_minutes=20,
                notes="Activity 1: Combination play into shooting. Work on give-and-go, overlaps, through balls."
            ))

        # Activity 2: Final third overloads (28 min)
        if '4v4+2 Possession' in drills:
            db.session.add(TemplateDrill(
                template_id=template5.id,
                drill_id=drills['4v4+2 Possession'].id,
                order=2,
                duration_minutes=28,
                notes="Activity 2: 6v4 in attacking third. Create overload situations, finish in big goal."
            ))

        # Scrimmage (30 min)
        if '8v8 Scrimmage' in drills:
            db.session.add(TemplateDrill(
                template_id=template5.id,
                drill_id=drills['8v8 Scrimmage'].id,
                order=3,
                duration_minutes=30,
                notes="Scrimmage: 8v8 or 11v11 game. Focus on attacking patterns in final third."
            ))

        # Template 6: Select - Defensive Organization & Pressing
        template6 = SessionTemplate(
            name="Select: Defensive Organization & Pressing",
            description="Tactical session on defensive shape, pressing triggers, and winning the ball back. Emphasizes team organization and tactical discipline.",
            category="Tactical",
            recommended_age_groups="U13, U14, U15, U16",
            skill_level="Intermediate",
            total_duration=90,
            focus_areas="Defending, Tactical Awareness, Pressing, Teamwork"
        )
        db.session.add(template6)
        db.session.flush()

        # Warm-up: Possession (12 min)
        if 'Passing Square' in drills:
            db.session.add(TemplateDrill(
                template_id=template6.id,
                drill_id=drills['Passing Square'].id,
                order=0,
                duration_minutes=12,
                notes="Warm-up: Rondo to get touches and warm up"
            ))

        # Activity 1: Defensive positioning (20 min)
        if '3v2 Defending Shape' in drills:
            db.session.add(TemplateDrill(
                template_id=template6.id,
                drill_id=drills['3v2 Defending Shape'].id,
                order=1,
                duration_minutes=20,
                notes="Activity 1: Teach defensive shape, pressing triggers, cover and balance"
            ))

        # Activity 2: Pressing scenarios (28 min)
        if '4v4+2 Possession' in drills:
            db.session.add(TemplateDrill(
                template_id=template6.id,
                drill_id=drills['4v4+2 Possession'].id,
                order=2,
                duration_minutes=28,
                notes="Activity 2: 6v6 - defending team works on pressing, winning ball back, counter-attacking"
            ))

        # Scrimmage (30 min)
        if '11v11 Scrimmage' in drills:
            db.session.add(TemplateDrill(
                template_id=template6.id,
                drill_id=drills['11v11 Scrimmage'].id,
                order=3,
                duration_minutes=30,
                notes="Scrimmage: 11v11 game. Observe defensive organization and pressing principles in game"
            ))

        # Template 7: Academy - Fun & Skills Session
        template7 = SessionTemplate(
            name="Academy: Fun & Skills Challenge",
            description="High-energy session combining fun games with skill development. Perfect for keeping young players engaged while developing technical abilities.",
            category="Fun",
            recommended_age_groups="U9, U10",
            skill_level="Beginner",
            total_duration=90,
            focus_areas="Ball Control, Dribbling, Fun, Teamwork"
        )
        db.session.add(template7)
        db.session.flush()

        # Warm-up (12 min)
        if 'Sharks and Minnows' in drills:
            db.session.add(TemplateDrill(
                template_id=template7.id,
                drill_id=drills['Sharks and Minnows'].id,
                order=0,
                duration_minutes=12,
                notes="Warm-up: Fun game to get them moving and laughing"
            ))

        # Activity 1 (20 min)
        if '1v1 Dribbling Race' in drills:
            db.session.add(TemplateDrill(
                template_id=template7.id,
                drill_id=drills['1v1 Dribbling Race'].id,
                order=1,
                duration_minutes=20,
                notes="Activity 1: Competition and skill challenges"
            ))

        # Activity 2 (28 min)
        if 'Passing Square' in drills:
            db.session.add(TemplateDrill(
                template_id=template7.id,
                drill_id=drills['Passing Square'].id,
                order=2,
                duration_minutes=28,
                notes="Activity 2: Team passing challenges - make it competitive and fun"
            ))

        # Scrimmage (30 min)
        if '4v4 Small-Sided Game' in drills:
            db.session.add(TemplateDrill(
                template_id=template7.id,
                drill_id=drills['4v4 Small-Sided Game'].id,
                order=3,
                duration_minutes=30,
                notes="Scrimmage: Fun 4v4 games - keep score, celebrate goals!"
            ))

        db.session.commit()
        print("\n✓ Created 7 improved session templates!")
        print("\nACADEMY TEMPLATES (U9-U12):")
        print("  1. Academy: Dribbling Fundamentals (Technical)")
        print("  2. Academy: Passing Technique & Vision (Technical)")
        print("  3. Academy: Introduction to Building Out (Tactical - Simplified)")
        print("  4. Academy: Fun & Skills Challenge (Fun)")
        print("\nSELECT TEMPLATES (U13+):")
        print("  5. Select: Building Out of the Back (Tactical - Advanced)")
        print("  6. Select: Attacking in the Final Third (Tactical)")
        print("  7. Select: Defensive Organization & Pressing (Tactical)")
        print("\nAll templates follow proper progression:")
        print("  - Warm-up (ball focused for Academy)")
        print("  - Activity 1 (introduce concept)")
        print("  - Activity 2 (build on concept)")
        print("  - Scrimmage (apply in game)")

if __name__ == '__main__':
    create_improved_templates()
