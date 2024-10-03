import os
import time

repo_path = "/path/to/your/repository"

while True:
    
    os.chdir(repo_path)

    os.system("git pull")

    time.sleep(60)
