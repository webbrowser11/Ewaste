# Ewaste 1.1, copyright 2025 webbrowser11
import os
import sys
import shutil 
import time

FolderPath = input("Full Path to the Ewaste folder, i.e. (C:/Users/Username/path/to/Ewaste/): ")

if "Ewaste" in FolderPath:
    Contents = os.listdir(FolderPath)
    
    DelConfirm = input(f"You are about to remove these files: {Contents} Are you sure [Y/N]: ")
    
    if DelConfirm == "y":
        try:
            shutil.rmtree(FolderPath)
            print("Deleted your Ewaste. Exiting soon please do not close.")
            time.sleep(3)
            sys.exit()
        except Exception as error:
            print(f"A unexpected error occured: {error}")
    else:
        print("Okay. Exiting soon please do not close.")
        time.sleep(3)
        sys.exit()
else:
    print("An error occured. Please make an Ewaste folder with your EWaste in it, and feed this program the path.")
