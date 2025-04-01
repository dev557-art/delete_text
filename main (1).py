from tkinter import Tk, Text, Button, Label, END
import time

window = Tk()
window.title("My program")
window.geometry("500x500")
window.configure(background='#f7f5dd')

start_time = None
elapsed_time = 0
running = False

last_edit_time = None  

def start_timer(event=None):
    global start_time, running, last_edit_time
    if not running:
        running = True
        start_time = time.time()
        last_edit_time = time.time()  
        update_timer()

def update_timer():
    global elapsed_time, running, last_edit_time
    if running:
        elapsed_time = round(time.time() - start_time, 2)
        

        if input_label.edit_modified():
            last_edit_time = time.time()  
            input_label.edit_modified(False)  
        if time.time() - last_edit_time > 2:  
            
            elapsed_time = round(time.time() - start_time, 2)
        
            if elapsed_time > 10:
                input_label.delete("1.0", END)
            
        window.after(10, update_timer)




input_label = Text(window, bg='white', height=5, width=40, font=('Arial', 12))
input_label.pack()
input_label.config(state='normal')
input_label.bind("<Key>", start_timer)




window.mainloop()