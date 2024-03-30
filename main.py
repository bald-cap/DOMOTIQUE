from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("DomotiQue")
root.config(bg="#111E26")


rooms_frame = Frame(root, width=100, height=50, bg="#273139")
rooms_frame.grid(row=0, column=1)

def return_rooms():
    if rooms_frame.winfo_viewable():
        rooms_frame.grid_remove()

def enter_state(event):
    return_btn.config(bg="#273339")

def leave_state(event):
    return_btn.config(bg='#39454B')

return_btn = Button(rooms_frame, width=3, height=1, text="<", font=("Segoe UI", 10, "bold"), command=lambda: return_rooms(), justify='center', bg="#39454B", fg='#E9EBEE')

return_btn.bind('<Enter>', enter_state)
return_btn.bind('<Leave>', leave_state)
return_btn.grid(row=0, column=0, padx=10)

def hover_state_opt(event):
    menu_opt.itemconfig(ACTIVE, {'bg': '#0D151C', 'fg' : '#D3D6DB'})

    index = menu_opt.nearest(event.y)
    menu_opt.itemconfig(index, {'bg' : '#2D3340'} )

    menu_opt.activate(index)

def leave_state_opt(event):
    menu_opt.intemconfig()
menu_opt = Listbox(rooms_frame, selectmode=SINGLE, bg="#0D151C", fg="#D3D6DB", font=("Segoe UI", 12, 'bold'), justify='center')
menu_opt.bind('<Motion>', hover_state_opt)
menu_opt.grid(row=0, column=1)

menu_opt.insert(END, '')
menu_opt.insert(END, '')
menu_opt.insert(END, 'Kitchen')
menu_opt.insert(END, '')
menu_opt.insert(END, 'Bedroom')
menu_opt.insert(END, '')
menu_opt.insert(END, 'Toilet')
menu_opt.insert(END, '')
# menu_holder.pack()


doms_frame = Frame(root, width=50, height=50)
doms_frame.grid(row=0, column=3)
columns, rows = root.grid_size()

for i in range(columns):
    root.grid_columnconfigure(i, weight=1)

for i in range(rows):
    root.rowconfigure(i, weight=1)

root.mainloop()