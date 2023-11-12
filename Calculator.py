import tkinter as tk
from tkinter import messagebox

win = tk.Tk()               # Импортируем класс
win.title("Calculator")       # Название
win.geometry("390x430+100+200")  # Размеры
win.resizable(True, True)         # Маштабирование

entry = tk.Entry(win, width=20, bd=5, font=("arial", 20), justify="right")

entry.grid(row=0, column=0, columnspan=4, sticky="WENS")


def add_numbers(number):
    value = entry.get() + str(number)
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    entry.delete(0, tk.END)
    entry.insert(0, value)


def add_operations(operation):
    value = entry.get()
    if value[-1] in "+-/*":
        value = value[-1]
    entry.delete(0, tk.END)
    entry.insert(0, value + operation)


def numbers(number):
    return tk.Button(win, text=number, bd=5, height=2, width=3,
                     font=("arial", 15), command=lambda: add_numbers(number))


def operations(operation):
    return tk.Button(win, text=operation, bd=5, height=2, width=4,
                     font=("arial", 15), command=lambda: add_numbers(operation))


def calc_button(operation):
    return tk.Button(win, text=operation, bd=5, height=2, width=4,
                     font=("arial", 15), command=calculate)


def calculate():
    value = entry.get()
    entry.delete(0, tk.END)
    try:
        entry.insert(0, eval(value))
    except ZeroDivisionError:
        tk.messagebox.showerror(title="Error", message="You can't divide by zero")


if __name__ == "__main__":
    numbers(1).grid(row=1, column=0, sticky="wens")
    numbers(2).grid(row=1, column=1, sticky="wens")
    numbers(3).grid(row=1, column=2, sticky="wens")
    numbers(4).grid(row=2, column=0, sticky="wens")
    numbers(5).grid(row=2, column=1, sticky="wens")
    numbers(6).grid(row=2, column=2, sticky="wens")
    numbers(7).grid(row=3, column=0, sticky="wens")
    numbers(8).grid(row=3, column=1, sticky="wens")
    numbers(9).grid(row=3, column=2, sticky="wens")
    numbers(0).grid(row=4, column=0, sticky="wens")

    tk.Button(win, text="c", bd=5, height=2, width=4, font=("arial", 15),
              command=lambda: entry.delete(0, tk.END)).grid(row=1, column=3, sticky="wens")

    operations("+").grid(row=2, column=3, sticky="wens")
    operations("-").grid(row=3, column=3, sticky="wens")
    operations("/").grid(row=4, column=2, sticky="wens")
    operations("*").grid(row=4, column=1, sticky="wens")

    calc_button("=").grid(row=4, column=3, sticky="wens")

    win.columnconfigure(1, minsize=70)
    win.columnconfigure(0, minsize=80)
    win.columnconfigure(3, minsize=70)
    win.columnconfigure(4, minsize=70)
    win.columnconfigure(5, minsize=70)

    win.mainloop()
  
