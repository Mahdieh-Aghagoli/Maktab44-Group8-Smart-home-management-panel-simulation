from Home import home
from Home import room
import csv
from hashlib import sha256


def login():
    user_name = input("Please enter your name : ")
    password = input("Please enter your password : ")


# def rooms_definition():
#     pass


# def home_definition():
#     pass


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




def main():
    while True:
        pass
