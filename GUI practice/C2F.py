import tkinter as tk
import ttkbootstrap as ttk

def convert():
    fahrenheit = (1.8 * celc.get()) + 30          #    input_space.get() - not efficient. Create entry Var instead.
    Fahr.set(fahrenheit)


root = tk.Tk()
root.geometry("350x150")

title_label = tk.Label(root, text = "Celcius to Fahrenheit", font=("Times new roman", 24, 'bold'))
title_label.pack()

input_frame = ttk.Frame(root)
celc = tk.IntVar()                     # variable to store input 
input_space = tk.Entry(input_frame, textvariable=celc)
submit = ttk.Button(input_frame, text="Convert", command=convert)
input_space.pack(side="left", padx=10)
submit.pack(side='left')
input_frame.pack(pady=10)

Fahr = tk.StringVar()
Answer = ttk.Label(root, text = 'Tempreture', font=("Times new roman", 24), textvariable=Fahr)
Answer.pack(pady=5)


root.mainloop()