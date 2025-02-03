import subprocess
import os

class GIT:
    def __init__(self, path: str) -> None:
        self.REPO_PATH = path
        print(self.REPO_PATH)

    def init_repo(self) -> None:
        if not os.path.exists(os.path.join(self.REPO_PATH, ".git")):
            result = subprocess.run(["git", "init"], cwd=self.REPO_PATH, capture_output=True, text=True)
            return result.stdout, result.stderr

    def add(self) -> None:
        subprocess.run(["git", "add", "."], cwd=self.REPO_PATH)

    def commit(self, msg: str) -> None:
        result = subprocess.run(["git", "commit", "-m", msg], cwd=self.REPO_PATH, capture_output=True, text=True)
        return result.stdout, result.stderr

    def pull(self, branch: str = "main") -> None:
        result = subprocess.run(["git", "pull", "origin", branch], cwd=self.REPO_PATH, capture_output=True, text=True)
        return result.stdout, result.stderr

    def push(self, branch: str = "main") -> None:
        result = subprocess.run(["git", "push", "-u", "origin", branch], cwd=self.REPO_PATH, capture_output=True, text=True)
        return result.stdout, result.stderr

    def checkout(self, branch: str) -> None:
        result = subprocess.run(["git", "checkout", branch], cwd=self.REPO_PATH, capture_output=True, text=True)
        return result.stdout, result.stderr

    def create_branch(self, branch: str) -> None:
        result = subprocess.run(["git", "checkout", "-b", branch], cwd=self.REPO_PATH, capture_output=True, text=True)
        return result.stdout, result.stderr

    def status(self) -> str:
        result = subprocess.run(["git", "status"], cwd=self.REPO_PATH, capture_output=True, text=True)
        return result.stdout

    def log(self, n: int = 5) -> str:
        result = subprocess.run(["git", "log", f"-{n}"], cwd=self.REPO_PATH, capture_output=True, text=True)
        return result.stdout
