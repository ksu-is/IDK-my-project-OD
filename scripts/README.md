# Setup Scripts

This folder contains one-time setup scripts for populating the database with initial data.

## Scripts

### Core Setup Scripts
- **`populate_improved_templates.py`** - Creates 7 session templates (Academy & Select levels)
  - Run this FIRST after setting up database
  - Creates properly structured 90-minute sessions with 4 drills each

- **`add_scrimmage_drills.py`** - Adds proper game/scrimmage drills
  - 7v7, 9v9, 11v11 full-field scrimmages
  - Small-sided games (4v4, 6v6, 8v8)

- **`add_more_drills.py`** - Adds comprehensive drill catalog
  - 15 additional drills covering Technical, Tactical, Physical, and Fun categories
  - Run after populate_improved_templates.py

### Legacy/Optional Scripts
- **`populate_drills.py`** - Original drill population script
- **`populate_session_templates.py`** - Original template script
- **`generate_diagrams.py`** - Diagram generation utility

## Usage

### Fresh Database Setup
```bash
# 1. Create database tables
python run.py  # Will create tables on first run

# 2. Populate with templates and base drills
python scripts/populate_improved_templates.py

# 3. Add scrimmage drills
python scripts/add_scrimmage_drills.py

# 4. Add more drills
python scripts/add_more_drills.py
```

### Reset Database
```bash
# Delete instance/soccer_planner.db
# Then follow Fresh Database Setup steps
```

## Notes
- Scripts check for duplicates before adding data
- Run from project root directory
- Requires virtual environment activated
