from tkinter import *
import time

def update():
    clock_lable.config(text=time.strftime("%I:%M:%S %p"))
    day_lable.config(text=time.strftime("%A"))
    date_label.config(text=time.strftime("%B %d, %Y"))


    window.after(1000, update)

window = Tk()
clock_lable = Label(window, fg='green', bg='black', font=('Arial', 50))
clock_lable.pack()

day_lable = Label(window, font=('Segoe Script', 30))
day_lable.pack()

date_label = Label(window, font=('Segoe Script', 25))
date_label.pack()


update()
window.mainloop()