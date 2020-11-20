from Home import room


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
        file = r"home_db.csv"
        return file


# h = Home.home_definition()
# room1 = h.rooms[0]
# print(room1.sensor)