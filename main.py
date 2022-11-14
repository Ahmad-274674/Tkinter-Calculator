# Importing Required Modules
import tkinter as tk

# Functions --> Commands
def button_click(number):
    current = screen.get()
    screen.delete(0, tk.END)
    screen.insert(0, str(current) + str(number))

# Addition
def add():
    current = screen.get()
    if current == '':
        screen.insert(0, "0+")
    else:
        screen.delete(0, tk.END)
        screen.insert(0, str(current) + "+")

# Subtraction
def sub():
    current = screen.get().lstrip()
    if current == '':
        screen.insert(0, "0-")
    else:
        screen.delete(0, tk.END)
        screen.insert(0, str(current) + "-")

# Multiplication
def prod():
    current = screen.get()
    if current == '':
        screen.insert(0, "1*")
    else:
        screen.delete(0, tk.END)
        screen.insert(0, str(current) + "*")

# Division
def divs():
    current = screen.get()
    if current == '':
        screen.insert(0, "1/")
    else:
        screen.delete(0, tk.END)
        screen.insert(0, str(current) + "/")

# Evaluate
def evalEqual():
    current = screen.get().lstrip("0")
    print(current)
    try:
        if current == "":
            screen.insert(0, str(0))
        else:
            screen.delete(0, tk.END)
            screen.insert(0, eval(current))
    except Exception as e:
        screen.insert(0, "Error")

# Initializing GUI -> root
root = tk.Tk()
root.title("Calculator") # Set Title

# Set The Dimensions
root.geometry("300x270")
root.resizable(False, False)

# Screen
screen = tk.Entry(root, width=32)
screen.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=10, padx=10, pady=10)

# Buttons -- Initialize
button_0 = tk.Button(root, text="0", width=5, height=2, command=lambda: button_click(0))
button_1 = tk.Button(root, text="1", width=5, height=2, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", width=5, height=2, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", width=5, height=2, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", width=5, height=2, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", width=5, height=2, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", width=5, height=2, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", width=5, height=2, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", width=5, height=2, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", width=5, height=2, command=lambda: button_click(9))
buttonAdd = tk.Button(root, text="+", width=5, height=2, bg='crimson', fg='white', command=add)
buttonSub = tk.Button(root, text="-", width=5, height=2, bg='crimson', fg='white', command=sub)
buttonMultiple = tk.Button(root, text="x", width=5, height=2, bg='crimson', fg='white', command=prod)
buttonDivision = tk.Button(root, text="/", width=5, height=2, bg='crimson', fg='white', command=divs)
buttonEqual = tk.Button(root, text="=", width=14, height=2, bg="#0079fc", fg='white', command=evalEqual)

# Buttons -- On Screen
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
buttonDivision.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
buttonMultiple.grid(row=2, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
buttonSub.grid(row=3, column=3)

button_0.grid(row=4, column=0)
buttonEqual.grid(row=4, column=1, columnspan=2)
buttonAdd.grid(row=4, column=3)


root.mainloop() # Ending GUI -> root