#!/usr/bin/env python3
"""
Add more drills to the Soccer Practice Planner catalog
Covers various categories and age groups
"""

from app import create_app, db
from app.models import Drill

def add_more_drills():
    app = create_app()

    with app.app_context():
        # Additional Technical Drills
        technical_drills = [
            {
                'name': 'Wall Pass Combination',
                'category': 'Technical',
                'sub_category': 'Passing',
                'description': 'Players practice one-two combinations with a partner acting as a wall. Focus on quick return passes and movement after the pass.',
                'skill_level': 'Intermediate',
                'min_players': 4,
                'max_players': 20,
                'duration_minutes': 15,
                'recommended_age_groups': 'U10, U11, U12, U13, U14, U15, U16',
                'equipment_needed': 'Balls, Cones',
                'coaching_points': 'First touch away from pressure, weight of pass, check away before receiving, communicate.',
                'focus_areas': 'Passing, Movement, Communication'
            },
            {
                'name': 'Turning with the Ball',
                'category': 'Technical',
                'sub_category': 'Dribbling',
                'description': 'Players practice different turning techniques: inside hook, outside hook, Cruyff turn, and step-over turn.',
                'skill_level': 'Intermediate',
                'min_players': 6,
                'max_players': 20,
                'duration_minutes': 15,
                'recommended_age_groups': 'U10, U11, U12, U13, U14, U15, U16',
                'equipment_needed': 'Balls, Cones',
                'coaching_points': 'Protect ball with body, quick feet, head up after turn, change of pace.',
                'focus_areas': 'Dribbling, Ball Control, 1v1'
            },
            {
                'name': 'Shooting from Distance',
                'category': 'Technical',
                'sub_category': 'Shooting',
                'description': 'Players practice shooting from outside the box. Focus on technique, power, and accuracy from 18-25 yards.',
                'skill_level': 'Advanced',
                'min_players': 6,
                'max_players': 16,
                'duration_minutes': 20,
                'recommended_age_groups': 'U13, U14, U15, U16',
                'equipment_needed': 'Balls, Goals, Cones',
                'coaching_points': 'Plant foot beside ball, strike through center, follow through, keep head down, lock ankle.',
                'focus_areas': 'Shooting, Finishing'
            },
            {
                'name': 'First Touch Control',
                'category': 'Technical',
                'sub_category': 'Receiving',
                'description': 'Players work on controlling balls from different angles and heights. Partner passing with varied service.',
                'skill_level': 'Beginner',
                'min_players': 4,
                'max_players': 20,
                'duration_minutes': 12,
                'recommended_age_groups': 'U9, U10, U11, U12',
                'equipment_needed': 'Balls',
                'coaching_points': 'Cushion the ball, touch away from pressure, use different surfaces (inside, outside, thigh, chest).',
                'focus_areas': 'Ball Control, Receiving'
            },
            {
                'name': 'Crossing and Finishing',
                'category': 'Technical',
                'sub_category': 'Crossing',
                'description': 'Wide players deliver crosses while attackers work on timing runs and finishing. Rotate positions.',
                'skill_level': 'Intermediate',
                'min_players': 8,
                'max_players': 16,
                'duration_minutes': 20,
                'recommended_age_groups': 'U11, U12, U13, U14, U15, U16',
                'equipment_needed': 'Balls, Goals, Cones',
                'coaching_points': 'Cross quality and placement, attacking runs (near post, far post, edge of box), finish first time when possible.',
                'focus_areas': 'Crossing, Finishing, Movement'
            }
        ]

        # Tactical Drills
        tactical_drills = [
            {
                'name': 'Pressing Triggers',
                'category': 'Tactical',
                'sub_category': 'Defending',
                'description': 'Team works on recognizing when to press as a unit. Triggers include bad touch, back pass, or player facing own goal.',
                'skill_level': 'Advanced',
                'min_players': 11,
                'max_players': 22,
                'duration_minutes': 25,
                'recommended_age_groups': 'U13, U14, U15, U16',
                'equipment_needed': 'Balls, Cones, Pinnies',
                'coaching_points': 'Recognition of triggers, press together, cut passing lanes, force turnovers in dangerous areas.',
                'focus_areas': 'Defending, Team Shape, Pressing'
            },
            {
                'name': 'Wide Play and Overlaps',
                'category': 'Tactical',
                'sub_category': 'Attacking',
                'description': 'Fullbacks and wingers work on overlapping runs to create 2v1 situations on the flanks.',
                'skill_level': 'Intermediate',
                'min_players': 8,
                'max_players': 16,
                'duration_minutes': 20,
                'recommended_age_groups': 'U11, U12, U13, U14, U15, U16',
                'equipment_needed': 'Balls, Cones, Goals',
                'coaching_points': 'Timing of overlap, communication, when to pass and when to keep ball, recovery runs.',
                'focus_areas': 'Attacking, Width, Support'
            },
            {
                'name': 'Transition: Defense to Attack',
                'category': 'Tactical',
                'sub_category': 'Transition',
                'description': 'Practice winning ball and quickly transitioning to attack. Focus on speed of play and decision making.',
                'skill_level': 'Advanced',
                'min_players': 12,
                'max_players': 22,
                'duration_minutes': 25,
                'recommended_age_groups': 'U13, U14, U15, U16',
                'equipment_needed': 'Balls, Cones, Goals, Pinnies',
                'coaching_points': 'Win ball and look forward first, quick passes, run at defenders, exploit space quickly.',
                'focus_areas': 'Transition, Speed of Play, Counter Attack'
            },
            {
                'name': 'Creating Space in Final Third',
                'category': 'Tactical',
                'sub_category': 'Attacking',
                'description': 'Attacking players work on movement to create space: checking away, pulling wide, diagonal runs.',
                'skill_level': 'Intermediate',
                'min_players': 10,
                'max_players': 18,
                'duration_minutes': 20,
                'recommended_age_groups': 'U12, U13, U14, U15, U16',
                'equipment_needed': 'Balls, Cones, Goals',
                'coaching_points': 'Movement off ball, timing of runs, communication, recognize when to check vs when to run in behind.',
                'focus_areas': 'Movement, Attacking, Support'
            },
            {
                'name': 'Defensive Shape and Cover',
                'category': 'Tactical',
                'sub_category': 'Defending',
                'description': 'Defenders practice maintaining shape, cover and balance. Work on sliding across and compressing space.',
                'skill_level': 'Intermediate',
                'min_players': 10,
                'max_players': 18,
                'duration_minutes': 20,
                'recommended_age_groups': 'U11, U12, U13, U14, U15, U16',
                'equipment_needed': 'Balls, Cones, Pinnies',
                'coaching_points': 'Maintain defensive shape, cover teammates, communicate, squeeze space together.',
                'focus_areas': 'Defending, Team Shape, Communication'
            }
        ]

        # Physical/Fitness Drills
        physical_drills = [
            {
                'name': 'Speed Ladder Footwork',
                'category': 'Physical',
                'sub_category': 'Agility',
                'description': 'Various footwork patterns through speed ladder: one foot, two feet, in-out, lateral, etc.',
                'skill_level': 'Beginner',
                'min_players': 4,
                'max_players': 20,
                'duration_minutes': 10,
                'recommended_age_groups': 'U9, U10, U11, U12, U13, U14, U15, U16',
                'equipment_needed': 'Speed Ladders',
                'coaching_points': 'Quick feet, stay on toes, arms pumping, focus on coordination.',
                'focus_areas': 'Agility, Coordination, Footwork'
            },
            {
                'name': 'SAQ (Speed, Agility, Quickness)',
                'category': 'Physical',
                'sub_category': 'Speed',
                'description': 'Cone drills focusing on acceleration, deceleration, and change of direction at game speed.',
                'skill_level': 'Intermediate',
                'min_players': 6,
                'max_players': 20,
                'duration_minutes': 15,
                'recommended_age_groups': 'U10, U11, U12, U13, U14, U15, U16',
                'equipment_needed': 'Cones',
                'coaching_points': 'Explosive starts, low center of gravity on turns, fast feet, push off outside foot.',
                'focus_areas': 'Speed, Agility, Explosiveness'
            },
            {
                'name': 'Endurance Running with Ball',
                'category': 'Physical',
                'sub_category': 'Endurance',
                'description': 'Players dribble continuously around marked area for timed intervals. Mix of speeds.',
                'skill_level': 'Intermediate',
                'min_players': 8,
                'max_players': 24,
                'duration_minutes': 12,
                'recommended_age_groups': 'U11, U12, U13, U14, U15, U16',
                'equipment_needed': 'Balls, Cones',
                'coaching_points': 'Maintain ball control while fatigued, head up, change of pace, work rate.',
                'focus_areas': 'Endurance, Ball Control, Work Rate'
            }
        ]

        # Fun/Game Drills
        fun_drills = [
            {
                'name': 'World Cup Tournament',
                'category': 'Fun',
                'sub_category': 'Competition',
                'description': 'Mini tournament with teams representing countries. Round-robin or knockout format with short games.',
                'skill_level': 'Beginner',
                'min_players': 12,
                'max_players': 24,
                'duration_minutes': 30,
                'recommended_age_groups': 'U9, U10, U11, U12, U13, U14',
                'equipment_needed': 'Balls, Goals, Cones, Pinnies',
                'coaching_points': 'Game application, teamwork, competitive spirit, decision making under pressure.',
                'focus_areas': 'Game Application, Competition, Teamwork'
            },
            {
                'name': 'King of the Ring',
                'category': 'Fun',
                'sub_category': '1v1',
                'description': 'Players compete 1v1 in a circle. Winner stays on, loser rotates out. First to score wins.',
                'skill_level': 'Beginner',
                'min_players': 6,
                'max_players': 16,
                'duration_minutes': 15,
                'recommended_age_groups': 'U9, U10, U11, U12, U13, U14',
                'equipment_needed': 'Balls, Cones',
                'coaching_points': 'Creativity, take players on, shield ball, quick finishing.',
                'focus_areas': '1v1, Dribbling, Competition'
            },
            {
                'name': 'Musical Balls',
                'category': 'Fun',
                'sub_category': 'Warm-up',
                'description': 'Players dribble around area. When coach calls "freeze", players must quickly find and control a ball.',
                'skill_level': 'Beginner',
                'min_players': 8,
                'max_players': 20,
                'duration_minutes': 10,
                'recommended_age_groups': 'U9, U10, U11, U12',
                'equipment_needed': 'Balls, Cones',
                'coaching_points': 'Awareness, quick reactions, ball control, scanning.',
                'focus_areas': 'Awareness, Ball Control, Fun'
            },
            {
                'name': 'Relay Races with Ball',
                'category': 'Fun',
                'sub_category': 'Competition',
                'description': 'Teams compete in relay races with various dribbling challenges and skills required.',
                'skill_level': 'Beginner',
                'min_players': 8,
                'max_players': 24,
                'duration_minutes': 12,
                'recommended_age_groups': 'U9, U10, U11, U12',
                'equipment_needed': 'Balls, Cones',
                'coaching_points': 'Speed with ball, control, teamwork, pressure performance.',
                'focus_areas': 'Dribbling, Speed, Teamwork'
            }
        ]

        # Combine all drills
        all_new_drills = (
            technical_drills +
            tactical_drills +
            physical_drills +
            fun_drills
        )

        # Add drills to database
        added_count = 0
        skipped_count = 0

        for drill_data in all_new_drills:
            # Check if drill already exists
            existing = Drill.query.filter_by(name=drill_data['name']).first()
            if existing:
                print(f"Skipped (already exists): {drill_data['name']}")
                skipped_count += 1
                continue

            drill = Drill(**drill_data)
            db.session.add(drill)
            added_count += 1
            print(f"Added: {drill_data['name']} - {drill_data['category']}")

        db.session.commit()

        print(f"\n✅ Successfully added {added_count} new drills!")
        print(f"⏭️  Skipped {skipped_count} drills (already exist)")
        print(f"📊 Total drills in database: {Drill.query.count()}")

if __name__ == '__main__':
    add_more_drills()
