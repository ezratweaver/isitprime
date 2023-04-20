from gui import Gui, window


if __name__ == "__main__":
    gui = Gui()
    gui.show_lightmode_canvas()
    window.resizable(False, False)
    window.mainloop()
