# Setup Guide - Soccer Practice Planner

## Quick Start

Follow these steps to get the application running on your machine.

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

### Step-by-Step Installation

#### 1. Verify Python Installation

```bash
python --version
# or
python3 --version
```

You should see Python 3.8 or higher.

#### 2. Navigate to Project Directory

```bash
cd /Users/omard/Documents/GitHub/pythonteachingcode/IDK-my-project-OD
```

#### 3. Create Virtual Environment

```bash
python -m venv venv
```

This creates an isolated Python environment for the project.

#### 4. Activate Virtual Environment

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

You should see `(venv)` appear at the beginning of your terminal prompt.

#### 5. Install Required Packages

```bash
pip install -r requirements.txt
```

This installs Flask, SQLAlchemy, and other dependencies.

#### 6. Run the Application

```bash
python run.py
```

You should see output like:
```
 * Running on http://0.0.0.0:5000
 * Debug mode: on
```

#### 7. Open in Browser

Open your web browser and go to:
```
http://localhost:5000
```

You should see the Soccer Practice Planner welcome screen!

## Testing the Application

### Creating Your First Team

1. Click "Create New Team" button
2. Fill in the form:
   - Team Name: "Test Team"
   - Age Group: Select "U12"
   - Skill Level: Select "Intermediate"
   - Number of Players: Enter "14"
   - Check some focus areas (e.g., Passing, Shooting)
   - Add notes if desired
3. Click "Create Team"
4. You'll be redirected to the team dashboard

### Viewing Teams

- Click "View My Teams" to see all created teams
- Click on a team card to view its dashboard

## Switching Between Interface Versions

### Currently Active: Version 1 (Clean & Professional)

To preview **Version 2 (Modern & Colorful)**:

1. **Temporary Test** (doesn't save changes):
   - Open `app/templates/welcome.html`
   - Change the first line from `{% extends "base.html" %}` to `{% extends "base-v2.html" %}`
   - Change the CSS link in base-v2.html if needed
   - Refresh browser (you may need to hard refresh: Cmd+Shift+R on Mac, Ctrl+Shift+R on Windows)

2. **Permanent Switch**:
   - Edit `app/routes.py`
   - Find: `return render_template('welcome.html')`
   - Change to: `return render_template('welcome-v2.html')`
   - Update other template files similarly

## Troubleshooting

### Port Already in Use

If you see "Address already in use" error:

1. Find the process using port 5000:
   ```bash
   lsof -i :5000
   ```

2. Kill the process:
   ```bash
   kill -9 <PID>
   ```

3. Or change the port in `run.py`:
   ```python
   app.run(debug=True, host='0.0.0.0', port=5001)
   ```

### Module Not Found Error

Make sure your virtual environment is activated:
```bash
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows
```

Then reinstall requirements:
```bash
pip install -r requirements.txt
```

### Database Issues

If you encounter database errors, delete the database and restart:
```bash
rm soccer_planner.db
python run.py
```

The database will be recreated automatically.

### CSS Not Loading

Try a hard refresh in your browser:
- **Mac**: Cmd + Shift + R
- **Windows/Linux**: Ctrl + Shift + R

## Stopping the Application

Press `Ctrl + C` in the terminal where the app is running.

## Deactivating Virtual Environment

When you're done working on the project:
```bash
deactivate
```

## Next Steps

Once the application is running:

1. ✅ Create a few test teams with different configurations
2. ✅ Test both interface versions to decide which you prefer
3. ✅ Make your first Git commit
4. 🔄 Start adding drill catalog features
5. 🔄 Implement practice plan generator
6. 🔄 Add visual diagram generation

## Git Workflow

### Making Your First Commit

```bash
# Check status
git status

# Add all files
git add .

# Create commit
git commit -m "feat: Initial project setup with team management"

# Push to GitHub
git push origin main
```

### Recommended Commit Messages

1. "feat: Initial project setup with Flask and database models"
2. "feat: Add team creation form and input validation"
3. "feat: Implement team dashboard and list views"
4. "style: Add Version 1 (Clean & Professional) interface"
5. "style: Add Version 2 (Modern & Colorful) interface"
6. "docs: Add comprehensive README and setup guide"

## Need Help?

- Check the main [README.md](README.md) for project overview
- Review Flask documentation: https://flask.palletsprojects.com/
- Review Bootstrap documentation: https://getbootstrap.com/docs/

Happy Coaching! ⚽
