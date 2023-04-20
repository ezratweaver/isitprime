from os import path, chdir
from sys import argv
from pathlib import Path
from tkinter import PhotoImage

EXE_DIR = path.dirname(argv[0])
chdir(EXE_DIR)

OUTPUT_PATH = EXE_DIR
ASSETS_PATH = OUTPUT_PATH / Path("assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class Assets():
    """All Imported Assets"""
    image_light_entry_bg = PhotoImage(
        file=relative_to_assets("lightmode/entry_bg_light.png"))
    image_light_title = PhotoImage(
        file=relative_to_assets("lightmode/title_light.png"))
    image_light_theme_switch = PhotoImage(
        file=relative_to_assets("lightmode/theme_switch_light.png"))
    image_dark_entry_bg = PhotoImage(
        file=relative_to_assets("darkmode/entry_bg_dark.png"))
    image_dark_title = PhotoImage(
        file=relative_to_assets("darkmode/title_dark.png"))
    image_dark_theme_switch = PhotoImage(
        file=relative_to_assets("darkmode/theme_switch_dark.png"))
    image_light_calculate_passive = PhotoImage(
        file=relative_to_assets("lightmode/calculate_neutral_light.png"))
    image_dark_calculate_passive = PhotoImage(
        file=relative_to_assets("darkmode/calculate_neutral_dark.png"))
    image_calculate_prime = PhotoImage(
        file=relative_to_assets("calculate_prime.png"))
    image_calculate_notprime = PhotoImage(
        file=relative_to_assets("calculate_notprime.png"))