from tkinter import *
from tkinter import ttk
import csv
import home
import room
from hashlib import sha256
from tkinter import messagebox
import tkinter.scrolledtext as st

home_db = r'home.csv'


def fill_db(file_name, row):
    with open(file_name, 'a') as csv_file:
        # creating a csv writer object
        csv_writer = csv.writer(csv_file)

        # writing the fields
        csv_writer.writerow(row)


def login():
    window.after(1000, window.destroy)
    login_win = Tk()  # A Toplevel widget is used to create a window on top of all other windows
    login_win.configure(bg="#98DBC6")
    login_win.title("Login")
    login_win.geometry('500x470')

    login_win.columnconfigure([0, 1], weight=1)

    # login_win.rowconfigure([0, 1, 2], weight=1)
    # frames
    username_lbl_frm = Frame(login_win, bg="#98DBC6")
    password_lbl_frm = Frame(login_win, bg="#98DBC6")
    username_ent_frm = Frame(login_win, bg="#98DBC6")
    password_ent_frm = Frame(login_win, bg="#98DBC6")
    submit_btn_frm = Frame(login_win, bg="#98DBC6")

    username_lbl_frm.grid(row=0, column=0)
    username_ent_frm.grid(row=0, column=1)
    password_lbl_frm.grid(row=1, column=0)
    password_ent_frm.grid(row=1, column=1)
    submit_btn_frm.grid(row=2, padx=5)

    def entrance():
        username_get = username_entry.get()  # get password from user
        password_get = password_entry.get()

        string = ''
        if home.Home.does_exist(username_get, home_db):  # to check if password exists in db or not
            with open(home_db, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    try:
                        if row[0] == sha256(username_get.encode()).hexdigest() and row[1] == sha256(
                                password_get.encode()).hexdigest():
                            string = string + username_get + '\n' * 2

                            find_room = row[2].strip('{}').split(sep=']')
                            # print(find_room)
                            for elem in find_room:
                                # room_dict[elem.split(sep=':')[0]] = elem.split(sep=':')[1]+']'
                                refind_key = elem.strip(' ,').split(sep=":")[0]
                                refind_val = elem.split(sep=":")[1] + ']'

                                string = string + "Room Number " + refind_key + ":" + "\n" + "\t"
                                # print(string)
                                string = string + refind_val + "\n" * 2
                    except IndexError:
                        pass

            login_win.after(1000, login_win.destroy)
            info_win = Tk()
            info_win.configure(bg="#98DBC6")
            info_win.title("Login")
            info_win.geometry('500x470')

            text_area = st.ScrolledText(info_win, width=55, height=10, font=("Times New Roman", 12))
            text_area.grid(row=0, column=0, pady=10, padx=10, ipadx=5)
            text_area.insert(INSERT, string)

            text_area.configure(state='disabled')

            info_win.mainloop()

        else:
            message = Toplevel(login_win)
            message.title("Wrong Information!")
            message.configure(bg="#98DBC6")
            message.geometry("200x100")
            msg = Message(message, text="Username Doesn't Exists", font=("Arial Bold", 10), bg="#98DBC6", anchor="ne")
            msg.pack()
            message.mainloop()

            # sign_up_win.after(2000, rooms)

    username_label = Label(username_lbl_frm, text="Username:", font=("Arial Bold", 12), fg='#063852', bg="#98DBC6")
    password_label = Label(password_lbl_frm, text="Password:", font=("Arial Bold", 12), fg='#063852', bg="#98DBC6")

    password = StringVar()
    username = StringVar()

    username_entry = Entry(username_ent_frm, textvariable=username, width=30)
    password_entry = Entry(password_ent_frm, show="*", textvariable=password, width=30)

    enter = Button(submit_btn_frm, text="Enter", command=entrance, font=("Arial Bold", 12), bg="#D0E1F9", fg="#063852",
                   activebackground="#FFEB94", activeforeground='#063852')

    username_label.grid(padx=10, pady=10)
    password_label.grid(padx=10, pady=10)

    username_entry.grid(padx=10, pady=10)
    password_entry.grid(padx=10, pady=10)

    enter.grid(padx=10, pady=10)

    login_win.mainloop()


def sign_up():
    window.after(1000, window.destroy)

    user_info = []

    # sign up window
    def submission():
        username_get = username_entry.get()  # get password from user
        password_get = password_entry.get()
        if home.Home.does_exist(username_get, home_db):  # to check if password exists in db or not
            # messagebox.showerror("error", "Username exists! Try another one.")
            message = Toplevel(sign_up_win)
            message.title("sign up Error!")
            message.configure(bg="#98DBC6")
            message.geometry("200x100")
            msg = Message(message, text="User name exists", font=("Arial Bold", 10), bg="#98DBC6", anchor="ne")
            msg.pack()
            message.mainloop()
            # n, ne, e, se, s, sw, w, nw, or center
        else:
            user_hash = sha256(username_get.encode()).hexdigest()
            user_info.append(user_hash)
            pass_hash = sha256(password_get.encode()).hexdigest()  # hash of password
            user_info.append(pass_hash)

            sign_up_win.after(2000, rooms)
        # print(user_info)
        # fill_db(home_db, user_info)

    def rooms():
        # destroy the previous window
        sign_up_win.destroy()
        rooms_of_home = []
        set_of_sensors = set()
        rooms_dict = {}

        def add_sensors():

            darkness_val_get = darkness_val.get()
            temp_val_get = temp_val.get()
            sound_val_get = sound_val.get()
            room_number_get = room_number.get()

            defined_room = room.Room(room_number_get)

            if darkness_val_get:
                defined_room.add_sensors("DarknessSensor")
                set_of_sensors.add("DarknessSensor")
            if temp_val_get:
                defined_room.add_sensors("TemperatureSensor")
                set_of_sensors.add("TemperatureSensor")
            if sound_val_get:
                defined_room.add_sensors("SoundSensor")
                set_of_sensors.add("SoundSensor")

            rooms_dict[room_number_get] = defined_room.sensor
            rooms_of_home.append(defined_room)
            print(rooms_dict)
            # print(rooms_of_home)

        def add_rooms():
            user_home = home.Home(rooms_of_home, rooms_of_home, user_info[1])
            # print(user_home)
            fill_db(home_db, [user_info[0], user_info[1], rooms_dict, user_home])

        # definition of new window
        definition_win = Tk()
        definition_win.title("Rooms")
        definition_win.geometry('500x470')
        definition_win.configure(bg="#98DBC6")

        definition_win.columnconfigure([0, 1], weight=1)
        definition_win.rowconfigure([0, 1, 2, 3], weight=1)
        # Frames
        sensor_lbl_frm = Frame(definition_win, bg="#98DBC6")
        room_num_lbl_frm = Frame(definition_win, bg="#98DBC6")
        room_num_ent_frm = Frame(definition_win, bg="#98DBC6")
        sensor_type_lbl_frm = Frame(definition_win, bg="#98DBC6")
        room_btn_frm = Frame(definition_win, bg="#98DBC6")
        home_btn_frm = Frame(definition_win, bg="#98DBC6")

        sensor_lbl_frm.grid(row=0, column=0)
        room_num_lbl_frm.grid(row=1, column=0)
        room_num_ent_frm.grid(row=1, column=1)
        sensor_type_lbl_frm.grid(row=2)
        room_btn_frm.grid(row=3, column=0)
        home_btn_frm.grid(row=3, column=1)


        # widgets
        sensor_label = Label(sensor_lbl_frm, text="Sensors : ", font=("Arial Bold", 15), fg='#063852', bg="#98DBC6")

        room_label = Label(room_num_lbl_frm, text="Room number : ", font=("Arial Bold", 9), fg='#063852', bg="#98DBC6")
        room_number = IntVar()
        room_entry = Entry(room_num_ent_frm, textvariable=room_number)

        darkness_val = BooleanVar()
        temp_val = BooleanVar()
        sound_val = BooleanVar()

        darkness_val.set(False)
        temp_val.set(False)
        sound_val.set(False)

        darkness = Checkbutton(sensor_type_lbl_frm, text="Darkness Sensor", var=darkness_val, font=("Arial Bold", 9),
                               bg="#98DBC6", activebackground="#FFEB94", activeforeground='#063852')
        temperature = Checkbutton(sensor_type_lbl_frm, text="Temperature Sensor", var=temp_val, font=("Arial Bold", 9),
                                  bg="#98DBC6", activebackground="#FFEB94", activeforeground='#063852')
        sound = Checkbutton(sensor_type_lbl_frm, text="Sound Sensor", var=sound_val, font=("Arial Bold", 9),
                            bg="#98DBC6", activebackground="#FFEB94", activeforeground='#063852')

        add_room = Button(room_btn_frm, text="Add Room", command=add_sensors, font=("Arial Bold", 12), bg="#D0E1F9",
                          fg="#063852",
                          activebackground="#FFEB94", activeforeground='#063852')

        add_home = Button(home_btn_frm, text="Add Home", command=add_rooms, font=("Arial Bold", 12), bg="#D0E1F9",
                          fg="#063852",
                          activebackground="#FFEB94", activeforeground='#063852')


        sensor_label.grid()
        room_label.grid()
        room_entry.grid()
        darkness.grid(row=0, column=0, padx=40, pady=10, sticky='W')
        temperature.grid(row=1, column=0, padx=40, pady=10, sticky='W')
        sound.grid(row=2, column=0, padx=40, pady=10, sticky='W')
        add_room.grid(padx=10, pady=10)
        add_home.grid(padx=10, pady=10)


        definition_win.mainloop()

    #
    # def user_home():
    #     pass

    # sign up window
    sign_up_win = Tk()  # A Toplevel widget is used to create a window on top of all other windows
    sign_up_win.title("Sign UP")
    sign_up_win.geometry('500x470')
    sign_up_win.configure(bg="#98DBC6")

    sign_up_win.columnconfigure([0, 1], weight=1)

    # sign_up_win.rowconfigure([0, 1, 2], weight=1)

    # frames
    username_lbl_frm = Frame(sign_up_win, bg="#98DBC6")
    password_lbl_frm = Frame(sign_up_win, bg="#98DBC6")
    username_ent_frm = Frame(sign_up_win, bg="#98DBC6")
    password_ent_frm = Frame(sign_up_win, bg="#98DBC6")
    submit_btn_frm = Frame(sign_up_win, bg="#98DBC6")

    username_lbl_frm.grid(row=0, column=0)
    username_ent_frm.grid(row=0, column=1)
    password_lbl_frm.grid(row=1, column=0)
    password_ent_frm.grid(row=1, column=1)
    submit_btn_frm.grid(row=2, padx=5)

    # sign up widgets
    username_label = Label(username_lbl_frm, text="Username:", font=("Arial Bold", 12), fg='#063852', bg="#98DBC6")
    password_label = Label(password_lbl_frm, text="Password:", font=("Arial Bold", 12), fg='#063852', bg="#98DBC6")

    password = StringVar()
    username = StringVar()

    username_entry = Entry(username_ent_frm, textvariable=username, width=30)
    password_entry = Entry(password_ent_frm, show="*", textvariable=password, width=30)

    submit = Button(submit_btn_frm, text="Submit", command=submission, font=("Arial Bold", 12), bg="#D0E1F9",
                    fg="#063852", activebackground="#FFEB94", activeforeground='#063852')

    username_label.grid(padx=10, pady=10)
    password_label.grid(padx=10, pady=10)

    username_entry.grid(padx=10, pady=10)
    password_entry.grid(padx=10, pady=10)

    submit.grid(padx=10, pady=10, sticky='w')
    sign_up_win.mainloop()


window = Tk()
window.title("Smart Home")
window.geometry('500x470')
window.configure(bg="#98DBC6")
window.iconphoto(False, PhotoImage(file='homeIcon.png'))

# window.resizable(0, 0)
name_frame = Frame(window, bg="#98DBC6")
name_frame.grid(row=0)

img_frame = Frame(window, bg="#98DBC6")
img_frame.grid(row=1)

sign_login_frame = Frame(window, bg="#98DBC6")
sign_login_frame.grid(row=2)

name = Label(name_frame, text="Smart Home Panel", font=("Arial Bold", 25), fg='#063852', bg="#98DBC6")

photo = PhotoImage(file='well.gif')
img = Label(img_frame, image=photo, bg="#98DBC6")

login_button = Button(sign_login_frame, text='Login', command=login, font=("Arial Bold", 12),

                      bg="#D0E1F9", fg="#063852", activebackground="#FFEB94", activeforeground='#063852')

signup_button = Button(sign_login_frame, text='Sign Up', command=sign_up, font=("Arial Bold", 12),
                       bg="#D0E1F9", fg="#063852", activebackground="#FFEB94", activeforeground='#063852')

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.rowconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.rowconfigure(2, weight=1)

name.pack()
img.pack(ipadx=5, padx=5, pady=5)
signup_button.grid(row=0, column=0, ipadx=20, padx=20, pady=2)
login_button.grid(row=0, column=1, ipadx=20, padx=20, pady=2)

window.mainloop()
