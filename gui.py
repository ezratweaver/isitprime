from tkinter import Canvas, Entry, Button
from window import window
from assets import Assets


class Gui():
    """Light Mode Class"""

    def __init__(self):
        self.main_canvas = Canvas(
            window,
            bg="#FFFFFF",
            height=220,
            width=341,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.main_canvas.pack()
        
        self.calculate_bg = self.main_canvas.create_image(
            173.0, 180.0, image=Assets.image_light_calculate_passive)
        self.entry_bg = self.main_canvas.create_image(
            173.0, 113.0, image=Assets.image_light_entry_bg)
        self.title = self.main_canvas.create_image(
            179.0, 39.0, image=Assets.image_light_title)

        self.calculate_button = Button(
            activebackground="#0067C0",
            bg="#0067C0",
            text="Calculate",
            fg="#FFFFFF",
            font=("Arial", 23 * -1),
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.input_taken("<Return>"),
            relief="flat")
        self.calculate_button.place(x=116.0, y=160.0, width=116.0, height=40.0)

        self.keypress = window.register(self.is_input_valid)
        self.entrybox = Entry(
            bd=0, bg="#CCCCCC",
            fg="#000716",
            highlightthickness=0,
            justify="center",
            font=("Arial", 25 * -1),
            validate="key",
            validatecommand=(self.keypress, "%P"))

        self.entrybox.place(x=130.0, y=98.0, width=87.0, height=29.0)
        self.entrybox.bind("<Return>", self.input_taken)

        self.theme_switch = Button(
            self.main_canvas,
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            image=Assets.image_light_theme_switch,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: None,
            relief="flat")
        self.theme_switch.place(x=8.0, y=192.0, width=24.0, height=24.0)

    def activate_lightmode(self):
        """Activates Light Mode"""

    def activate_darkmode(self):
        """Activates Dark Mode"""

    def show_if_prime(self, boolean):
        """Change The Calculate Button To Reflect If Number is Prime"""
        global global_resettimer
        if boolean:
            self.main_canvas.itemconfigure(
                self.calculate_bg, image=Assets.image_calculate_prime)
            responsetext = "Prime"
            color = "#3ABC38"
        else:
            self.main_canvas.itemconfigure(
                self.calculate_bg, image=Assets.image_calculate_notprime)
            responsetext = "Non Prime"
            color = "#BC3838"
        self.calculate_button.configure(
            bg=color, text=responsetext, activebackground=color)
        global_resettimer = self.main_canvas.after(1000, self.reset_calculate_button)

    def reset_calculate_button(self):
        """Reset Calculate Button Back To Normal"""
        self.calculate_button.configure(
            bg="#0067C0", text="Calculate", activebackground="#0067C0")
        self.main_canvas.itemconfigure(
            self.calculate_bg, image=Assets.image_light_calculate_passive)
        
    def input_taken(self, event):
        """Ran when user input is accepted"""
        prime_number = self.entrybox.get()
        self.entrybox.delete(0, "end")
        try:
            prime_number = int(prime_number)
        except:
            return
        try:
            self.main_canvas.after_cancel(global_resettimer)
        except:
            pass
        self.show_if_prime(self.is_it_prime(prime_number))

    def is_input_valid(self, current_input):
        """Check if user input is valid to be entered"""
        if current_input == "":
            return True
        try:
            int(current_input)
            return len(current_input) <= 6
        except ValueError:
            return False

    def is_it_prime(self, number):
        """Checking if number is prime"""
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    return False
            return True
        else:
            return False

if __name__ == "__main__":
    gui = Gui()
    window.resizable(False, False)
    window.mainloop()
