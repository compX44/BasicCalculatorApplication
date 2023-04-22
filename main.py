from tkinter import *

# This is a basic calculator app

# Calculator interface
root = Tk()
root.configure(bg="black")
root.title("Basic Calculator")

# Window for Calculator
win = Entry(root, width=35, borderwidth=5)
win.grid(row=0, column=0, columnspan=4, padx=20, pady=20)
win.configure(bg="light green")

# Functions for button behaviors
def button_click(number):
    current = win.get()
    win.delete(0,END)
    win.insert(0, str(current) + str(number))

def button_addition():
    first_num = win.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_num)
    win.delete(0,END)

def button_subtraction():
    first_number = win.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    win.delete(0, END)

def button_multiplication():
    first_number = win.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    win.delete(0, END)

def button_division():
    first_number = win.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    win.delete(0, END)

def button_equal():
    second_num = win.get()
    win.delete(0, END)

    if math == "addition":
        win.insert(0, f_num + int(second_num))

    elif math == "subtraction":
        win.insert(0, f_num - int(second_num))

    elif math == "multiplication":
        win.insert(0, f_num * int(second_num))

    else:
        win.insert(0, f_num / int(second_num))

def button_clear():
    win.delete(0, END)

# Buttons for the calculator:

# Number buttons
button_1 = Button(root, text="1", padx=45, pady=20, bg="deep sky blue", command=lambda:button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, bg="deep sky blue", command=lambda:button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, bg="deep sky blue", command=lambda:button_click(3))
button_4 = Button(root, text="4", padx=45, pady=20, bg="deep sky blue", command=lambda:button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, bg="deep sky blue", command=lambda:button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, bg="deep sky blue", command=lambda:button_click(6))
button_7 = Button(root, text="7", padx=45, pady=20, bg="deep sky blue", command=lambda:button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, bg="deep sky blue", command=lambda:button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, bg="deep sky blue", command=lambda:button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, bg="deep sky blue", command=lambda:button_click(0))

# Operation buttons
button_add = Button(root, text="+", padx=40, pady=20, fg="white", bg="blue", command=button_addition)
button_sub = Button(root, text="-", padx=40, pady=20, fg="white", bg="blue", command=button_subtraction)
button_mult = Button(root, text="x", padx=40, pady=20, fg="white", bg="blue", command=button_multiplication)
button_div = Button(root, text="/", padx=40, pady=20, fg="white", bg="blue", command=button_division)
button_eql = Button(root, text="=", padx=40, pady=20, bg="slate blue", command=button_equal)
button_clr = Button(root, text="Clr", padx=40, pady=20, bg="sky blue", command=button_clear)

# Button placement
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)

button_add.grid(row=4, column=3)
button_sub.grid(row=3, column=3)
button_mult.grid(row=2, column=3)
button_div.grid(row=1, column=3)
button_eql.grid(row=4, column=2)
button_clr.grid(row=4, column=0)

# Display the interface
root.mainloop()