from tkinter import *

# Main window
root = Tk()
root.geometry("750x500")
root.title("DomotiQue")
root.config(bg="#111E26")

# Rooms Frame Section
## Room Wrapper / Frame
rooms_frame = Frame(root, width=100, height=50, bg="#111E26")
rooms_frame.grid(row=0, column=0)

### Hover State Function for Rooms Options
def hover_state_rooms_opt(event):
    rooms_opt.itemconfig(ACTIVE, {'bg': '#0D151C', 'fg' : '#D3D6DB'})
    index = rooms_opt.nearest(event.y)

    if rooms_opt.get(index) != '':
        rooms_opt.itemconfig(index, {'bg' : '#2D3340'})
    else:
        rooms_opt.itemconfig(index, {'bg' : '#0D151C'})

    rooms_opt.activate(index)

### Select State Function for Rooms Options
def select_state_rooms_opt(event):
    pos_rooms_opt_tup = rooms_opt.curselection()
    pos_opt = pos_rooms_opt_tup[0]
    opt = rooms_opt.get(pos_opt)

    if opt.strip() != '':
        rooms_opt.itemconfig(pos_opt, selectbackground="#033F4D")
    else:
        rooms_opt.itemconfig(pos_opt, selectbackground='#0D151C')
    
### Leave State Function for Rooms Options
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

## Listbox for Rooms Options
rooms_opt = Listbox(rooms_frame, selectmode=SINGLE, bg="#0D151C", fg="#D3D6DB", font=("Segoe UI", 12, 'bold'), justify='center', highlightthickness=0, borderwidth=0, selectbackground="#033F4D", exportselection=False)
rooms_opt.bind('<Motion>', hover_state_rooms_opt)
rooms_opt.bind('<<ListboxSelect>>', select_state_rooms_opt)
rooms_opt.bind('<Leave>', leave_state_rooms_opt)
rooms_opt.grid(row=1, column=0)

### Inserting Rooms Options
rooms_opt.insert(END, '')
rooms_opt.insert(END, '')
rooms_opt.insert(END, 'Kitchen')
rooms_opt.insert(END, '')
rooms_opt.insert(END, 'Bedroom')
rooms_opt.insert(END, '')
rooms_opt.insert(END, 'Toilet')
rooms_opt.insert(END, '')

# Objects Frame Section
## Objects Frame
objs_frame = Frame(root, width=50, height=50)
objs_frame.grid(row=0, column=1)

### Hover State Function for Objects Options
def hover_state_objs_opt(event):
    objs_opt.itemconfig(ACTIVE, {'bg': '#0D151C', 'fg' : '#D3D6DB'})

    index = objs_opt.nearest(event.y)
    if objs_opt.get(index) != '':
        objs_opt.itemconfig(index, {'bg' : '#2D3340'})
    else:
        objs_opt.itemconfig(index, {'bg' : '#0D151C'})

    objs_opt.activate(index)

### Select State Function for Objects Options
def select_state_objs_opt(event):
    pos_objs_opt_tup = objs_opt.curselection()
    pos_opt = pos_objs_opt_tup[0]
    opt = objs_opt.get(pos_opt)

    if opt.strip() != '':
        objs_opt.itemconfig(pos_opt, selectbackground='#033F4D')
    else:
        objs_opt.itemconfig(pos_opt, selectbackground='#0D151C')

### Leave State Function for Objects Options
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
        

## Listbox for Objects Options
objs_opt = Listbox(objs_frame, selectmode=SINGLE, highlightthickness=0, borderwidth=0, justify='center', font=("Segoe UI", 12, "bold"), fg="#D3D6DB", bg="#0D151C", exportselection=False, )
objs_opt.bind('<Motion>', hover_state_objs_opt)
objs_opt.bind('<<ListboxSelect>>', select_state_objs_opt)
objs_opt.bind('<Leave>', leave_state_objs_opt)
objs_opt.grid(row=0, column=0)

### Inserting Objects Options
objs_opt.insert(END, '')
objs_opt.insert(END, '')
objs_opt.insert(END, '')
objs_opt.insert(END, 'Radiator')
objs_opt.insert(END, '')
objs_opt.insert(END, 'Lights')
# objs_opt.insert(END, '')

# Lights Frame Section
## Lights Wrapper/ Frame
lights_frame = Frame(root, width=30, height=50, background='#2F4858')
lights_frame.grid(row=0, column=2)

## Lights State Frame
lights_state_frame = Frame(lights_frame, bg='#111E26', borderwidth=1)
lights_state_frame.grid(row=0, column=0, pady=15)

## Lights State Label
lights_state_intro = Label(lights_state_frame, text='STATE :', font=('Segoe UI sans serif', 14, 'bold'), bg='#111E26', fg='#D3D6DB')
lights_state_intro.grid(row=0, column=0)

## Lights State Value
state = StringVar()
state.set("ON")
lights_state = Label(lights_state_frame, textvariable=state, font=('Segoe UI sans serif', 14, 'bold'), bg='#00C59F', fg='#364B44')
lights_state.grid(row=0, column=1, padx=5, pady=5)

## Light Switch Button
switch = StringVar()
switch.set('OFF')
def light_switch_enter(event):
    light_switch_btn.config(bg='#B1BDC5')
def light_switch_leave(event):
    light_switch_btn.config(bg='white')

light_switch_btn = Button(lights_state_frame, textvariable= switch, width=10, height=1, font=('Segoe UI sans serif', 15, 'bold'), command=lambda:switch_act(), activebackground='#B1BDC5')
light_switch_btn.bind('<Enter>', light_switch_enter)
light_switch_btn.bind('<Leave>', light_switch_leave)
light_switch_btn.grid(row=1, column=0, sticky='ew', columnspan=2)

### Function for Light Switch Action
def switch_act():
    if switch.get() == 'OFF' and state.get() == 'ON':
        switch.set('ON')
        lights_state.config(bg='#C41200', fg='#FFE6D8')
        state.set('OFF')
    elif switch.get() == 'ON' and state.get() == 'OFF':
        switch.set('OFF')
        lights_state.config(bg='#00C59F', fg='#364B44')
        state.set('ON')

## Lights Intensity Value
intens = StringVar()
intens.set('LOW')

## Lights Intensity Frame
intens_frame = Frame(lights_frame, background='#2F4858')
intens_frame.grid(row=2, column=0)

## Lights Intensity Label Frame
lights_intens_label_frame = Frame(intens_frame, bg='#111E26')
lights_intens_label_frame.grid(row=0, column=1, pady=15)

## Lights Intensity Label
lights_intens_intro = Label(lights_intens_label_frame, text='BRIGHTNESS :', font=('Segoe UI sans serif', 14, 'bold'), bg='#111E26', fg='#D3D6DB')
lights_intens_intro.grid(row=0, column=0, padx=(10, 2), pady=7)


lights_intens = Label(lights_intens_label_frame, textvariable=intens, font=('Segoe UI sans serif', 13, 'bold'), bg='#D2D8D9')
lights_intens.grid(row=0, column=1, padx=(2,10), ipady=1)

### Checking if Intensity buttons have been clicked
min_clicked = mid_clicked = high_clicked = False

## Button for Minimum Intensity
def min_enter(event):
    global min_clicked
    if not min_clicked:
        min_intens_btn.config(bg='#014853', fg='#D3D6DB')

def min_leave(event):
    global min_clicked
    if not min_clicked:
        min_intens_btn.config(bg='#111E26', fg='#D3D6DB')
min_intens_btn = Button(intens_frame, text='LOW', bg='#111E26', fg='#D3D6DB', font=('Segoe UI sans serif', 13, 'bold'), activeforeground='#D3D6DB', activebackground='#014853', command=lambda: set_intens_low(intens))
min_intens_btn.bind('<Enter>', min_enter)
min_intens_btn.bind('<Leave>', min_leave)
min_intens_btn.grid(row=2, column=0, padx=10)

### Function for Setting Intensity to Low
def set_intens_low(intens):
    intens.set('LOW')
    global min_clicked, mid_clicked, high_clicked
    min_clicked = True
    mid_clicked = False
    high_clicked = False
    min_intens_btn.config(bg='#B6A999', fg='#4F4537')
    mid_intens_btn.config(bg='#111E26', fg='#D3D6DB')
    high_intens_btn.config(bg='#111E26', fg='#D3D6DB')

## Button for Medium Intensity
def mid_enter(event):
    global mid_clicked
    if not mid_clicked:
        mid_intens_btn.config(bg='#014853', fg='#D3D6DB')

def mid_leave(event):
    global mid_clicked
    if not mid_clicked:
        mid_intens_btn.config(bg='#111E26', fg='#D3D6DB')

def set_intens_mid(intens):
    intens.set('MID')
    global min_clicked, mid_clicked, high_clicked
    min_clicked = False
    mid_clicked = True
    high_clicked = False
    mid_intens_btn.config(bg='#B6A999', fg='#4F4537')
    min_intens_btn.config(bg='#111E26', fg='#D3D6DB')
    high_intens_btn.config(bg='#111E26', fg='#D3D6DB')

mid_intens_btn = Button(intens_frame, text='MID', bg='#111E26', fg='#D3D6DB', font=('Segoe UI sans serif', 13, 'bold'), activeforeground='#D3D6DB', activebackground='#014853', command=lambda: set_intens_mid(intens))
mid_intens_btn.bind('<Enter>', mid_enter)
mid_intens_btn.bind('<Leave>', mid_leave)
mid_intens_btn.grid(row=2, column=1, padx=10)


### Function for Setting Intensity to Mid


## Button for High Intensity
def high_enter(event):
    global high_clicked
    if not high_clicked:
        high_intens_btn.config(bg='#014853', fg='#D3D6DB')

def high_leave(event):
    global high_clicked
    if not high_clicked:
        high_intens_btn.config(bg='#111E26', fg='#D3D6DB')

### Function for Setting Intensity to High
def set_intens_high(intens):
    intens.set('HIGH')
    global min_clicked, mid_clicked, high_clicked
    min_clicked = False
    mid_clicked = False
    high_clicked = True
    high_intens_btn.config(bg='#B6A999', fg='#4F4537')
    min_intens_btn.config(bg='#111E26', fg='#D3D6DB')
    mid_intens_btn.config(bg='#111E26', fg='#D3D6DB')

high_intens_btn = Button(intens_frame, text='HIGH', bg='#111E26', fg='#D3D6DB', font=('Segoe UI sans serif', 13, 'bold'), activeforeground='#D3D6DB', activebackground='#014853', command=lambda: set_intens_high(intens))
high_intens_btn.grid(row=2, column=2, padx=10, pady=15)
high_intens_btn.bind('<Enter>', high_enter)
high_intens_btn.bind('<Leave>', high_leave)

# Configuring grid weights
columns_root, rows_root = root.grid_size()
for i in range(columns_root):
    root.grid_columnconfigure(i, weight=1)

for i in range(rows_root):
    root.rowconfigure(i, weight=1)

root.mainloop()