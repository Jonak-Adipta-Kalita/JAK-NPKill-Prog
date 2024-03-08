import os, shutil, sys

directory = sys.argv[1] if len(sys.argv) > 1 else str(input("Path to Directory: ")).strip("\"")
leave = []

if os.path.exists("leave.txt"):
    with open("leave.txt", "r") as f:
        for i in f.read().splitlines():
            leave.append(i)

def check_for_node_modules(project_dir: str) -> bool:
    folders = []
    for root, dirs, _ in os.walk(project_dir):
        root += "\\node_modules"
        if "node_modules" in dirs and root.count("\\node_modules") == 1:
            folders.append(root)

    return folders

print()
for project in os.listdir(directory):
    project_dir = f"{directory}\\{project}" 
    if project in leave or not os.path.isdir(project_dir):
        continue

    folders = check_for_node_modules(project_dir)
    if not folders: continue

    try:
        for folder in folders:
            shutil.rmtree(folder)
        print(f"\"{project_dir}\" NPKilled!!")
    except Exception as err:
        print(f"(Skipping) Issue in {project}: {err}")
