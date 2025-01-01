# Ewaste 1.0, copyright 2025 webbrowser11
import os
import sys
import shutil 
import time

FolderPath = input("Full Path to the Ewaste folder, i.e. (C:/Users/Username/path/to/Ewaste/): ")

Contents = os.listdir(FolderPath)

DelConfirm = input(f"You are about to remove these files: {Contents} Are you sure [Y/N]: ")

if DelConfirm == "y":
    shutil.rmtree(FolderPath)
    print("Deleted your Ewaste. Exiting soon please do not close.")
    time.sleep(3)
    sys.exit()
else:
    print("Okay. Exiting soon please do not close.")
    time.sleep(3)
    sys.exit()