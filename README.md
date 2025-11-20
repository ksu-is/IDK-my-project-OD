# Soccer Practice Planner

A web application for professional youth soccer coaches to create customized practice sessions tailored to their team's needs.

## Project Overview

This application helps soccer coaches manage teams (U9-U16) and generate age-appropriate practice plans with visual diagrams. Input team information including age group, skill level, number of players, and training focus areas to receive personalized practice sessions.

## Features

- **Team Management**: Input and store detailed team information
- **Age Groups**: Support for U9, U10, U12, U14, and U16 teams
- **Skill Levels**: Beginner, Intermediate, and Advanced
- **Training Focus Areas**: Passing, Dribbling, Shooting, Defending, Possession, Transitions, Fitness, and Set Pieces
- **Smart Recommendations**: Automatic session duration suggestions based on age
- **Multiple Interface Versions**: Choose between Clean Professional or Modern Colorful designs

## Technology Stack

- **Backend**: Python 3.x with Flask
- **Database**: SQLite with SQLAlchemy
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Visualization**: Matplotlib (for future drill diagrams)

## Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd IDK-my-project-OD
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**:
   ```bash
   python run.py
   ```

6. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

## Interface Versions

This application comes with TWO different interface designs. You can switch between them by modifying the template files.

### Version 1: Clean & Professional
- Blue and green color scheme
- Simple, elegant design
- Professional appearance
- Uses: `base.html`, `welcome.html`, `style.css`

### Version 2: Modern & Colorful (Soccer-themed)
- Vibrant green, orange, and blue colors
- Soccer field-inspired design
- Animated elements
- Gradient backgrounds
- Uses: `base-v2.html`, `welcome-v2.html`, `style-v2.css`

### How to Switch Between Versions

**Currently using Version 1 by default**

To switch to Version 2:
1. Open `app/routes.py`
2. Change template names in render_template() calls:
   - `welcome.html` → `welcome-v2.html`
3. Update template inheritance in other template files to use `base-v2.html`

## Project Structure

```
IDK-my-project-OD/
│
├── app/
│   ├── __init__.py              # Flask app initialization
│   ├── routes.py                # Application routes
│   ├── models/
│   │   ├── __init__.py
│   │   ├── team.py              # Team database model
│   │   └── player.py            # Player database model
│   ├── templates/
│   │   ├── base.html            # Base template (Version 1)
│   │   ├── base-v2.html         # Base template (Version 2)
│   │   ├── welcome.html         # Welcome page (Version 1)
│   │   ├── welcome-v2.html      # Welcome page (Version 2)
│   │   ├── team_form.html       # Team creation form
│   │   ├── teams_list.html      # List all teams
│   │   └── team_dashboard.html  # Individual team dashboard
│   └── static/
│       └── css/
│           ├── style.css        # Styles (Version 1)
│           └── style-v2.css     # Styles (Version 2)
│
├── run.py                       # Application entry point
├── requirements.txt             # Python dependencies
├── README.md                    # This file
└── soccer_planner.db           # SQLite database (auto-generated)
```

## Database Schema

### Team Model
- `id`: Primary key
- `name`: Team name
- `age_group`: U9, U10, U12, U14, or U16
- `skill_level`: Beginner, Intermediate, or Advanced
- `num_players`: Number of players on the team
- `focus_areas`: Comma-separated training focus areas
- `additional_notes`: Special considerations or notes
- `created_at`: Timestamp of creation
- `updated_at`: Timestamp of last update

### Player Model
- `id`: Primary key
- `name`: Player name
- `position`: Forward, Midfielder, Defender, or Goalkeeper
- `skill_level`: Beginner, Intermediate, or Advanced
- `special_needs`: Individual training considerations
- `team_id`: Foreign key to Team

## Recommended Session Durations

The application automatically suggests practice durations based on age:
- **U9**: 60 minutes
- **U10**: 75 minutes
- **U12**: 90 minutes
- **U14**: 90 minutes
- **U16**: 105 minutes

## Future Enhancements

- [ ] Drill catalog with visual diagrams
- [ ] Practice plan generator
- [ ] Session library and saved plans
- [ ] PDF export functionality
- [ ] Player roster management
- [ ] Attendance tracking
- [ ] Mobile app version

## Development Notes

- Built for Application Development class assignment
- Designed to be extended with additional features
- Database uses SQLite for simplicity (can be upgraded to PostgreSQL for production)
- All styling is responsive and mobile-friendly

## Author

Youth Soccer Coach - Professional Level (U9-U16)

## License

MIT License - See LICENSE file for details
