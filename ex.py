import os
import subprocess

# Define folder structure based on your DSA course
folders = [
    "algorithm-analysis",
    "recursion",
    "arrays-and-lists",
    "stacks-and-queues",
    "linked-lists",
    "maps-and-hash-tables",
    "trees",
    "graphs",
    "heaps",
    "binary-search",
    "backtracking",
    "dynamic-programming",
    "assignments",
    "projects",
    "tests",
    "utils"
]

# Create folders and add README.md files
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "README.md"), "w") as f:
        f.write(f"# {folder.replace('-', ' ').title()}\n\nDescription of {folder} module.")

# Initialize Git and push changes
try:
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Added folder structure for DSA course"], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)
    print("✅ Folder structure created and pushed to GitHub successfully!")
except subprocess.CalledProcessError as e:
    print(f"❌ Git error: {e}")
