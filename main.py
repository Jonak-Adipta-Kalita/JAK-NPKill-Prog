import os, shutil

directory = str(input("Path to Directory: ")).strip("\"")
leave = []

if os.path.exists("leave.txt"):
    with open("leave.txt", "r") as f:
        for i in f.read().splitlines():
            leave.append(i)

for project in os.listdir(directory):
    if project in leave: continue
    
    # try:
    #     if os.path.isdir(f"Works/{i}") and os.path.isdir(f"Works/{i}/node_modules"):
    #         shutil.rmtree(f"Works/{i}/node_modules")
    # except:
    #     continue
