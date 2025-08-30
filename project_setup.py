import os

project_name = "10minKivyGameWithChatGPT"

folders = [
    project_name,
    os.path.join(project_name, "entities")
]

files = {
    os.path.join(project_name, "main.py"): "# Main entry point\n",
    os.path.join(project_name, "game.py"): "# Game class\n",
    os.path.join(project_name, "config.py"): "# Configuration constants\n",
    os.path.join(project_name, "hud.py"): "# HUD class\n",
    os.path.join(project_name, "entities", "__init__.py"): "",
    os.path.join(project_name, "entities", "entity.py"): "# Base Entity class\n",
    os.path.join(project_name, "entities", "player.py"): "# Player class\n",
    os.path.join(project_name, "entities", "enemy.py"): "# Enemy class\n",
    os.path.join(project_name, "entities", "platform.py"): "# Platform class\n",
    os.path.join(project_name, "entities", "collectible.py"): "# Collectible class\n",
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Created folder: {folder}")

# Create files
for path, content in files.items():
    if not os.path.exists(path):
        with open(path, "w") as f:
            f.write(content)
        print(f"Created file: {path}")
    else:
        print(f"File already exists: {path}")

print("\nProject architecture for 10minKivyGameWithChatGPT created successfully!")
