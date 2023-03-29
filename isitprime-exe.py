from pathlib import Path
from os import path, environ
from tkinter import Tk, Canvas, Entry, Button, PhotoImage





def resource_path(relative):
    return path.join(
        environ.get(
            "_MEIPASS2",
            path.abspath(".")
        ),
        relative
    )
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(resource_path("assets")) 
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.geometry("341x221")
window.title('Prime Number Check')
window.iconbitmap("isitprime.ico")
canvas = Canvas( window, bg = "#FFFFFF", height = 221, width = 341, bd = 0, highlightthickness = 0, relief = "ridge" )
canvas.place(x = 0, y = 0)





image_calculate_passive = PhotoImage( file=relative_to_assets("calculate_passive.png"))
image_calculate_prime = PhotoImage( file=relative_to_assets("calculate_prime.png"))
image_calculate_notprime = PhotoImage( file=relative_to_assets("calculate_notprime.png"))
image_entrybox_bg = PhotoImage( file=relative_to_assets("entrybox_bg.png"))
image_title = PhotoImage( file=relative_to_assets("title.png"))




title = canvas.create_image( 179.0, 39.0, image=image_title )
entrybox_bg = canvas.create_image( 173.0, 113.0, image=image_entrybox_bg )
calculate_bg = canvas.create_image( 173.0, 180.0, image=image_calculate_passive )


#Is Prime Number Logic/Changing Elements

def is_it_prime(number):
    entrybox.delete(0, 'end')
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                number_is_prime(False)
                break
        else:
            number_is_prime(True)
    else:
        number_is_prime(False)


def number_is_prime(boolean): 
    global resettimer   
    if boolean:
        canvas.itemconfigure(calculate_bg, image=image_calculate_prime)
        responsetext = 'Prime'
        color = '#3ABC38'
    else:
        canvas.itemconfigure(calculate_bg, image=image_calculate_notprime)
        responsetext = 'Non Prime'
        color = '#BC3838'
    calculate_button.configure(bg=color, text=responsetext, activebackground=color)
    resettimer = canvas.after(1000, reset_button)


def reset_button():
    calculate_button.configure(bg='#4043C8', text='Calculate', activebackground="#4043C8")
    canvas.itemconfigure(calculate_bg, image=image_calculate_passive)
    

#Button Code

calculate_button = Button( 
    activebackground="#4043C8",
    bg='#4043C8', 
    text='Calculate', 
    fg="#FFFFFF", 
    font=("Arial", 23 * -1), 
    borderwidth=0, 
    highlightthickness=0, 
    command=lambda: enter_pressed('<Return>'), 
    relief="flat" )

calculate_button.place( x=119.0, y=167.0, width=108.0, height=26.0 )


#Entry Box Code

def enter_pressed(event):
    prime_number = entrybox.get()

    try:
        prime_number = int(prime_number)
    except:
        return        
    try:
        canvas.after_cancel(resettimer)
    except:
        donothing=True

    is_it_prime(prime_number)


def validate_input(current_input):
    if current_input == "":
        return True
    try:
        int(current_input)
        return len(current_input) <= 6
    except ValueError:
        return False

validate_cmd = window.register(validate_input)

entrybox = Entry( bd=0, bg="#CCCCCC", fg="#000716", highlightthickness=0, justify="center", font=("Arial", 25 * -1), validate='key', validatecommand=(validate_cmd, '%P'))
entrybox.place( x=130.0, y=98.0, width=87.0, height=29.0 )
entrybox.bind('<Return>', enter_pressed)



window.resizable(False, False)
window.mainloop()
