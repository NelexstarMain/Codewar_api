import subprocess
import os

REPO_PATH = "/ścieżka/do/repozytorium"

def init_repo():
    if not os.path.exists(os.path.join(REPO_PATH, ".git")):
        subprocess.run(["git", "init"], cwd=REPO_PATH)

def add():
    subprocess.run(["git", "add", "."], cwd=REPO_PATH)

def commit(msg):
    result = subprocess.run(["git", "commit", "-m", msg], cwd=REPO_PATH, capture_output=True, text=True)
    return result.stdout, result.stderr

def pull():
    result = subprocess.run(["git", "pull"], cwd=REPO_PATH, capture_output=True, text=True)
    return result.stdout, result.stderr

def push():
    result = subprocess.run(["git", "push"], cwd=REPO_PATH, capture_output=True, text=True)
    return result.stdout, result.stderr

