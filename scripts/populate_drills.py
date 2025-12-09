"""Script to populate the database with sample soccer drills"""
from app import create_app, db
from app.models import Drill

def populate_drills():
    """Add sample drills to the database"""
    app = create_app()

    with app.app_context():
        # Clear existing drills
        Drill.query.delete()

        drills = [
            # Technical Drills
            Drill(
                name="Passing Square",
                category="Technical",
                sub_category="Passing",
                description="Players work in groups of 4-6 to practice passing accuracy and receiving skills in a square formation.",
                equipment_needed="4 cones, 1 ball per group",
                min_players=4,
                max_players=6,
                recommended_age_groups="U9,U10,U12,U14,U16",
                skill_level="Beginner",
                duration_minutes=15,
                focus_areas="Passing accuracy, first touch, communication",
                setup_instructions="Set up a 10x10 yard square with cones at each corner. Players stand at each cone with one ball.",
                coaching_points="- Use the inside of the foot\n- Look up before passing\n- Move to receive after passing\n- Communicate with teammates",
                variations="- Add a defender in the middle\n- Use only weak foot\n- Limit touches to one or two\n- Increase square size"
            ),

            Drill(
                name="1v1 Dribbling Race",
                category="Technical",
                sub_category="Dribbling",
                description="Players race with the ball to develop close control dribbling skills and speed with the ball.",
                equipment_needed="Cones for lanes, 1 ball per player",
                min_players=2,
                max_players=16,
                recommended_age_groups="U9,U10,U12",
                skill_level="Beginner",
                duration_minutes=10,
                focus_areas="Close control, dribbling speed, ball manipulation",
                setup_instructions="Create 4-5 dribbling lanes 20 yards long using cones. Players line up in pairs at the start.",
                coaching_points="- Keep ball close to feet\n- Use both feet\n- Look up occasionally\n- Change of pace",
                variations="- Add obstacles to dribble around\n- Only use weak foot\n- Dribble backwards on return"
            ),

            Drill(
                name="Shooting from Distance",
                category="Technical",
                sub_category="Shooting",
                description="Players practice striking the ball with power and accuracy from outside the penalty area.",
                equipment_needed="Goals, multiple balls, cones for positioning",
                min_players=6,
                max_players=16,
                recommended_age_groups="U12,U14,U16",
                skill_level="Intermediate",
                duration_minutes=20,
                focus_areas="Shooting technique, power, accuracy",
                setup_instructions="Set up shooting stations 20-25 yards from goal. Players take turns shooting after receiving a pass.",
                coaching_points="- Plant foot beside ball\n- Strike through the ball\n- Follow through\n- Keep head down on contact",
                variations="- Add a defender to pressure\n- Shoot first time\n- Different angles of approach"
            ),

            # Tactical Drills
            Drill(
                name="4v4+2 Possession",
                category="Tactical",
                sub_category="Possession",
                description="Small-sided game focused on maintaining possession with numerical advantage using neutral players.",
                equipment_needed="Cones for grid, 1 ball, pinnies",
                min_players=10,
                max_players=10,
                recommended_age_groups="U12,U14,U16",
                skill_level="Intermediate",
                duration_minutes=20,
                focus_areas="Possession, support play, transition, decision making",
                setup_instructions="Create a 30x30 yard grid. Two teams of 4 plus 2 neutral players who always play with team in possession.",
                coaching_points="- Create passing triangles\n- Spread out to create space\n- Play quickly\n- Support the ball",
                variations="- Limit touches\n- Add small goals for counter-attacking\n- Make grid smaller or larger"
            ),

            Drill(
                name="3v2 Defending Shape",
                category="Tactical",
                sub_category="Defending",
                description="Defenders work together to maintain proper defensive shape and win the ball against attackers.",
                equipment_needed="Cones, goals, balls, pinnies",
                min_players=5,
                max_players=15,
                recommended_age_groups="U14,U16",
                skill_level="Advanced",
                duration_minutes=15,
                focus_areas="Defensive organization, pressure and cover, communication",
                setup_instructions="Set up a channel to goal. 3 attackers try to score against 2 defenders.",
                coaching_points="- First defender pressures ball\n- Second defender covers\n- Force play to sideline\n- Communicate constantly",
                variations="- Add another defender (3v3)\n- Require defenders to win ball and counter\n- Different starting positions"
            ),

            # Physical Drills
            Drill(
                name="Agility Ladder Drills",
                category="Physical",
                sub_category="Agility",
                description="Players perform various footwork patterns through an agility ladder to improve coordination and quickness.",
                equipment_needed="Agility ladder or cones",
                min_players=4,
                max_players=20,
                recommended_age_groups="U9,U10,U12,U14,U16",
                skill_level="All",
                duration_minutes=10,
                focus_areas="Foot speed, coordination, agility, balance",
                setup_instructions="Lay out agility ladder. Players perform different footwork patterns: two feet in, one foot in, lateral steps, etc.",
                coaching_points="- Stay on toes\n- Quick feet\n- Arms pumping\n- Head up",
                variations="- Add ball after completing ladder\n- Backwards through ladder\n- Different patterns"
            ),

            Drill(
                name="Interval Sprints",
                category="Physical",
                sub_category="Fitness",
                description="High-intensity interval training to build speed and cardiovascular endurance specific to soccer.",
                equipment_needed="Cones for markers",
                min_players=4,
                max_players=20,
                recommended_age_groups="U12,U14,U16",
                skill_level="All",
                duration_minutes=15,
                focus_areas="Speed, endurance, recovery",
                setup_instructions="Mark out 20, 40, and 60 yard distances. Players sprint, recover, and repeat.",
                coaching_points="- Maximum effort on sprints\n- Active recovery (jog back)\n- Proper running form\n- Breathe rhythmically",
                variations="- Add ball to sprints\n- Partner races\n- Combine with technical work"
            ),

            # Fun/Games
            Drill(
                name="World Cup Tournament",
                category="Fun",
                sub_category="Small-Sided Game",
                description="Tournament-style small-sided games where winners stay on. Fast-paced and competitive fun for all ages.",
                equipment_needed="Small goals or cones, balls, pinnies",
                min_players=12,
                max_players=24,
                recommended_age_groups="U9,U10,U12,U14,U16",
                skill_level="All",
                duration_minutes=25,
                focus_areas="Game situations, competitiveness, all soccer skills",
                setup_instructions="Set up 2-4 small fields. Teams of 3-4 players. Winners stay, losers rotate off.",
                coaching_points="- Encourage creative play\n- All touches count\n- Keep score\n- Celebrate goals!",
                variations="- Different team sizes (2v2, 3v3, 4v4)\n- Must score from weak foot\n- Add conditions (2-touch maximum)"
            ),

            Drill(
                name="Sharks and Minnows",
                category="Fun",
                sub_category="Dribbling Game",
                description="Classic dribbling game where players (minnows) dribble across while sharks try to knock their balls out.",
                equipment_needed="1 ball per minnow, cones for boundaries",
                min_players=8,
                max_players=20,
                recommended_age_groups="U9,U10,U12",
                skill_level="All",
                duration_minutes=15,
                focus_areas="Dribbling under pressure, shielding, awareness",
                setup_instructions="Mark 30x30 yard grid. All players start on one side with a ball except 2-3 sharks in the middle.",
                coaching_points="- Keep ball close\n- Use body to shield\n- Change direction quickly\n- Look for space",
                variations="- Last minnow standing wins\n- Sharks must also dribble a ball\n- Make grid smaller as game progresses"
            ),
        ]

        # Add all drills to database
        for drill in drills:
            db.session.add(drill)

        db.session.commit()

        print(f"✓ Successfully added {len(drills)} drills to the database!")

if __name__ == '__main__':
    populate_drills()
