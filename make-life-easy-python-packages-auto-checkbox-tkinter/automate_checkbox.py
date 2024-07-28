from tkinter import *
from collections import OrderedDict
 
class automate_checkbox:
    vari = OrderedDict()
    seq = []
    obj = OrderedDict()
    len_seq = 0
    root = 0
    starting_row = 0
    starting_col = 0
    
    def __init__(self, window) -> None:
        self.root = window
        
    def cr_checkbox(self, sequence, bg='white', fg='black', row_lb=0, column_lb=0):
        self.len_seq = len(sequence)
        self.seq = sequence
        self.starting_row = row_lb
        self.starting_col = column_lb
        row_l = []
        for y in range(row_lb, self.len_seq + row_lb):
            row_l.append(y)

        for i in range(self.len_seq):
            it = self.seq[i]
            self.vari[it] = BooleanVar(self.root, value=False)
            self.obj[it] = Checkbutton(self.root, text=it, variable=self.vari[it], bg=bg, justify='left', fg=fg)
            self.obj[it].grid(row=row_l[i], column=column_lb)
        
    def fetch_cked_val(self):
        lis = []
        for i in self.seq:
            if self.vari[i].get():
               lis.append(i) 
        return lis
    
    def remove_box(self, element=[], remove_all=False):
        if remove_all:
            for i in self.seq:
                self.obj[i].destroy()
                del self.obj[i]

                del self.vari[i]

                self.seq.remove(i)
                self.len_seq = 0
        elif element:
            le = len(element)
            for i in element:
                self.obj[i].destroy()
                del self.obj[i]

                del self.vari[i]

                self.seq.remove(i)
            self.len_seq -= le
        else:
            ele = self.seq[-1]
            self.obj[ele].destroy()
            del self.obj[ele]

            del self.vari[ele]

            self.seq.remove(ele)
            self.len_seq -= 1

        for i in range(self.len_seq):
            it = self.seq[i]
            self.obj[it].grid(row=self.starting_row+i, column=self.starting_col)
        
    def add_box(self, squence=[], bg='white', fg='black', rlb=starting_row, column_lb=starting_col):
        ln = len(squence)
        sq = squence
        variables, objts = OrderedDict(), OrderedDict()
        
        for i in range(ln):
            it = sq[i]
            variables[it] = BooleanVar(self.root, value=False)
            objts[it] = Checkbutton(self.root, text=it, textvariable=variables[it], bg=bg, justify='left', fg=fg)

        org_dict = list(self.obj.items())
        new_dict = list(objts.items())
        org_vari_dict = list(self.vari.items())
        new_vari_dict = list(variables.items())
        for i in range(ln):
            self.seq.insert(rlb+i, squence[i])
            org_dict.insert(rlb+i, new_dict[i])
            org_vari_dict.insert(rlb+i, new_vari_dict[i])
        
        self.len_seq = len(self.seq)
        self.obj = OrderedDict(org_dict)
        self.vari = OrderedDict(org_vari_dict)

        for i in range(self.len_seq):
            it = self.seq[i]
            self.obj[it].grid(row=rlb+i, column=column_lb)
