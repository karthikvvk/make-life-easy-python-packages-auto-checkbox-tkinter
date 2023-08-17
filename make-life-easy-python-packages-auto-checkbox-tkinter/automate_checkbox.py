"""
cr_checkbox(): takes the tkinter window object and the items to be listed as arguments and return checkbox objects as list.
fetch_cked_val(): takes the list returned by cr_checkbox() as argument and return a list of checked/selected items.
**NOTE: ONLY WORK FOR TKINTER.
    >Default  layout managers is .grid()
    >Please change according  to your prefered layout managers(.place(), .pack(), etc.).
"""
from tkinter import *

vari = []
seq = []
obu = []
len_seq = 0


def cr_checkbox(tk_window_object, sequence, bg='white', fg='black', row_lb=0, column_lb=0):
    global vari, seq, obu, len_seq
    vari, row_l = [], []
    len_seq = len(sequence)
    seq = sequence

    for y in range(row_lb, len_seq + row_lb):
        row_l.append(y)

    for i in range(len_seq):
        vari.append('a' + str(i))
        obu.append('a' + str(i))
        vari[i] = BooleanVar(tk_window_object, value=False)
        obu[i] = Checkbutton(tk_window_object, text=sequence[i], variable=vari[i], bg=bg, justify='left', fg=fg)
        obu[i].grid(row=row_l[i], column=column_lb)

    return [vari, obu]


def fetch_cked_val(chbx_obj):
    global seq

    bx_chked = []
    for t in range(len(seq)):
        if chbx_obj[t].get():
            bx_chked.append(seq[t])

    return bx_chked


def remove(element=[], remove_all=False):
    global obu, seq, vari
    if element:
        for i in element:
            ind = seq.index(element[i])
            obu[ind].destroy()
            obu.pop(ind)
    else:
        obu[-1].destroy()
        obu.pop()
    if remove_all:
        for i in obu:
            i.destroy()
            obu = []


def add(tk_window_object, row_lb=0, elements=[], bg='white', fg='black', column_lb=0):
    global obu, seq, vari, len_seq
    if row_lb > len_seq:
        pass
    else:
        row_lb = len_seq
    row_l = []

    add_len_seq = len(elements)
    seq += elements

    for y in range(row_lb, add_len_seq + row_lb+1):
        row_l.append(y)

    for i in range(len_seq, len_seq+add_len_seq):
        vari.append('a' + str(i))
        obu.append('a' + str(i))
        vari[i] = BooleanVar(tk_window_object, value=False)
        obu[i] = Checkbutton(tk_window_object, text=elements[len_seq-i], variable=vari[i], bg=bg, justify='left', fg=fg)
        obu[i].grid(row=i, column=column_lb)
    len_seq = len_seq+add_len_seq
