from tkinter import *

root = Tk()
root.geometry("750x500")
root.title("DomotiQue")
root.config(bg="#111E26")


rooms_frame = Frame(root, width=100, height=50, bg="#111E26")
rooms_frame.grid(row=0, column=0)

def return_rooms():
    if rooms_frame.winfo_viewable():
        rooms_frame.grid_remove()

def enter_state(event):
    return_btn.config(bg="#273339")

def leave_state(event):
    return_btn.config(bg='#39454B')

return_btn = Button(rooms_frame, width=3, height=0, text="<", font=("Archivo Black", 10, 'bold'), command=lambda: return_rooms(), justify='center', bg="#39454B", fg='#E9EBEE')

return_btn.bind('<Enter>', enter_state)
return_btn.bind('<Leave>', leave_state)
return_btn.grid(row=0, column=0, pady=10)

def hover_state_rooms_opt(event):
    rooms_opt.itemconfig(ACTIVE, {'bg': '#0D151C', 'fg' : '#D3D6DB'})
    index = rooms_opt.nearest(event.y)

    if rooms_opt.get(index) != '':
        rooms_opt.itemconfig(index, {'bg' : '#2D3340'})
    else:
        rooms_opt.itemconfig(index, {'bg' : '#0D151C'})

    rooms_opt.activate(index)

def select_state_rooms_opt(event):
    pos_rooms_opt_tup = rooms_opt.curselection()
    pos_opt = pos_rooms_opt_tup[0]
    opt = rooms_opt.get(pos_opt)

    if opt.strip() != '':
        rooms_opt.itemconfig(pos_opt, selectbackground="#033F4D")
    else:
        rooms_opt.itemconfig(pos_opt, selectbackground='#0D151C')
    
def leave_state_rooms_opt(event):
    pos_rooms_opt_tup = rooms_opt.curselection()

    if pos_rooms_opt_tup:
        pos_rooms_opt = pos_rooms_opt_tup[0]
        for i in range(rooms_opt.size()):
            if i != pos_rooms_opt:
                rooms_opt.itemconfig(i, {'bg' : '#0D151C'})
    else:
        for i in range(rooms_opt.size()):
            rooms_opt.itemconfig(i, {'bg' : '#0D151C'})

rooms_opt = Listbox(rooms_frame, selectmode=SINGLE, bg="#0D151C", fg="#D3D6DB", font=("Segoe UI", 12, 'bold'), justify='center', highlightthickness=0, borderwidth=0, selectbackground="#033F4D", exportselection=False)
rooms_opt.bind('<Motion>', hover_state_rooms_opt)
rooms_opt.bind('<<ListboxSelect>>', select_state_rooms_opt)
rooms_opt.bind('<Leave>', leave_state_rooms_opt)
rooms_opt.grid(row=1, column=0)

rooms_opt.insert(END, '')
rooms_opt.insert(END, '')
rooms_opt.insert(END, 'Kitchen')
rooms_opt.insert(END, '')
rooms_opt.insert(END, 'Bedroom')
rooms_opt.insert(END, '')
rooms_opt.insert(END, 'Toilet')
rooms_opt.insert(END, '')


objs_frame = Frame(root, width=50, height=50)
objs_frame.grid(row=0, column=1)

def hover_state_objs_opt(event):
    objs_opt.itemconfig(ACTIVE, {'bg': '#0D151C', 'fg' : '#D3D6DB'})

    index = objs_opt.nearest(event.y)
    if objs_opt.get(index) != '':
        objs_opt.itemconfig(index, {'bg' : '#2D3340'})
    else:
        objs_opt.itemconfig(index, {'bg' : '#0D151C'})

    objs_opt.activate(index)

def select_state_objs_opt(event):
    pos_objs_opt_tup = objs_opt.curselection()
    pos_opt = pos_objs_opt_tup[0]
    opt = objs_opt.get(pos_opt)

    if opt.strip() != '':
        objs_opt.itemconfig(pos_opt, selectbackground='#033F4D')
    else:
        objs_opt.itemconfig(pos_opt, selectbackground='#0D151C')

def leave_state_objs_opt(event):
    pos_objs_opt_tup = objs_opt.curselection()

    if pos_objs_opt_tup:
        pos_objs_opt = pos_objs_opt_tup[0]
        for i in range(objs_opt.size()):
            if i != pos_objs_opt:
                objs_opt.itemconfig(i, {'bg' : '#0D151C'})
    else:
        for i in range(objs_opt.size()):
            objs_opt.itemconfig(i, {'bg' : '#0D151C'})
        
        
objs_opt = Listbox(objs_frame, selectmode=SINGLE, highlightthickness=0, borderwidth=0, justify='center', font=("Segoe UI", 12, "bold"), fg="#D3D6DB", bg="#0D151C", exportselection=False, )
objs_opt.bind('<Motion>', hover_state_objs_opt)
objs_opt.bind('<<ListboxSelect>>', select_state_objs_opt)
objs_opt.bind('<Leave>', leave_state_objs_opt)
objs_opt.grid(row=0, column=0)

objs_opt.insert(END, '')
objs_opt.insert(END, '')
objs_opt.insert(END, '')
objs_opt.insert(END, 'Radiator')
objs_opt.insert(END, '')
objs_opt.insert(END, 'Lights')
# objs_opt.insert(END, '')


lights_frame = Frame(root, width=30, height=50, bg="#48575E")
lights_frame.grid(row=0, column=2)

lights_state_frame = Frame(lights_frame, bg='#111E26', borderwidth=1, highlightthickness=1)
lights_state_frame.grid(row=0, column=0)
lights_state_intro = Label(lights_state_frame, text='STATE :', font=('Segoe UI sans serif', 15, 'bold'), bg='#111E26', fg='#D3D6DB')
lights_state_intro.grid(row=0, column=0)

state = StringVar()
state.set("ON")
lights_state = Label(lights_state_frame, textvariable=state, font=('Segoe UI sans serif', 15, 'bold'), bg='#00C59F', fg='#364B44')
lights_state.grid(row=0, column=1, padx=5, pady=5)

intens = StringVar()
intens.set('LOW')

intens_frame = Frame(lights_frame, borderwidth=1, highlightthickness=1)
intens_frame.grid(row=2, column=0)

lights_intens_intro = Label(intens_frame, text='INTENSITY :', font=('Segoe UI sans serif', 15, 'bold'), bg='#D2D8D9')
lights_intens_intro.grid(row=1, column=0, pady=5)

lights_intens = Label(intens_frame, textvariable=intens, font=('Segoe UI sans serif', 15, 'bold'), bg='#D2D8D9')
lights_intens.grid(row=1, column=1)


min_intens_btn = Button(intens_frame, text='LOW', bg='#111E26', fg='#D3D6DB', font=('Segoe UI sans serif', 13, 'bold'), command=lambda: set_intens_low(intens))
min_intens_btn.grid(row=2, column=0, padx=10)

def set_intens_low(intens):
    intens.set('LOW')
    min_intens_btn.config(bg='#B6A999', fg='#4F4537')


mid_intens_btn = Button(intens_frame, text='MID', bg='#111E26', fg='#D3D6DB', font=('Segoe UI sans serif', 13, 'bold'), command=lambda: set_intens_low(intens))
mid_intens_btn.grid(row=2, column=1, padx=10)


high_intens_btn = Button(intens_frame, text='HIGH', bg='#111E26', fg='#D3D6DB', font=('Segoe UI sans serif', 13, 'bold'), command=lambda: set_intens_low(intens))
high_intens_btn.grid(row=2, column=2, padx=10)


columns_root, rows_root = root.grid_size()
for i in range(columns_root):
    root.grid_columnconfigure(i, weight=1)

for i in range(rows_root):
    root.rowconfigure(i, weight=1)


# cols_lf, rows_lf = lights_frame.grid_size()
# for i in range(cols_lf):
#     lights_frame.grid_columnconfigure(i, weight=1)

# for i in range(rows_lf):
#     lights_frame.rowconfigure(i, weight=1)


root.mainloop()