import configparser
import os
from pathlib import Path

class ReadConfig:
    def __init__(self):
        self.project_root = Path(__file__).parent.parent
        self.config_path = os.path.join(self.project_root, "config", "config,ini")
        self.config = configparser.ConfigParser()
        self._load_config()

    def