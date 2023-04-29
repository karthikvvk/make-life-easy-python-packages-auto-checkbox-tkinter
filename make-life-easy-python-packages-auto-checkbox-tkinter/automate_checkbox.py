"""
Create checkboxes using the given sequence and return the checkbox objects in 'vari'
That is 'print(cr_checkbox(tk_window_object, sequence)[1])' will print all the checkbox's objects.
And 

for i in cr_checkbox(tk_window_object, sequence)[1]:
        print(i.get())

the above will print the value(1 or 0), that is the status of checked(1) or unchecked(0).
"""
from tkinter import *


def cr_checkbox(tk_window_object, sequence, bg='white', fg='black', row=0, column=0):
    len_seq = len(sequence)
    vari = []
    row_l = []

    for y in range(row, len_seq + row):
        row_l.append(y)

    for i in range(len_seq):
        vari.append('a' + str(i))
        vari[i] = IntVar(tk_window_object, value=0)

    for i in range(len_seq):
        Checkbutton(tk_window_object, text=sequence[i], variable=vari[i], bg=bg, justify='left', fg=fg).grid(
            row=row_l[i], column=column)
    return [len_seq, vari, sequence]
    