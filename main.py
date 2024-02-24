import os, shutil

directory = str(input("Path to Directory: ")).strip("\"")
leave = []

if os.path.exists("leave.txt"):
    with open("leave.txt", "r") as f:
        for i in f.read().splitlines():
            leave.append(i)

for project in os.listdir(directory):
    if project in leave: continue
    project_dir = f"{directory}\\{project}" 

    if not os.path.isdir(project_dir) or not os.path.isdir(f"{project_dir}\\node_modules"):
        continue

    try:
        shutil.rmtree(f"{project_dir}\\node_modules")
    except Exception as err:
        print(f"(Skipping) Issue in {project}: {err}")
