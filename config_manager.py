import yaml
from typing import Dict

class ConfigManager:
    def __init__(self, path: str):
        self.path: str = path
        self.data: Dict = {}

    def open(self) -> dict:
        """Loads the configuration data from the specified file."""
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                self.data = yaml.safe_load(file) or {}
                return self.data
            
        except FileNotFoundError:
            raise FileNotFoundError(f'File not found at {self.path}. Please check the path.')

    def save(self) -> None:
        """Saves the current configuration data to the specified file."""
        with open(self.path, "w", encoding="utf-8") as file:
            yaml.safe_dump(self.data, file)

            



