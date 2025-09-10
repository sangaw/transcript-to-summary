import json
import os
from typing import Any, Dict

CONFIG_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "config")
LOCAL_SETTINGS_PATH = os.path.join(CONFIG_DIR, "local-settings.json")


def load_local_settings() -> Dict[str, Any]:
    if not os.path.exists(LOCAL_SETTINGS_PATH):
        return {}
    try:
        with open(LOCAL_SETTINGS_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception:
        return {}
