from Home import room


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
        pass

    elif user_choice == 2:
        pass

    else:
        print("no operation")


def sign_up():
    pass
