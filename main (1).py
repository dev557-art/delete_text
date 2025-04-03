from tkinter import Tk, Text, Button, Label, END
import time

window = Tk()
window.title("My program")
window.geometry("500x500")
window.configure(background='#f7f5dd')

INACTIVITY_TIMEOUT = 4  # Seconds of inactivity before deleting text
last_edit_time = None
running = False

def start_timer(event=None):
    global running, last_edit_time
    if not running:
        running = True
        last_edit_time = time.time()
        update_timer()

def update_timer():
    global running, last_edit_time
    if running:
        if input_label.edit_modified():
            last_edit_time = time.time()
            input_label.edit_modified(False)
            
        # Check if enough time has passed since last edit
        if time.time() - last_edit_time >= INACTIVITY_TIMEOUT:
            input_label.delete("1.0", END)
            running = False  # Stop the timer after deleting
        else:
            window.after(100, update_timer)

input_label = Text(window, bg='white', height=5, width=40, font=('Arial', 12))
input_label.pack()
input_label.config(state='normal')
input_label.bind("<Key>", start_timer)

window.mainloop()