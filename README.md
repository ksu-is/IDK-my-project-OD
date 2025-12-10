# Soccer Practice Planner ⚽

A comprehensive web application for youth soccer coaches to create, manage, and organize practice sessions.

## 📋 Features

### Team Management
- Create and manage multiple teams
- Track age groups (U9-U16), skill levels, and focus areas
- Recommended session durations based on age group

### Drill Catalog
- **30+ professional soccer drills** covering:
  - Technical skills (passing, dribbling, shooting, receiving)
  - Tactical concepts (building out, pressing, transitions)
  - Physical conditioning (speed, agility, endurance)
  - Fun/competitive games
- **Advanced filtering**: Search by name, category, skill level, and age group
- **Visual diagrams** for each drill
- **CSV import** functionality for bulk drill uploads

### Practice Plan Management
- Build custom practice plans from scratch
- Use pre-made templates (7 templates for Academy & Select levels)
- Drag-and-drop drill ordering
- Set custom durations for each drill
- Add session notes and coaching points
- **Edit, duplicate, and delete** practice plans
- **Print-friendly views** for field use

### Session Templates
- **Academy templates** (U9-U12): Technical focus
- **Select templates** (U13+): Tactical focus
- Properly structured 90-minute sessions:
  - Warm-up (10-15 min)
  - Activity 1 (15-20 min)
  - Activity 2 (20-30 min)
  - Scrimmage (30-35 min)

### UI Features
- **Dark mode** support
- Responsive design (mobile-friendly)
- Professional color scheme (Steel Blue & Desert Gold)
- Interactive drill selection with diagrams

## 🛠️ Tech Stack

- **Backend**: Python 3.x, Flask
- **Database**: SQLAlchemy ORM with SQLite
- **Frontend**: Bootstrap 5, JavaScript
- **Icons**: Bootstrap Icons
- **Styling**: Custom CSS with CSS variables

## 📁 Project Structure

```
IDK-my-project-OD/
├── app/
│   ├── __init__.py           # Flask app factory
│   ├── routes.py             # All application routes
│   ├── models/               # Database models
│   │   ├── team.py
│   │   ├── drill.py
│   │   ├── practice_plan.py
│   │   ├── session_template.py
│   │   └── player.py
│   ├── templates/            # Jinja2 templates
│   │   ├── base-v3.html      # Base template
│   │   ├── welcome-v3.html   # Landing page
│   │   ├── drills_catalog.html
│   │   ├── practice_plan_*.html
│   │   └── ...
│   ├── static/
│   │   ├── css/
│   │   │   └── style-v3.css  # Main stylesheet
│   │   └── drill_diagrams/   # SVG diagrams
│   └── utils/
│       └── diagram_generator.py
├── scripts/                  # Setup/population scripts
│   ├── README.md
│   ├── populate_improved_templates.py
│   ├── add_scrimmage_drills.py
│   └── add_more_drills.py
├── instance/
│   └── soccer_planner.db     # SQLite database
├── run.py                    # Application entry point
└── README.md
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   cd IDK-my-project-OD
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask flask-sqlalchemy
   ```

4. **Initialize database**
   ```bash
   python run.py  # Creates tables on first run
   # Press Ctrl+C to stop
   ```

5. **Populate with sample data**
   ```bash
   python scripts/populate_improved_templates.py
   python scripts/add_scrimmage_drills.py
   python scripts/add_more_drills.py
   ```

6. **Run the application**
   ```bash
   python run.py
   ```

7. **Open in browser**
   ```
   http://localhost:5000
   ```

## 📖 Usage

### Creating Your First Team
1. Click "Create New Team" on the homepage
2. Fill in team details (name, age group, skill level, number of players)
3. Select focus areas (e.g., Passing, Shooting, Defending)
4. Submit to create team

### Building a Practice Plan

#### Option 1: Use a Template
1. From team dashboard, click "Start Practice Plan"
2. Choose "Use Template"
3. Select a template matching your team's level
4. Customize drill durations if needed
5. Save your plan

#### Option 2: Build Custom Plan
1. From team dashboard, click "Start Practice Plan"
2. Choose "Build Custom"
3. Search and filter drills by category, skill level, age group
4. Click "Add" to add drills to your session
5. Drag to reorder, set durations
6. Save your plan

### Managing Practice Plans
- **View**: See full details with diagrams and coaching points
- **Edit**: Modify drills, durations, or notes
- **Duplicate**: Create a copy to modify for next session
- **Print**: Generate print-friendly version for field use
- **Delete**: Remove old plans

### Importing Drills
1. Go to "Drill Catalog"
2. Click "Import Drills from CSV"
3. Download the template CSV
4. Fill in drill information
5. Upload the CSV file

## 🗃️ Database Models

### Team
- Name, age group, skill level
- Number of players
- Focus areas
- Additional notes

### Drill
- Name, category, sub-category
- Description, coaching points
- Skill level, player count (min/max)
- Duration, equipment needed
- Recommended age groups
- Diagram URL

### Practice Plan
- Associated team
- Name, duration, notes
- Created date, practice date
- Collection of drills with ordering

### Session Template
- Pre-configured practice sessions
- Name, description
- Total duration
- Target skill level and age groups
- Collection of template drills

## 🎨 Design System

### Color Palette
- **Steel Blue**: `#4682B4` - Primary actions
- **Desert Gold**: `#D4A574` - Accents
- **Olive Green**: `#6B8E23` - Success states
- **Coral Orange**: `#FF6F61` - Highlights
- **Dark Slate**: `#2C3E50` - Text/backgrounds

### Dark Mode
Toggle in navigation bar for reduced eye strain during planning sessions.

## 🐛 Known Issues & Fixes

See [CODE_ISSUES_AND_FIXES.html](CODE_ISSUES_AND_FIXES.html) for detailed documentation of issues encountered and solutions implemented.

## 🔮 Future Enhancements

- [ ] Complete UI overhaul with modern design system
- [ ] Player attendance tracking
- [ ] Season planning calendar
- [ ] Drill favorites/bookmarking
- [ ] Export plans to PDF
- [ ] Mobile app version
- [ ] Multi-language support
- [ ] Video integration for drill demonstrations

## 👤 Author

Professional youth soccer coach specializing in U9-U16 age groups

## 📝 License

Educational project for Python programming course

## 🙏 Acknowledgments

- Built with guidance from Claude AI
- Drill library based on professional youth soccer coaching practices
- Inspired by real-world coaching needs for U9-U16 teams
