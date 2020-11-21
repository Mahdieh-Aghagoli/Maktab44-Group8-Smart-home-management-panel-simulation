from tkinter import *
import csv

home_db = r'home.csv'


def fill_db(file_name, row):
    """
    to add users info to a csv file
    :param file_name:
    :param row:
    :return: nothing
    """
    with open(file_name, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(row)

        # writing the data rows
        # csvwriter.writerows()


def login():
    login_win = Toplevel(window)  # A Toplevel widget is used to create a window on top of all other windows
    # window.withdraw()
    # window.deiconify()

    login_win.title("Login")
    login_win.geometry('500x470')

    login_win.mainloop()


def sign_up():
    user_info = []

    # sign up window
    # to get the users password then add it to db
    def submission():
        password_get = password_entry.get()
        user_info.append(password_get)
        fill_db(home_db, user_info)


    sign_up_win = Toplevel(window)  # A Toplevel widget is used to create a window on top of all other windows
    sign_up_win.title("Login")
    sign_up_win.geometry('500x470')

    # sign up widgets
    password_label = Label(sign_up_win, text="Password", font=("Arial Bold", 15), fg='#063852', bg="#98DBC6")

    password = StringVar()  #gets string input
    password_entry = Entry(sign_up_win, show="*", textvariable=password)

    submit = Button(sign_up_win, text="Submit", command=submission, font=("Arial Bold", 12), bg="#D0E1F9", fg="#063852",
                    activebackground="#FFEB94", activeforeground='#063852')

    password_label.grid()
    password_entry.grid()

    submit.grid()
    sign_up_win.mainloop()


#main window
window = Tk()
window.title("Smart Home")
window.geometry('500x470')
window.configure(bg="#98DBC6")
window.iconphoto(False, PhotoImage(file='homeIcon.png'))

# window.resizable(0, 0)

# widgets of main window
name = Label(window, text="Smart Home Panel", font=("Arial Bold", 25), fg='#063852', bg="#98DBC6")

photo = PhotoImage(file='well.gif')
img = Label(window, image=photo)

login_button = Button(window, text='Login', command=login, font=("Arial Bold", 12),

                      bg="#D0E1F9", fg="#063852", activebackground="#FFEB94", activeforeground='#063852')

signup_button = Button(window, text='Sign Up', command=sign_up, font=("Arial Bold", 12),
                       bg="#C1E1DC", fg="#063852", activebackground="#FFEB94", activeforeground='#063852')

name.grid()
img.grid()
signup_button.grid()
login_button.grid()

window.mainloop()
