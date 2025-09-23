from tkinter import *

def press_button(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_var.set(equation_text)

def equals():
    global equation_text
    try:
        result = eval(equation_text)
        equation_var.set(result)
    except ZeroDivisionError:
        equation_var.set('arithmetic error')
    except SyntaxError:
        equation_var.set('synatax error')

def clear():
    global equation_text
    equation_text = ''
    equation_var.set(equation_text)


window = Tk()

window.title('Calculator')
window.geometry('250x250')

equation_text = ""

equation_var = StringVar()

equation_label = Label(window, textvariable=equation_var, font=('Arial', 14), bg='white', width=20)
equation_label.pack()


frame = Frame(window)
frame.pack()

button1 = Button(frame, text='1', font=('Arial', 14), bg='white', width=3,
                 command=lambda: press_button(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text='2', font=('Arial', 14), bg='white', width=3,
                 command=lambda: press_button(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text='3', font=('Arial', 14), bg='white', width=3,
                 command=lambda: press_button(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text='4', font=('Arial', 14), bg='white', width=3,
                 command=lambda: press_button(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text='5', font=('Arial', 14), bg='white', width=3,
                 command=lambda: press_button(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text='6', font=('Arial', 14), bg='white', width=3,
                 command=lambda: press_button(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text='7', font=('Arial', 14), bg='white', width=3,
                 command=lambda: press_button(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text='8', font=('Arial', 14), bg='white', width=3,
                 command=lambda: press_button(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text='9', font=('Arial', 14), bg='white', width=3,
                 command=lambda: press_button(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text='0', font=('Arial', 14), bg='white', width=3,
                 command=lambda: press_button(0))
button0.grid(row=3, column=1)

plus = Button(frame, text='+', font=('Arial', 14), bg='white', width=3,
              command=lambda: press_button('+'))
plus.grid(row=0, column=3)

minus = Button(frame, text='-', font=('Arial', 14), bg='white', width=3,
               command=lambda: press_button('-'))
minus.grid(row=1, column=3)

multiply = Button(frame, text='*', font=('Arial', 14), bg='white', width=3,
                  command=lambda: press_button('*'))
multiply.grid(row=2, column=3)

dot = Button(frame, text='.', font=('Arial', 14), bg='white', width=3,
             command=lambda: press_button('.'))
dot.grid(row=3, column=2)

devision = Button(frame, text='/', font=('Arial', 14), bg='white', width=3,
                  command=lambda: press_button('/'))
devision.grid(row=3, column=3)

equal = Button(frame, text='=', font=('Arial', 14), bg='white', width=3,
               command=lambda: equals())
equal.grid(row=3, column=0)


clear_button = Button(window, text='Clear', font=('Arial', 12), bg='white', width=5, relief=RAISED, command=clear)
clear_button.pack()
window.mainloop()