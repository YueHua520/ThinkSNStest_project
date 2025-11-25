import configparser
import os
from pathlib import Path


class ReadConfig:
    def __init__(self):
        self.project_root = Path(__file__).parent.parent
        self.config_path = os.path.join(self.project_root, "config", "config.ini")
        self.config = configparser.ConfigParser()
        self._load_config()

    def _load_config(self):
        """加载配置文件"""
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"配置文件不存在：{self.config_path}")
        self.config.read(self.config_path, encoding="utf-8")

