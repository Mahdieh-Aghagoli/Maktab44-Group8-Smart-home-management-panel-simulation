class Room:
    def __init__(self, room_number):
        sensor = []
        self.sensor = sensor
        self.room_number = room_number

    def __str__(self):
        return "{}".format(self.sensor)

    def add_sensors(self, other):
        self.sensor.append(other)


