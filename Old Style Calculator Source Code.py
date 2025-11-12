import tkinter as tk

root = tk.Tk()
root.config(background = "Grey")
root.geometry("500x400")
root.title("Calculator.exe")
root.resizable(False, False)
#The Math
#Show answer
def show_input(value):
    current = Screen.cget("text")
    Screen.config(text=current + str(value))
#Calculations
def calculate():
    try:
        expression = Screen.cget("text")
        result = eval(expression)
        Screen.config(text=str(result))
    except (SyntaxError, ZeroDivisionError, TypeError, NameError):
        Screen.config(text="Error")
        Screen.after(1000, lambda: Screen.config(text=""))
#for those who want press
def keypress(event):
    key = event.char
    if key.isdigit() or key in "+-*/":
        show_input(key)
    elif key == "\r" or "=":
        calculate()
    elif key.lower() == "c":
        Screen.config(text="")

root.bind("<Key>", keypress)

#numbers
one = tk.Button(root, width=10, height=2, text="1", bg="tan", activebackground="#a67c52", activeforeground="white",  command=lambda: show_input(1))
one.place(x=34, y=110)
two = tk.Button(root, width=10, height=2, text="2", bg="tan", activebackground="#a67c52", activeforeground="white", command=lambda:show_input("2"))
two.place(x=34, y=160)
three = tk.Button(root, width=10, height=2, text="3", bg="tan", activebackground="#a67c52", activeforeground="white", command=lambda:show_input("3"))
three.place(x=34, y=210)
four = tk.Button(root, width=10, height=2, text="4", bg="tan", activebackground="#a67c52", activeforeground="white", command=lambda:show_input("4"))
four.place(x=34, y=260)
five = tk.Button(root, width=10, height=2, text="5", bg="tan", activebackground="#a67c52", activeforeground="white", command=lambda:show_input("5"))
five.place(x=34, y=310)
six = tk.Button(root, width=10, height=2, text="6", bg="tan", activebackground="#a67c52", activeforeground="white", command=lambda:show_input("6"))
six.place(x=134, y=110)
seven = tk.Button(root, width=10, height=2, text="7", bg="tan", activebackground="#a67c52", activeforeground="white", command=lambda:show_input("7"))
seven.place(x=134, y=160)
eight = tk.Button(root, width=10, height=2, text="8", bg="tan", activebackground="#a67c52", activeforeground="white", command=lambda:show_input("8"))
eight.place(x=134, y=210)
nine = tk.Button(root, width=10, height=2, text="9", bg="tan", activebackground="#a67c52", activeforeground="white", command=lambda:show_input("9"))
nine.place(x=134, y=260)
zero = tk.Button(root, width=10, height=2, text="0", bg="tan", activebackground="#a67c52", activeforeground="white", command=lambda:show_input("0"))
zero.place(x=134, y=310)
#operation symbol
addition = tk.Button(root, width=15, height=2, text="+", bg="tan", activebackground="#a67c52", activeforeground="white", command=lambda:show_input("+"))
addition.place(x=234, y=110)
subtraction = tk.Button(root, width=15, height=2, text="-", bg="tan", activebackground="#a67c52", activeforeground="white", command=lambda:show_input("-"))
subtraction.place(x=234, y=160)
division = tk.Button(root, width=15, height=2, text="/", bg="tan", activebackground="#a67c52", activeforeground="white", command=lambda:show_input("/"))
division.place(x=234, y=210)
multiplication = tk.Button(root, width=15, height=2, text="*", bg="tan", activebackground="#a67c52", activeforeground="white", command=lambda:show_input("*"))
multiplication.place(x=234, y=260)
equal = tk.Button(root, width=15, height=10, text="=", bg="tan", activebackground="#a67c52", activeforeground="white", command=calculate)
equal.place(x=360, y=145)
#The Extras
Clear = tk.Button(root, width=15, height=2, text="Clear", bg="tan", activebackground="#a67c52", activeforeground="white", command=lambda: Screen.config(text=""))
Clear.place(x=234, y=310)
#Screen
Screen = tk.Label(root, width=15, height=1, text=" ", bg="#0000CC", bd=5, relief="ridge", font=("Courier", 40, "bold",), fg="green")
Screen.pack()
root.mainloop()

