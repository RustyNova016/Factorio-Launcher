import json
import tkinter as tk
import os
from pathlib import Path
from tkinter import filedialog as fd

CODE_PATH = Path().absolute()

SETTINGS_PATH = Path.joinpath(Path(os.environ['USERPROFILE']),"AppData\\Roaming\\Factorio\\launcher\\settings.txt")
SETTINGS_DICT = {
    "launcher exit": False
}

FACTORIO_CONFIG_PATH = Path.joinpath(Path(os.environ['USERPROFILE']), "AppData\\Roaming\\Factorio\\launcher\\factorio_configs.txt")
FACTORIO_CONFIG_DICT = {
    "configs": []
}


