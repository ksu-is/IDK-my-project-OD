"""Generate soccer field diagrams for drills using matplotlib"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle, Rectangle, Arc, FancyArrowPatch
import os

def create_field(ax, field_type='half'):
    """
    Create a soccer field background
    field_type: 'full', 'half', or 'small' (for small-sided games)
    """
    ax.set_aspect('equal')
    ax.axis('off')

    if field_type == 'full':
        # Full field dimensions (simplified)
        field = Rectangle((0, 0), 100, 60, linewidth=2, edgecolor='white', facecolor='#2d7a3e', zorder=0)
        ax.add_patch(field)

        # Center line
        ax.plot([50, 50], [0, 60], 'white', linewidth=2)

        # Center circle
        center_circle = Circle((50, 30), 9.15, linewidth=2, edgecolor='white', facecolor='none')
        ax.add_patch(center_circle)

        # Goals
        ax.add_patch(Rectangle((0, 24), -2, 12, linewidth=2, edgecolor='white', facecolor='none'))
        ax.add_patch(Rectangle((100, 24), 2, 12, linewidth=2, edgecolor='white', facecolor='none'))

        # Penalty areas
        ax.add_patch(Rectangle((0, 18), 16.5, 24, linewidth=2, edgecolor='white', facecolor='none'))
        ax.add_patch(Rectangle((100, 18), -16.5, 24, linewidth=2, edgecolor='white', facecolor='none'))

        ax.set_xlim(-5, 105)
        ax.set_ylim(-5, 65)

    elif field_type == 'half':
        # Half field
        field = Rectangle((0, 0), 50, 60, linewidth=2, edgecolor='white', facecolor='#2d7a3e', zorder=0)
        ax.add_patch(field)

        # Goal
        ax.add_patch(Rectangle((0, 24), -2, 12, linewidth=2, edgecolor='white', facecolor='none'))

        # Penalty area
        ax.add_patch(Rectangle((0, 18), 16.5, 24, linewidth=2, edgecolor='white', facecolor='none'))

        # Center line
        ax.plot([50, 50], [0, 60], 'white', linewidth=2, linestyle='--')

        ax.set_xlim(-5, 55)
        ax.set_ylim(-5, 65)

    else:  # small grid
        # Small training grid
        field = Rectangle((0, 0), 30, 30, linewidth=2, edgecolor='white', facecolor='#2d7a3e', zorder=0)
        ax.add_patch(field)

        ax.set_xlim(-2, 32)
        ax.set_ylim(-2, 32)

def add_player(ax, x, y, color='#FFD23F', label='', size=800):
    """Add a player marker to the field"""
    ax.scatter(x, y, s=size, c=color, edgecolors='white', linewidths=2, zorder=5)
    if label:
        ax.text(x, y, label, ha='center', va='center', fontsize=10, fontweight='bold', color='black', zorder=6)

def add_cone(ax, x, y, color='#FF7F50'):
    """Add a cone marker"""
    cone = Circle((x, y), 0.5, color=color, edgecolor='white', linewidth=1, zorder=4)
    ax.add_patch(cone)

def add_ball(ax, x, y):
    """Add a ball marker"""
    ball = Circle((x, y), 0.8, color='white', edgecolor='black', linewidth=2, zorder=5)
    ax.add_patch(ball)
    # Add pattern to make it look like a soccer ball
    ax.plot([x-0.4, x+0.4], [y, y], 'black', linewidth=1)
    ax.plot([x, x], [y-0.4, y+0.4], 'black', linewidth=1)

def add_arrow(ax, x1, y1, x2, y2, color='#FFD23F', style='solid', label=''):
    """Add an arrow showing movement or pass"""
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                           arrowstyle='->', mutation_scale=25,
                           linewidth=3, edgecolor=color, facecolor=color,
                           linestyle=style, zorder=3)
    ax.add_patch(arrow)

    if label:
        mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
        ax.text(mid_x, mid_y + 1, label, ha='center', fontsize=9,
               bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

def add_goal(ax, x, y, width=8, color='white'):
    """Add a small goal marker"""
    goal = Rectangle((x - width/2, y - 1), width, 2, linewidth=2,
                    edgecolor=color, facecolor='none', zorder=4)
    ax.add_patch(goal)

def generate_passing_square_diagram():
    """Generate diagram for Passing Square drill"""
    fig, ax = plt.subplots(figsize=(8, 8), facecolor='#2C3E50')
    create_field(ax, 'small')

    # Four cones at corners
    positions = [(5, 5), (25, 5), (25, 25), (5, 25)]
    for i, (x, y) in enumerate(positions):
        add_cone(ax, x, y)

    # Players at each corner
    add_player(ax, 5, 5, label='1')
    add_player(ax, 25, 5, label='2')
    add_player(ax, 25, 25, label='3')
    add_player(ax, 5, 25, label='4')

    # Ball at player 1
    add_ball(ax, 6, 5)

    # Passing pattern arrows
    add_arrow(ax, 5, 5, 25, 5, color='#FFD23F', label='Pass')
    add_arrow(ax, 25, 5, 25, 25, color='#4682B4')
    add_arrow(ax, 25, 25, 5, 25, color='#FFD23F')
    add_arrow(ax, 5, 25, 5, 5, color='#4682B4')

    plt.title('Passing Square Drill', fontsize=16, fontweight='bold', color='white', pad=20)

    return fig

def generate_dribbling_race_diagram():
    """Generate diagram for 1v1 Dribbling Race"""
    fig, ax = plt.subplots(figsize=(10, 6), facecolor='#2C3E50')
    create_field(ax, 'small')

    # Create lanes
    for i in range(5):
        x = 5 + i * 5
        # Start line
        add_cone(ax, x, 5)
        # Finish line
        add_cone(ax, x, 25)

        # Lane lines
        ax.plot([x, x], [5, 25], 'white', linewidth=1, linestyle='--', alpha=0.5)

    # Players at start
    add_player(ax, 7, 5, label='1')
    add_player(ax, 12, 5, label='2')
    add_player(ax, 17, 5, label='3')

    # Balls
    add_ball(ax, 7, 6)
    add_ball(ax, 12, 6)
    add_ball(ax, 17, 6)

    # Dribbling arrows
    add_arrow(ax, 7, 7, 7, 23, color='#FFD23F')
    add_arrow(ax, 12, 7, 12, 23, color='#4682B4')
    add_arrow(ax, 17, 7, 17, 23, color='#FF7F50')

    plt.title('1v1 Dribbling Race', fontsize=16, fontweight='bold', color='white', pad=20)

    return fig

def generate_shooting_diagram():
    """Generate diagram for Shooting from Distance"""
    fig, ax = plt.subplots(figsize=(10, 8), facecolor='#2C3E50')
    create_field(ax, 'half')

    # Goal
    ax.add_patch(Rectangle((-2, 24), 2, 12, linewidth=3, edgecolor='white', facecolor='none'))

    # Shooting positions
    positions = [(20, 15), (20, 30), (20, 45), (25, 22), (25, 38)]

    for i, (x, y) in enumerate(positions):
        add_cone(ax, x, y)
        add_player(ax, x + 3, y, label=str(i+1))
        add_ball(ax, x + 2, y)
        # Shooting arrow to goal
        add_arrow(ax, x + 3, y, 0, 30, color='#FFD23F')

    plt.title('Shooting from Distance', fontsize=16, fontweight='bold', color='white', pad=20)

    return fig

def generate_possession_diagram():
    """Generate diagram for 4v4+2 Possession"""
    fig, ax = plt.subplots(figsize=(8, 8), facecolor='#2C3E50')
    create_field(ax, 'small')

    # Team 1 (Yellow)
    team1_positions = [(8, 8), (22, 8), (8, 22), (22, 22)]
    for i, (x, y) in enumerate(team1_positions):
        add_player(ax, x, y, color='#FFD23F', label=str(i+1))

    # Team 2 (Blue)
    team2_positions = [(10, 15), (20, 15), (15, 10), (15, 20)]
    for i, (x, y) in enumerate(team2_positions):
        add_player(ax, x, y, color='#4682B4', label=str(i+1))

    # Neutral players (Orange)
    add_player(ax, 15, 5, color='#FF7F50', label='N1')
    add_player(ax, 15, 25, color='#FF7F50', label='N2')

    # Ball
    add_ball(ax, 8, 8)

    # Passing options
    add_arrow(ax, 8, 8, 22, 22, color='#FFD23F', style='dashed')
    add_arrow(ax, 8, 8, 15, 5, color='#FF7F50', style='dashed')

    plt.title('4v4+2 Possession', fontsize=16, fontweight='bold', color='white', pad=20)

    return fig

def generate_defending_shape_diagram():
    """Generate diagram for 3v2 Defending Shape"""
    fig, ax = plt.subplots(figsize=(10, 8), facecolor='#2C3E50')
    create_field(ax, 'half')

    # Small goals
    add_goal(ax, 0, 30)

    # Attackers (Yellow)
    add_player(ax, 35, 20, color='#FFD23F', label='A1')
    add_player(ax, 35, 30, color='#FFD23F', label='A2')
    add_player(ax, 35, 40, color='#FFD23F', label='A3')

    # Defenders (Blue)
    add_player(ax, 20, 25, color='#4682B4', label='D1')
    add_player(ax, 15, 35, color='#4682B4', label='D2')

    # Ball with attacker
    add_ball(ax, 36, 30)

    # Defending arrows showing pressure and cover
    add_arrow(ax, 20, 25, 35, 30, color='#DC143C', label='Pressure')
    add_arrow(ax, 15, 35, 20, 30, color='#4682B4', style='dashed', label='Cover')

    plt.title('3v2 Defending Shape', fontsize=16, fontweight='bold', color='white', pad=20)

    return fig

def generate_agility_ladder_diagram():
    """Generate diagram for Agility Ladder"""
    fig, ax = plt.subplots(figsize=(10, 6), facecolor='#2C3E50')

    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_xlim(0, 30)
    ax.set_ylim(0, 15)

    # Background
    field = Rectangle((0, 0), 30, 15, facecolor='#2d7a3e', zorder=0)
    ax.add_patch(field)

    # Agility ladder
    ladder_start_x = 5
    ladder_y = 7.5
    num_rungs = 10
    rung_spacing = 1.5

    # Ladder sides
    ax.plot([ladder_start_x, ladder_start_x + num_rungs * rung_spacing],
           [ladder_y - 1, ladder_y - 1], 'white', linewidth=3)
    ax.plot([ladder_start_x, ladder_start_x + num_rungs * rung_spacing],
           [ladder_y + 1, ladder_y + 1], 'white', linewidth=3)

    # Rungs
    for i in range(num_rungs + 1):
        x = ladder_start_x + i * rung_spacing
        ax.plot([x, x], [ladder_y - 1, ladder_y + 1], 'white', linewidth=2)

    # Player at start
    add_player(ax, ladder_start_x - 2, ladder_y, label='P')

    # Movement arrow
    add_arrow(ax, ladder_start_x - 1, ladder_y, ladder_start_x + num_rungs * rung_spacing + 1, ladder_y, color='#FFD23F')

    # Footprint indicators (simplified)
    for i in range(1, num_rungs):
        x = ladder_start_x + i * rung_spacing + 0.5
        ax.scatter([x, x], [ladder_y - 0.4, ladder_y + 0.4], s=50, c='#FFD23F', marker='o', alpha=0.7)

    plt.title('Agility Ladder Drills', fontsize=16, fontweight='bold', color='white', pad=20)

    return fig

def generate_world_cup_diagram():
    """Generate diagram for World Cup Tournament"""
    fig, ax = plt.subplots(figsize=(10, 8), facecolor='#2C3E50')

    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 50)

    # Background
    field = Rectangle((0, 0), 50, 50, facecolor='#2d7a3e', zorder=0)
    ax.add_patch(field)

    # Field 1 (top left)
    ax.add_patch(Rectangle((2, 27), 21, 21, linewidth=2, edgecolor='white', facecolor='none'))
    add_goal(ax, 2, 37.5, width=6)
    add_goal(ax, 23, 37.5, width=6)
    # Teams
    add_player(ax, 8, 35, color='#FFD23F', label='Y')
    add_player(ax, 17, 35, color='#4682B4', label='B')
    add_ball(ax, 12.5, 37.5)

    # Field 2 (top right)
    ax.add_patch(Rectangle((27, 27), 21, 21, linewidth=2, edgecolor='white', facecolor='none'))
    add_goal(ax, 27, 37.5, width=6)
    add_goal(ax, 48, 37.5, width=6)
    # Teams
    add_player(ax, 33, 35, color='#FF7F50', label='O')
    add_player(ax, 42, 35, color='#556B2F', label='G')
    add_ball(ax, 37.5, 37.5)

    # Field 3 (bottom left)
    ax.add_patch(Rectangle((2, 2), 21, 21, linewidth=2, edgecolor='white', facecolor='none'))
    add_goal(ax, 2, 12.5, width=6)
    add_goal(ax, 23, 12.5, width=6)

    # Field 4 (bottom right)
    ax.add_patch(Rectangle((27, 2), 21, 21, linewidth=2, edgecolor='white', facecolor='none'))
    add_goal(ax, 27, 12.5, width=6)
    add_goal(ax, 48, 12.5, width=6)

    plt.title('World Cup Tournament (4 Fields)', fontsize=16, fontweight='bold', color='white', pad=20)

    return fig

def generate_sharks_minnows_diagram():
    """Generate diagram for Sharks and Minnows"""
    fig, ax = plt.subplots(figsize=(8, 8), facecolor='#2C3E50')
    create_field(ax, 'small')

    # Safe zones
    ax.add_patch(Rectangle((0, 0), 30, 3, linewidth=2, edgecolor='white', facecolor='#4682B4', alpha=0.3))
    ax.add_patch(Rectangle((0, 27), 30, 3, linewidth=2, edgecolor='white', facecolor='#4682B4', alpha=0.3))

    # Minnows at start (with balls)
    minnow_positions = [(5, 2), (10, 2), (15, 2), (20, 2), (25, 2)]
    for x, y in minnow_positions:
        add_player(ax, x, y, color='#FFD23F', label='M')
        add_ball(ax, x, y + 1)

    # Sharks in middle (no balls)
    add_player(ax, 10, 15, color='#DC143C', label='S', size=1000)
    add_player(ax, 20, 15, color='#DC143C', label='S', size=1000)

    # Movement arrows
    add_arrow(ax, 5, 3, 5, 27, color='#FFD23F', style='dashed')
    add_arrow(ax, 15, 3, 15, 27, color='#FFD23F', style='dashed')
    add_arrow(ax, 25, 3, 25, 27, color='#FFD23F', style='dashed')

    plt.title('Sharks and Minnows', fontsize=16, fontweight='bold', color='white', pad=20)

    return fig

def save_drill_diagram(drill_name, drill_id):
    """Generate and save diagram for a specific drill"""
    # Create diagrams directory if it doesn't exist
    static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'diagrams')
    os.makedirs(static_dir, exist_ok=True)

    # Generate appropriate diagram based on drill name
    drill_generators = {
        'Passing Square': generate_passing_square_diagram,
        '1v1 Dribbling Race': generate_dribbling_race_diagram,
        'Shooting from Distance': generate_shooting_diagram,
        '4v4+2 Possession': generate_possession_diagram,
        '3v2 Defending Shape': generate_defending_shape_diagram,
        'Agility Ladder Drills': generate_agility_ladder_diagram,
        'World Cup Tournament': generate_world_cup_diagram,
        'Sharks and Minnows': generate_sharks_minnows_diagram,
    }

    if drill_name in drill_generators:
        fig = drill_generators[drill_name]()

        # Save figure
        filename = f'drill_{drill_id}.png'
        filepath = os.path.join(static_dir, filename)
        fig.savefig(filepath, dpi=150, bbox_inches='tight', facecolor='#2C3E50')
        plt.close(fig)

        return f'diagrams/{filename}'

    return None
