class Room:
    def __init__(self, room_number):
        logging.basicConfig(filename='IOT.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('Rooms and sensors!')
        sensor = []
        self.sensor = sensor
        self.room_number = room_number

    def __str__(self):
        return "{}".format(self.sensor)

    def add_sensors(self, other):
        self.sensor.append(other)

    @staticmethod
    def rooms_definition(number, num_of_sensors):
        logging.basicConfig(filename='IOT.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('Definition of rooms and number of rooms!')
        room = Room(number)

        for i in range(num_of_sensors):
            pass  # here we should get sensors then use add_sensors function to finally have our room defined

        return room
