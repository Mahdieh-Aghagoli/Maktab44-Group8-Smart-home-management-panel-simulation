from Home import home
import csv
from hashlib import sha256


def menu():
    print(
        """
        What do you want to do?
        1)sign up
        2)login    
        """)

    user_choice = int(input())

    if user_choice == 1:
        sign_up()

    elif user_choice == 2:
        login()

    else:
        print("no operation")


def sign_up():
    new_home = home.Home.home_definition()
    password = sha256(new_home.password.encode()).hexdigest()
    write_in_db(password, new_home.sensors, new_home.rooms)


def write_in_db(*args):
    db_file = r'Home\home_db.csv'
    row = [args]

    # writing to csv file
    with open(db_file, 'a') as csv_file:
        # creating a csv writer object
        csv_writer = csv.writer(csv_file)
        # writing the data rows
        csv_writer.writerows(row)


def login():
    password = input("Please enter your password : ")
    db_file = r'Home\home_db.csv'

    if is_exist(password, db_file):
        with open(db_file, 'r') as csv_file:
            # creating a csv reader object
            csv_reader = csv.reader(csv_file)

            for row in csv_reader:
                for elem in range(len(row)):
                    if elem == 0:
                        pass
                    else:
                        print(row[elem])
    else:
        print("password didn't match!")


def is_exist(password, db_file):
    # reading csv file
    pass_hash = sha256(password.encode()).hexdigest()
    with open(db_file, 'r') as csv_file:
        # creating a csv reader object
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            if row[0] == pass_hash:
                return True
            else:
                return False



def main():
    while True:
        pass
sign_up()
login()