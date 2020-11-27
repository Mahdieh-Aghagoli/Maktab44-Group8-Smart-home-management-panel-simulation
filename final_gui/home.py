import room
import csv
from hashlib import sha256


class Home:
    def __init__(self, rooms, sensors, password):
        """
        :param rooms: different rooms of the house
        :param sensors: different sensors in a specific house
        :param password: users password to check her house
        """
        self.rooms = rooms
        self.sensors = sensors  # i think there is no need for this!
        self.password = password

    def __str__(self):
        return """
        your rooms : {}
        sensors in your home : {}
        """.format(self.rooms, self.sensors)

    @staticmethod
    def home_definition():
        set_of_sensors = set()
        number_of_rooms = int(input("How many rooms do you want to have?"))
        password = input("Please enter a password : ")
        while Home.does_exist(password, Home.home_db()):
            print("Try with different info!")
            password = input("Please enter a password : ")

        rooms_of_house = {}

        for i in range(number_of_rooms):
            num_of_sensors = int(input("Please Enter the number of sensors for room {}: ".format(i + 1)))
            this_room = room.Room.rooms_definition(i, num_of_sensors)
            for item in this_room.sensor:
                set_of_sensors.add(item)
            rooms_of_house[i] = this_room

        return Home(rooms_of_house, set_of_sensors, password)

    @staticmethod
    def home_db():
        file = r"Home\home_db.csv"
        return file

    @staticmethod
    def sign_up():
        """
        :return: user can sign up and add her home to DB
        """
        # all this problems (in this case, again using the db_file location) are because of not having username (
        # specific email address) because it was not asked, and by having that in mind i coded this part and i didn't
        # wanted to change the code due to time limits
        db_file = Home.home_db()
        new_home = Home.home_definition()
        password = sha256(new_home.password.encode()).hexdigest()
        # if Home.does_exist(new_home.password, db_file):
        #     print("Try with different info!")
        #     Home.sign_up()
        # else:
        Home.write_in_db(password, new_home.sensors, new_home.rooms)

    @staticmethod
    def write_in_db(*args):
        db_file = Home.home_db()
        row = [args]

        # writing to csv file
        with open(db_file, 'a') as csv_file:
            # creating a csv writer object
            csv_writer = csv.writer(csv_file)
            # writing the data rows
            csv_writer.writerows(row)

    @staticmethod
    def login():
        '''
        :return: print the info of users home or if the does not exist it tells about it
        '''
        password = input("Please enter your password : ")
        db_file = Home.home_db()

        if Home.does_exist(password, db_file):
            with open(db_file, 'r') as csv_file:
                # creating a csv reader object
                csv_reader = csv.reader(csv_file)

                for row in csv_reader:
                    try:
                        if row[0] == sha256(password.encode()).hexdigest():
                            for elem in range(len(row)):
                                if elem == 0:
                                    pass
                                else:
                                    print(row[elem])
                    except IndexError:
                        pass
        else:
            print("password didn't match!")

    @staticmethod
    def does_exist(password, db_file):
        '''
        :param password: get password entered by user
        :param db_file: our simple .csv file
        :return: True if the password exists in .csv file
        '''
        pass_hash = sha256(password.encode()).hexdigest()

        # reading csv file
        with open(db_file, 'r') as csv_file:
            # creating a csv reader object
            csv_reader = csv.reader(csv_file)

            for row in csv_reader:
                try:
                    if row[0] == pass_hash:
                        return True
                except IndexError:
                    pass

# h = Home.home_definition()
# # room1 = h.rooms[0]
# # print(room1.sensor)
# hm = Home(1,2,3)
