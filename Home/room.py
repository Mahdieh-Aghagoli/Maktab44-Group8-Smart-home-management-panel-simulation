class Room:
    def __init__(self, room_number):
        sensor = []
        self.sensor = sensor
        self.room_number = room_number

    def __str__(self):
        return "{}".format(self.sensor)

    def add_sensors(self, other):
        self.sensor.append(other)

    @staticmethod
    def rooms_definition(number, num_of_sensors):
        room = Room(number)

        for i in range(num_of_sensors):
            pass  # here we should get sensors then use add_sensors function to finally have our room defined

        return room
