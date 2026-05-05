# Anna Pestova, CSC221.40C, Spring 2026
''' Purpose: 

This is a Final Project for CSC.221.40C Introduction to Problem Solving and Programming course.

Problem statement:

This application allows to convert numbers from decimal number system (base 10) to binary (base2), octal (base 8), 
and hexadecimal (base 16) numbers, and vice versa. 

The functions to convert to decimal and to bases 2, 8, and 16 are in base_conversion.py file.

The goal was to implement this conversion using custom function with additional error handling.

This file contains code to test functionality via terminal (lines 23-31) - need to uncomment the code (and comment out all other code)

Starting with the line 34 - it is the GUI support. 

For GUI I selected tkinter library.'''

import base_conversion as bc

# test using terminal input
# is_decimal = input("Do you want to convert number to decimal (Y/N)? ")
# n = input("What number do you want to transfer? ")
# base = input(f"#{'From what base' if is_decimal == 'Y' else 'To what base'} do you want to convert the number (2, 8, or 16)? ")

# if is_decimal == "Y":
#     print(bc.to_decimal(int(base), n))
# else:
#     print(bc.to_base(int(base), n))


from tkinter import *
import tkinter as tk
from tkinter import  ttk
from tkinter import messagebox
from tkinter import font


root = Tk()

root.title("Number Converter")


mainframe = ttk.Frame(root, padding=150)
mainframe.grid()
mainframe['borderwidth'] = 2
mainframe['relief'] = 'sunken'

main_font = font.Font(family='Helvetica', size=12) 
result_font = font.Font(family='Helvetica', size=18, weight='bold') 
label_font = font.Font(family='Helvetica', size=14, weight='bold')
button_font = font.Font(family='Helvetica', size=14)

# Choose convert function
ttk.Label(mainframe, text="From base to decimal?", font=label_font).grid(column=1, row=4)

is_to_decimal = tk.BooleanVar()
r1 = tk.Radiobutton(mainframe, text="base -> 10", 
   variable=is_to_decimal, value=True, font=main_font)
r2 = tk.Radiobutton(mainframe, text="10 -> base", 
   variable=is_to_decimal, value=False, font=main_font)
is_to_decimal.set(True)
r1.grid(column=2, row=3, pady=(10,10))
r2.grid(column=2, row=5, pady=(10,10))


# Input for number to convert to decimal
ttk.Label(mainframe, text="Enter value", font=label_font).grid(column=1, row=6)
number_var=tk.StringVar()
number_entry = tk.Entry(mainframe, textvariable = number_var)
number_entry.grid(column=2, row=6, pady=(10,10))

# Dropdown for base to convert to decimal
base_var = tk.IntVar()
base_variants = ttk.Combobox(mainframe, width=4,textvariable=base_var)
# Dropdown list
base_variants['values'] = (2,8,16)
base_var.set(2)

base_variants.grid(column=3, row=6, pady=(10,10))
base_variants.current()

   

# run function when button 'Calculate' clicked
def calculate():
   try: 
      to_decimal = is_to_decimal.get()
      n = number_var.get()
      base = base_var.get()
      result = ""
      # run methods to_decimal or to_base depend on user input
      if to_decimal == True:
         result = bc.to_decimal(base, n) 
      else:
         result = bc.to_base(base, n)
      display_data.set(result)

   except Exception as e:
      #  show errors
      messagebox.showerror(title= "Exception raised",message = str(e), parent=mainframe)
      is_to_decimal.set(True)
      number_var.set("")
      base_var.set(2)


display_data = StringVar()
display_data.set("")

ttk.Label(mainframe, textvariable=display_data, padding=10, font=result_font).grid(column=2, row=9)

tk.Button(mainframe, text="Calculate", font=button_font, command=calculate, padx=5, pady=5).grid(column=2, row=10, pady=(10,10))

# run function when button 'Reset window' clicked
def reset():
   is_to_decimal.set(True)
   number_var.set("")
   base_var.set(2)

# reset form
tk.Button(mainframe, text="Reset window", command=reset, font=button_font, padx=5, pady=5).grid(column=2, row=12, pady=(10,10))


root.mainloop()