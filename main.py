from tkinter import *

# Main window
root = Tk()
root.geometry("980x600")
root.title("DomotiQue")
root.config(bg="#111E26")

rooms_obj_dict = {
    'Kitchen':{
        'Radiator': {
            'State' : 'ON',
            'Temperature' : 20 
        },
        'Lights' : {
            'State' : 'ON',
            'Brightness' : 'LOW'
        }
    },
    'Bedroom':{
        'Radiator': {
            'State' : 'ON',
            'Temperature' : 20 
        },
        'Lights' : {
            'State' : 'ON',
            'Brightness' : 'LOW'
        }
    },
    'Toilet':{
        'Radiator': {
            'State' : 'ON',
            'Temperature' : 20 
        },
        'Lights' : {
            'State' : 'ON',
            'Brightness' : 'LOW'
        }
    }
}

global Line

## Return Button
def return_home():
    if rooms_frame.winfo_viewable():
        rooms_frame.grid_remove()
    if objs_frame.winfo_viewable():
        objs_frame.grid_remove()
    if rad_frame.winfo_viewable():
        rad_frame.grid_remove()
    if lights_frame.winfo_viewable():
        lights_frame.grid_remove()
    
    return_btn.grid_remove()
    wel_lab.grid(row=0, column=0, columnspan=3)
    wel_lab_btn.grid(row=1, column=0, columnspan=3)


def enter_state(event):
    return_btn.config(bg="#273339")

def leave_state(event):
    return_btn.config(bg='#39454B')

return_btn = Button(root, width=25, height=0, text="RETURN TO HOMEPAGE", font=("Archivo Black", 10, 'bold'), command=lambda: return_home(), justify='center', bg="#39454B", fg='#E9EBEE')

return_btn.bind('<Enter>', enter_state)
return_btn.bind('<Leave>', leave_state)

# Welcome Screen
wel_lab = Label(root, text='WELCOME TO DOMOTIQUE.\n CLICK START TO BEGIN!', font=('Segoe UI sans serif', 13, 'bold'), bg='#1E2C35', fg='#D7F0EB', justify='center')
wel_lab.grid(row=0, column=0)

def start():
    wel_lab.grid_remove()
    wel_lab_btn.grid_remove()
    return_btn.grid(row=0, column=0, pady=10)
    rooms_frame.grid(row=1, column=0)

def wel_lab_enter_state(event):
    wel_lab_btn.config(bg='#D0DEE7')

def wel_lab_leave_state(event):
    wel_lab_btn.config(bg='#ffffff')

wel_lab_btn = Button(root, text='START', font=('Segoe UI sans serif', 13, 'bold'), fg='#1E2C35', bg='#ffffff', activebackground='#D0DEE7', activeforeground='#1E2C35', command=lambda: start())
wel_lab_btn.bind('<Enter>', wel_lab_enter_state)
wel_lab_btn.bind('<Leave>', wel_lab_leave_state)
wel_lab_btn.grid(row=1, column=0)

# Rooms Frame Section
## Room Wrapper / Frame
rooms_frame = Frame(root, width=100, height=50, bg="#111E26")

## Rooms Label
rooms_lab = Label(rooms_frame, font=('Segoe UI sans serif', 13, 'bold'), text='ROOMS', bg='#303B4A', fg='#D7F0EB')
rooms_lab.grid(row=0, column=0, pady=10)

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
    pos_opt_room = pos_rooms_opt_tup[0]
    opt_room = rooms_opt.get(pos_opt_room)

    if opt_room.strip() != '':
        rooms_opt.itemconfig(pos_opt_room, selectbackground="#033F4D")
        if not objs_frame.winfo_viewable():
            return_btn.grid(row=0, column=0, columnspan=2)
            objs_frame.grid(row=1, column=1)

            columns, rows = root.grid_size()
            for i in range(columns):
                root.grid_columnconfigure(i, weight=1)

    else:
        rooms_opt.itemconfig(pos_opt_room, selectbackground='#0D151C')
    
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
objs_frame = Frame(root, width=50, height=50, bg='#111E26')

## Objects Label
objs_lab = Label(objs_frame, font=('Segoe UI sans serif', 13, 'bold'), text='OBJECTS', bg='#303B4A', fg='#D7F0EB')
objs_lab.grid(row=0, column=0, pady=10)

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
    pos_opt_obj = pos_objs_opt_tup[0]
    opt_obj = objs_opt.get(pos_opt_obj)

    pos_rooms_opt_tup = rooms_opt.curselection()
    pos_opt_room = pos_rooms_opt_tup[0]
    opt_room = rooms_opt.get(pos_opt_room)


    if opt_obj.strip() != '':
        global Line 
        Line = rooms_obj_dict[opt_room][opt_obj]
        objs_opt.itemconfig(pos_opt_obj, selectbackground='#033F4D')
        if opt_obj.strip() == 'Lights':
            if rad_frame.winfo_viewable:
                rad_frame.grid_remove()
            return_btn.grid(row=0, column=0, columnspan=3)
            lights_frame.grid(row=1, column=2)
            upd_frame.grid(row=2, column=1, pady=(0, 15))

            columns, rows = root.grid_size()
            for i in range(columns):
                root.grid_columnconfigure(i, weight=1)

        elif opt_obj.strip() == 'Radiator':
            if lights_frame.winfo_viewable():
                lights_frame.grid_remove()
            return_btn.grid(row=0, column=0, columnspan=3)
            rad_frame.grid(row=1, column=2)
            upd_frame.grid(row=2, column=1, pady=(0, 15))

            columns, rows = root.grid_size()
            for i in range(columns):
                root.grid_columnconfigure(i, weight=1)

        rad_state.set(Line['State'])
    else:
        objs_opt.itemconfig(pos_opt_obj, selectbackground='#0D151C')

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
objs_opt.grid(row=1, column=0)

### Inserting Objects Options
objs_opt.insert(END, '')
objs_opt.insert(END, '')
objs_opt.insert(END, '')
objs_opt.insert(END, 'Radiator')
objs_opt.insert(END, '')
objs_opt.insert(END, 'Lights')


# Radiator Frame Scetion
## Radiator Frame
rad_frame = Frame(root, width=30, height=50, bg='#2F4858')

## Radiator Label
rad_lab = Label(rad_frame, font=('Segoe UI sans serif', 13, 'bold'), text='RADIATOR CONTROL', bg='#1E2C35', fg='#D7F0EB')
rad_lab.grid(row=0, column=0, pady=10, padx=15)

## Radiator State Frame
rad_state_frame = Frame(rad_frame, bg='#111E26', borderwidth=1)
rad_state_frame.grid(row=1, column=0, pady=15)

## Radiator State Label
rad_state_intro = Label(rad_state_frame, text='STATE :', font=('Segoe UI sans serif', 14, 'bold'), bg='#111E26', fg='#D3D6DB')
rad_state_intro.grid(row=0, column=0)

## Radiator State Value
rad_state = StringVar()
rad_state.set("ON")
rad_state_lab = Label(rad_state_frame, textvariable=rad_state, font=('Segoe UI sans serif', 14, 'bold'), bg='#00C59F', fg='#364B44')
rad_state_lab.grid(row=0, column=1, padx=5, pady=5)

## Radiator Switch Button
rad_switch = StringVar()
rad_switch.set('OFF')
def rad_switch_enter(event):
    rad_switch_btn.config(bg='#B1BDC5')
def rad_switch_leave(event):
    rad_switch_btn.config(bg='white')

rad_switch_btn = Button(rad_state_frame, textvariable= rad_switch, width=10, height=1, font=('Segoe UI sans serif', 15, 'bold'), command=lambda:rad_switch_act(rooms_obj_dict), activebackground='#B1BDC5')
rad_switch_btn.bind('<Enter>', rad_switch_enter)
rad_switch_btn.bind('<Leave>', rad_switch_leave)
rad_switch_btn.grid(row=1, column=0, sticky='ew', columnspan=2)

### Function for Radiator Switch Action
def rad_switch_act(rooms_obj_dict):
    pos_objs_opt_tup = objs_opt.curselection()
    pos_opt_obj = pos_objs_opt_tup[0]
    opt_obj = objs_opt.get(pos_opt_obj)

    pos_rooms_opt_tup = rooms_opt.curselection()
    pos_opt_room = pos_rooms_opt_tup[0]
    opt_room = rooms_opt.get(pos_opt_room)

    print(opt_room)
    print(opt_obj)

    if opt_room in rooms_obj_dict and opt_obj :
        if rad_switch.get() == 'OFF' and rad_state.get() == 'ON' and rooms_obj_dict[opt_room][opt_obj]['State'] == 'ON' :
            rooms_obj_dict[opt_room][opt_obj]['State'] = 'OFF'
            obj_value = rooms_obj_dict[opt_room][opt_obj]['State']
            rad_state.set(obj_value)

            rad_switch.set('ON')
            rad_state_lab.config(bg='#C41200', fg='#FFE6D8')
            
            rad_min_btn.grid_remove()
            rad_plus_btn.grid_remove()
        elif rad_switch.get() == 'ON' and rad_state.get() == 'OFF' and rooms_obj_dict[opt_room][opt_obj]['State'] == 'OFF' :
            rooms_obj_dict[opt_room][opt_obj]['State'] = 'ON'
            obj_value = rooms_obj_dict[opt_room][opt_obj]['State']
            rad_state.set(obj_value)

            rad_switch.set('OFF')
            rad_state_lab.config(bg='#00C59F', fg='#364B44')

            rad_min_btn.grid(row=1, column=0, padx=5, pady=(10,0))
            rad_plus_btn.grid(row=1, column=2, padx=5, pady=(10,0))
        print(str(rooms_obj_dict[opt_room][opt_obj]['State']))

    # if opt_room in rooms_obj_dict and opt_obj in opt_room:
    #     obj_val = opt_room[opt_obj]
    #     if obj_val[state.get()] == 'OFF':
    #        obj_val[state.get()] = 'ON'


    if mes_lab.get(0) == 'NO UPDATES MADE!':
        mes_lab.delete(0)
        mes_lab.insert(END, '- ' + opt_room + ' ' + opt_obj + ' : ' + rad_state.get())
    else:
        mes_lab.insert(END, '- ' + opt_room + ' ' + opt_obj + ' : ' + rad_state.get())

## Radiator Control Frame
rad_ctrl_frame = Frame(rad_frame, width=30, height=50, borderwidth=0, highlightthickness=0, bg='#2F4858')
rad_ctrl_frame.grid(row=2, column=0, pady=10, padx=20)


## Temperature Label
rad_temp_label = Label(rad_ctrl_frame, text='TEMPERATRUE ', font=('Segoe UI sans serif', 13, 'bold'), bg='#111E26', fg='#D3D6DB')
rad_temp_label.grid(row=0, column=1)

## Temp Varaiable
temp = IntVar()
temp.set('20')

## Radiator Temperature
rad_temp_label = Label(rad_ctrl_frame, font=('Segoe UI sans serif', 19, 'bold'), width=6, height=2, textvariable=temp, justify='center')
rad_temp_label.grid(row=1, column=1, rowspan=2, padx=10, pady=13)


## Decrease Temperature Button
def rad_min_enter_state(event):
    rad_min_btn.config(bg='#B6C0C4')

def rad_min_leave_state(event):
    rad_min_btn.config(bg='#F1FBFF')

def decr_temp(temp):
    pos_objs_opt_tup = objs_opt.curselection()
    pos_opt_obj = pos_objs_opt_tup[0]
    opt_obj = objs_opt.get(pos_opt_obj)

    pos_rooms_opt_tup = rooms_opt.curselection()
    pos_opt_room = pos_rooms_opt_tup[0]
    opt_room = rooms_opt.get(pos_opt_room)

    temp_act = rooms_obj_dict[opt_room][opt_obj]['Temperature']
    if temp_act > 18:
        temp_act -= 1
        rooms_obj_dict[opt_room][opt_obj]['Temperature'] = temp_act
        temp.set(rooms_obj_dict[opt_room][opt_obj]['Temperature'])

        if mes_lab.get(0) == 'NO UPDATES MADE!':
            mes_lab.delete(0)
            mes_lab.insert(END, '- ' + opt_room + ' ' + opt_obj + ' : ' + str(temp_act) + '°')
        else:
            mes_lab.insert(END, '- ' + opt_room + ' ' + opt_obj + ' : ' + str(temp_act) + '°')

rad_min_btn = Button(rad_ctrl_frame, width=2, height=1, font=('Archivo Black', 15, 'bold'), text='-', bg='#F1FBFF', fg='#2A3235', activebackground='#B6C0C4', command=lambda: decr_temp(temp))
rad_min_btn.grid(row=1, column=0, padx=5, pady=(10,0))
rad_min_btn.bind('<Enter>', rad_min_enter_state)
rad_min_btn.bind('<Leave>', rad_min_leave_state)


## Increase Temperature Button
def rad_plus_enter_state(event):
    rad_plus_btn.config(bg='#B6C0C4')

def rad_plus_leave_state(event):
    rad_plus_btn.config(bg='#F1FBFF')

def incr_temp(temp):
    pos_objs_opt_tup = objs_opt.curselection()
    pos_opt_obj = pos_objs_opt_tup[0]
    opt_obj = objs_opt.get(pos_opt_obj)

    pos_rooms_opt_tup = rooms_opt.curselection()
    pos_opt_room = pos_rooms_opt_tup[0]
    opt_room = rooms_opt.get(pos_opt_room)

    temp_act = rooms_obj_dict[opt_room][opt_obj]['Temperature']

    if temp_act < 40:
        temp_act += 1
        rooms_obj_dict[opt_room][opt_obj]['Temperature'] = temp_act
        temp.set(rooms_obj_dict[opt_room][opt_obj]['Temperature'])
        if mes_lab.get(0) == 'NO UPDATES MADE!':
            mes_lab.delete(0)
            mes_lab.insert(END, '- ' + opt_room + ' ' + opt_obj + ' : ' + str(temp_act) + '°')
        else:
            mes_lab.insert(END, '- ' + opt_room + ' ' + opt_obj + ' : ' + str(temp_act) + '°')
        

rad_plus_btn = Button(rad_ctrl_frame, width=2, height=0, font=('Archivo Black', 15, 'bold'), text='+', bg='#F1FBFF', fg='#2A3235', activebackground='#B6C0C4', command=lambda: incr_temp(temp))
rad_plus_btn.grid(row=1, column=2, padx=5, pady=(10,0))
rad_plus_btn.bind('<Enter>', rad_plus_enter_state)
rad_plus_btn.bind('<Leave>', rad_plus_leave_state)

upd_room_rad = Button(rad_frame, text='UPDATE ROOM', font=('Segoe UI sans serif', 13, 'bold'), activebackground='#C68226', bg='#039590', fg='#DBE8E6', command=lambda:update_room_rad())
upd_room_rad.grid(row=3, column=0, pady=15)

def update_room_rad():
    pos_objs_opt_tup = objs_opt.curselection()
    pos_opt_obj = pos_objs_opt_tup[0]
    opt_obj = objs_opt.get(pos_opt_obj)

    pos_rooms_opt_tup = rooms_opt.curselection()
    pos_opt_room = pos_rooms_opt_tup[0]
    opt_room = rooms_opt.get(pos_opt_room)

    if opt_obj == 'Radiator':
        rad_state.set(rooms_obj_dict[opt_room][opt_obj]['State'])
        if rooms_obj_dict[opt_room]['Radiator']['State'] == 'ON':
            rad_switch.set('OFF')
        else:
            rad_switch.set('ON')
        temp.set(rooms_obj_dict[opt_room]['Radiator']['Temperature'])

# Lights Frame Section
## Lights Wrapper/ Frame
lights_frame = Frame(root, width=30, height=50, bg='#2F4858')

## Lights Label
lights_lab = Label(lights_frame, font=('Segoe UI sans serif', 13, 'bold'), text='LIGHTS CONTROL', bg='#1E2C35', fg='#D7F0EB')
lights_lab.grid(row=0, column=0, pady=10)

## Lights State Frame
lights_state_frame = Frame(lights_frame, bg='#111E26', borderwidth=1)
lights_state_frame.grid(row=1, column=0, pady=15)

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

light_switch_btn = Button(lights_state_frame, textvariable= switch, width=10, height=1, font=('Segoe UI sans serif', 15, 'bold'), command=lambda:light_switch_act(), activebackground='#B1BDC5')
light_switch_btn.bind('<Enter>', light_switch_enter)
light_switch_btn.bind('<Leave>', light_switch_leave)
light_switch_btn.grid(row=1, column=0, sticky='ew', columnspan=2)

### Function for Light Switch Action
def light_switch_act():
    pos_objs_opt_tup = objs_opt.curselection()
    pos_opt_obj = pos_objs_opt_tup[0]
    opt_obj = objs_opt.get(pos_opt_obj)

    pos_rooms_opt_tup = rooms_opt.curselection()
    pos_opt_room = pos_rooms_opt_tup[0]
    opt_room = rooms_opt.get(pos_opt_room)

    if opt_room in rooms_obj_dict and opt_obj :
        if switch.get() == 'OFF' and state.get() == 'ON' and rooms_obj_dict[opt_room][opt_obj]['State'] == 'ON' :

            rooms_obj_dict[opt_room][opt_obj]['State'] = 'OFF'
            obj_value = rooms_obj_dict[opt_room][opt_obj]['State']
            state.set(obj_value)

            lights_state.config(bg='#C41200', fg='#FFE6D8')
            switch.set('ON')
            min_intens_btn.grid_remove()
            mid_intens_btn.grid_remove()
            high_intens_btn.grid_remove()

        elif switch.get() == 'ON' and state.get() == 'OFF' and rooms_obj_dict[opt_room][opt_obj]['State'] == 'OFF' :
            rooms_obj_dict[opt_room][opt_obj]['State'] = 'ON'
            obj_value = rooms_obj_dict[opt_room][opt_obj]['State']
            state.set(obj_value)            
            
            lights_state.config(bg='#00C59F', fg='#364B44')
            switch.set('OFF')
            min_intens_btn.grid(row=2, column=0, padx=10)
            mid_intens_btn.grid(row=2, column=1, padx=10)
            high_intens_btn.grid(row=2, column=2, padx=10, pady=15)

    if mes_lab.get(0) == 'NO UPDATES MADE!':
        mes_lab.delete(0)
        mes_lab.insert(END, '- ' + opt_room + ' ' + opt_obj + ' : ' + state.get())
    else:
        mes_lab.insert(END, '- ' + opt_room + ' ' + opt_obj + ' : ' + state.get())

## Lights Brightness Value
intens = StringVar()
intens.set('LOW')

## Lights Brightness Frame
intens_frame = Frame(lights_frame, bg='#2F4858')
intens_frame.grid(row=2, column=0)

## Lights Brightness Label Frame
lights_intens_label_frame = Frame(intens_frame, bg='#111E26')
lights_intens_label_frame.grid(row=0, column=1, pady=15, padx=15)

## Lights Brightness Label
lights_intens_intro = Label(lights_intens_label_frame, text='BRIGHTNESS :', font=('Segoe UI sans serif', 14, 'bold'), bg='#111E26', fg='#D3D6DB')
lights_intens_intro.grid(row=0, column=0, padx=(10, 2), pady=7)


lights_intens = Label(lights_intens_label_frame, textvariable=intens, font=('Segoe UI sans serif', 13, 'bold'), bg='#D2D8D9')
lights_intens.grid(row=0, column=1, padx=(2,10), ipady=1)

### Checking if Brightness buttons have been clicked
min_clicked = mid_clicked = high_clicked = False

## Button for Minimum Brightness
def min_enter(event):
    global min_clicked
    if not min_clicked:
        min_intens_btn.config(bg='#1C4B63', fg='#D3D6DB')

def min_leave(event):
    global min_clicked
    if not min_clicked:
        min_intens_btn.config(bg='#111E26', fg='#D3D6DB')
min_intens_btn = Button(intens_frame, text='LOW', bg='#111E26', fg='#D3D6DB', font=('Segoe UI sans serif', 13, 'bold'), activeforeground='#D3D6DB', activebackground='#014853', command=lambda: set_intens_low(intens))
min_intens_btn.bind('<Enter>', min_enter)
min_intens_btn.bind('<Leave>', min_leave)
min_intens_btn.grid(row=2, column=0, padx=10)

### Function for Setting Brightness to Low
def set_intens_low(intens):
    pos_objs_opt_tup = objs_opt.curselection()
    pos_opt = pos_objs_opt_tup[0]
    opt_obj = objs_opt.get(pos_opt)

    pos_rooms_opt_tup = rooms_opt.curselection()
    pos_opt = pos_rooms_opt_tup[0]
    opt_room = rooms_opt.get(pos_opt)

    rooms_obj_dict[opt_room][opt_obj]['Brightness'] = 'LOW'
    obj_value = rooms_obj_dict[opt_room][opt_obj]['Brightness']
    intens.set(obj_value)

    global min_clicked, mid_clicked, high_clicked
    min_clicked = True
    mid_clicked = False
    high_clicked = False
    min_intens_btn.config(bg='#B6A999', fg='#4F4537')
    mid_intens_btn.config(bg='#111E26', fg='#D3D6DB')
    high_intens_btn.config(bg='#111E26', fg='#D3D6DB')

    if mes_lab.get(0) == 'NO UPDATES MADE!':
        mes_lab.delete(0)
        mes_lab.insert(END, '- ' + opt_room + ' ' + opt_obj + ', ' + 'BRIGHTNESS : LOW')
    else:
        mes_lab.insert(END, '- ' + opt_room + ' ' + opt_obj + ', ' + 'BRIGHTNESS : LOW')

## Button for Medium Brightness
def mid_enter(event):
    global mid_clicked
    if not mid_clicked:
        mid_intens_btn.config(bg='#1C4B63', fg='#D3D6DB')

def mid_leave(event):
    global mid_clicked
    if not mid_clicked:
        mid_intens_btn.config(bg='#111E26', fg='#D3D6DB')


### Function for Setting Brightness to Mid
def set_intens_mid(intens):
    pos_objs_opt_tup = objs_opt.curselection()
    pos_opt = pos_objs_opt_tup[0]
    opt_obj = objs_opt.get(pos_opt)

    pos_rooms_opt_tup = rooms_opt.curselection()
    pos_opt = pos_rooms_opt_tup[0]
    opt_room = rooms_opt.get(pos_opt)

    rooms_obj_dict[opt_room][opt_obj]['Brightness'] = 'MID'
    obj_value = rooms_obj_dict[opt_room][opt_obj]['Brightness']
    intens.set(obj_value)

    global min_clicked, mid_clicked, high_clicked
    min_clicked = False
    mid_clicked = True
    high_clicked = False
    mid_intens_btn.config(bg='#B6A999', fg='#4F4537')
    min_intens_btn.config(bg='#111E26', fg='#D3D6DB')
    high_intens_btn.config(bg='#111E26', fg='#D3D6DB')

    if mes_lab.get(0) == 'NO UPDATES MADE!':
        mes_lab.delete(0)
        mes_lab.insert(END, '- ' + opt_room + ' ' + opt_obj + ', ' + 'BRIGHTNESS : MID')
    else:
        mes_lab.insert(END, '- ' + opt_room + ' ' + opt_obj + ', ' + 'BRIGHTNESS : MID')

mid_intens_btn = Button(intens_frame, text='MID', bg='#111E26', fg='#D3D6DB', font=('Segoe UI sans serif', 13, 'bold'), activeforeground='#D3D6DB', activebackground='#014853', command=lambda: set_intens_mid(intens))
mid_intens_btn.bind('<Enter>', mid_enter)
mid_intens_btn.bind('<Leave>', mid_leave)
mid_intens_btn.grid(row=2, column=1, padx=10)


## Button for High Brightness
def high_enter(event):
    global high_clicked
    if not high_clicked:
        high_intens_btn.config(bg='#1C4B63', fg='#D3D6DB')

def high_leave(event):
    global high_clicked
    if not high_clicked:
        high_intens_btn.config(bg='#111E26', fg='#D3D6DB')

### Function for Setting Brightness to High
def set_intens_high(intens):
    pos_objs_opt_tup = objs_opt.curselection()
    pos_opt = pos_objs_opt_tup[0]
    opt_obj = objs_opt.get(pos_opt)

    pos_rooms_opt_tup = rooms_opt.curselection()
    pos_opt = pos_rooms_opt_tup[0]
    opt_room = rooms_opt.get(pos_opt)

    rooms_obj_dict[opt_room][opt_obj]['Brightness'] = 'HIGH'
    obj_value = rooms_obj_dict[opt_room][opt_obj]['Brightness']
    intens.set(obj_value)

    global min_clicked, mid_clicked, high_clicked
    min_clicked = False
    mid_clicked = False
    high_clicked = True
    high_intens_btn.config(bg='#B6A999', fg='#4F4537')
    min_intens_btn.config(bg='#111E26', fg='#D3D6DB')
    mid_intens_btn.config(bg='#111E26', fg='#D3D6DB')

    if mes_lab.get(0) == 'NO UPDATES MADE!':
        mes_lab.delete(0)
        mes_lab.insert(END, '- ' + opt_room + ' ' + opt_obj + ', ' + 'BRIGHTNESS : HIGH')
    else:
        mes_lab.insert(END, '- ' + opt_room + ' ' + opt_obj + ', ' + 'BRIGHTNESS : HIGH')

high_intens_btn = Button(intens_frame, text='HIGH', bg='#111E26', fg='#D3D6DB', font=('Segoe UI sans serif', 13, 'bold'), activeforeground='#D3D6DB', activebackground='#014853', command=lambda: set_intens_high(intens))
high_intens_btn.grid(row=2, column=2, padx=10, pady=15)
high_intens_btn.bind('<Enter>', high_enter)
high_intens_btn.bind('<Leave>', high_leave)

upd_room_light = Button(lights_frame, text='UPDATE ROOM', font=('Segoe UI sans serif', 13, 'bold'), activebackground='#C68226', bg='#039590', fg='#DBE8E6', command=lambda:update_room_lights())
upd_room_light.grid(row=3, column=0, pady=15)

def update_room_lights():
    pos_objs_opt_tup = objs_opt.curselection()
    pos_opt_obj = pos_objs_opt_tup[0]
    opt_obj = objs_opt.get(pos_opt_obj)

    pos_rooms_opt_tup = rooms_opt.curselection()
    pos_opt_room = pos_rooms_opt_tup[0]
    opt_room = rooms_opt.get(pos_opt_room)

    
    if opt_obj == 'Lights':
        state.set(rooms_obj_dict[opt_room][opt_obj]['State'])
        if rooms_obj_dict[opt_room]['Lights']['State'] == 'ON':
            switch.set('OFF')
        else:
            switch.set('ON')
        intens.set(rooms_obj_dict[opt_room]['Lights']['Brightness'])
    
    if rooms_obj_dict[opt_room]['Lights']['Brightness'] == 'LOW':
        min_intens_btn.config(bg='#B6A999', fg='#4F4537')
        mid_intens_btn.config(bg='#111E26', fg='#D3D6DB')
        high_intens_btn.config(bg='#111E26', fg='#D3D6DB')
    elif rooms_obj_dict[opt_room]['Lights']['Brightness'] == 'MID':
        mid_intens_btn.config(bg='#B6A999', fg='#4F4537')
        min_intens_btn.config(bg='#111E26', fg='#D3D6DB')
        high_intens_btn.config(bg='#111E26', fg='#D3D6DB')
    elif rooms_obj_dict[opt_room]['Lights']['Brightness'] == 'HIGH':
        high_intens_btn.config(bg='#B6A999', fg='#4F4537')
        min_intens_btn.config(bg='#111E26', fg='#D3D6DB')
        mid_intens_btn.config(bg='#111E26', fg='#D3D6DB')


upd_frame = Frame(root, width=30, height=50, borderwidth=0, highlightthickness=0, bg='#111E26')

upd_lab = Label(upd_frame, text='UPDATES', font=('Seoge UI sans serif', 13, 'bold'), bg='#303B4A', fg='#D7F0EB')
upd_lab.grid(row=0, column=0, pady=15)


def remove_select(event):
    list_size = mes_lab.size()
    pos_upd_sel_tup = mes_lab.curselection()

    if pos_upd_sel_tup:
        pos_up_sel = pos_upd_sel_tup[0]
        mes_lab.itemconfig(pos_up_sel, {'bg': '#98A0A4', 'fg' : '#111E26'})

mes_lab = Listbox(upd_frame, font=('Roboto Mono', 13, 'bold'), width=35, height=5, bg="#98A0A4", fg='#111E26', selectbackground='#98A0A4', selectforeground='#111E26', justify='center')
mes_lab.bind('<<Listboxselect>>', remove_select)
mes_lab.grid(row=1, column=0)

mes_lab.insert(END, 'NO UPDATES MADE!')

mes_lab_scroll = Scrollbar(upd_frame, orient='vertical', command=lambda:mes_lab.yview)
mes_lab_scroll.grid(row=1, column=1, sticky='ns')
mes_lab.config(yscrollcommand=mes_lab_scroll.set)

# Configuring grid weights
columns_root, rows_root = root.grid_size()
for i in range(columns_root):
    root.grid_columnconfigure(i, weight=1)

for i in range(rows_root):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()