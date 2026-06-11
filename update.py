import os
import subprocess

print("WELCOME TO LINUX AUTO-UPDATER, PLEASE ALWAYS RUN AS SUDO")
while True:
    if os.getuid() != 0:
        print("SUDO REQUIRED")
        break
    elif os.getuid() == 0:
        subprocess.call("apt update -y && apt upgrade -y", shell=True)