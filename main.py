import os, shutil

directory = str(input("Path to Directory: ")).strip("\"")

for i in os.listdir(directory):
    print(i)
    #if i in leave: continue
    
    #try:
        #if os.path.isdir(f"Works/{i}") and os.path.isdir(f"Works/{i}/node_modules"):
            #shutil.rmtree(f"Works/{i}/node_modules")
            #print(i)
    #except:
        #continue
