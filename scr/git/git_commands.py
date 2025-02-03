import subprocess
import os

class GIT:
    def __init__(self, path) -> None:
        self.REPO_PATH = path
        print(self.REPO_PATH)

    def init_repo(self) -> None:
        if not os.path.exists(os.path.join(self.REPO_PATH, ".git")):
            result = subprocess.run(["git", "init"], cwd=self.REPO_PATH)
            return result.stdout, result.stderr
        
    def add(self) -> None:
        subprocess.run(["git", "add", "."], cwd=self.REPO_PATH)

    def commit(self, msg) -> None:
        result = subprocess.run(["git", "commit", "-m", msg], cwd=self.REPO_PATH, capture_output=True, text=True)
        return result.stdout, result.stderr

    def pull(self) -> None:
        result = subprocess.run(["git", "pull"], cwd=self.REPO_PATH, capture_output=True, text=True)
        return result.stdout, result.stderr

    def push(self) -> None:
        result = subprocess.run(["git", "push"], cwd=self.REPO_PATH, capture_output=True, text=True)
        return result.stdout, result.stderr
    

