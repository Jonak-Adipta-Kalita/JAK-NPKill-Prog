import os, shutil, sys

directory = sys.argv[1] if len(sys.argv) > 1 else str(input("Path to Directory: ")).strip("\"")
leave = []

if os.path.exists("leave.txt"):
    with open("leave.txt", "r") as f:
        for i in f.read().splitlines():
            leave.append(i)

def check_for_node_modules(project_dir: str) -> bool:
     for root, dirs, _ in os.walk(project_dir):
         return 'node_modules' in dirs, root

for project in os.listdir(directory):
    project_dir = f"{directory}\\{project}" 
    if project in leave or not os.path.isdir(project_dir):
        continue

    exists_in_project, project_dir = check_for_node_modules(project_dir)

    if not exists_in_project: 
        continue

    try:
        shutil.rmtree(f"{project_dir}\\node_modules")
        print(f"{project_dir} NPKilled!!")
    except Exception as err:
        print(f"(Skipping) Issue in {project}: {err}")
