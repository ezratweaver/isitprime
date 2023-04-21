from gui import Gui, window
from winreg import OpenKey, QueryValueEx, CloseKey, HKEY_CURRENT_USER

def is_dark_mode_enabled():
    """Checks registry if user is in dark mode"""
    registry_path = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize'
    registry_key = 'AppsUseLightTheme'
    try:
        reg = OpenKey(HKEY_CURRENT_USER, registry_path)
        value, registry_type = QueryValueEx(reg, registry_key)
        CloseKey(reg)
        return value == 0
    except WindowsError:
        return False


if __name__ == "__main__":
    gui = Gui()
    if is_dark_mode_enabled():
        gui.activate_darkmode()
    window.title("Prime Number Check")
    window.iconbitmap("isitprime.ico")
    window.resizable(False, False)
    window.mainloop()
