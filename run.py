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
        home.Home.sign_up()

    elif user_choice == 2:
        home.Home.login()

    else:
        print("no operation")


menu()




















# def sign_up():
#     """
#     :return: user can sign up and add her home to DB
#     """
#     # all this problems (in this case, again using the db_file location) are because of not having username (
#     # specific email address) because it was not asked, and by having that in mind i coded this part and i didn't
#     # wanted to change the code due to time limits
#     db_file = r'Home\home_db.csv'
#     new_home = home.Home.home_definition()
#     password = sha256(new_home.password.encode()).hexdigest()
#     if is_exist(new_home.password, db_file):
#         print("Try with different info!")
#         sign_up()
#     else:
#         write_in_db(password, new_home.sensors, new_home.rooms)
#
#
# def write_in_db(*args):
#     db_file = r'Home\home_db.csv'
#     row = [args]
#
#     # writing to csv file
#     with open(db_file, 'a') as csv_file:
#         # creating a csv writer object
#         csv_writer = csv.writer(csv_file)
#         # writing the data rows
#         csv_writer.writerows(row)
#
#
# def login():
#     '''
#     :return: print the info of users home or if the does not exist it tells about it
#     '''
#     password = input("Please enter your password : ")
#     db_file = r'Home\home_db.csv'
#
#     if is_exist(password, db_file):
#         with open(db_file, 'r') as csv_file:
#             # creating a csv reader object
#             csv_reader = csv.reader(csv_file)
#
#             for row in csv_reader:
#                 for elem in range(len(row)):
#                     if elem == 0:
#                         pass
#                     else:
#                         print(row[elem])
#     else:
#         print("password didn't match!")
#
#
# def is_exist(password, db_file):
#     '''
#     :param password: get password entered by user
#     :param db_file: our simple .csv file
#     :return: True if the password exists in .csv file
#     '''
#     pass_hash = sha256(password.encode()).hexdigest()
#
#     # reading csv file
#     with open(db_file, 'r') as csv_file:
#         # creating a csv reader object
#         csv_reader = csv.reader(csv_file)
#
#         for row in csv_reader:
#             try:
#                 if row[0] == pass_hash:
#                     return True
#             except IndexError:
#                 pass
#
#
# def main():
#     while True:
#         pass
#
# menu()
# sign_up()
# login()
# is_exist('2020', r'Home\home_db.csv')
