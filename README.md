Creates checkboxes using the given sequence and return the checkbox objects in 'vari'
Also can get the checked items using fetch_cked_val(); return as list
That is 'print(cr_checkbox(tk_window_object, sequence)[1])' will print all the checkbox's objects.
And

for i in cr_checkbox(tk_window_object, sequence)[1]:
        print(i.get())

the above will print the value(1 or 0), that is the status of checked(1) or unchecked(0).
