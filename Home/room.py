import logging
from IOT_Sensors import sensors


class Room:

    def __init__(self, room_number):
        """
        :param sensor: list of sensors in a room
        :param room_number: a specific number for each room of a house
        """
        logging.basicConfig(filename='IOT.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('Rooms and sensors!')

        sensor = []
        self.sensor = sensor
        self.room_number = room_number

    @property
    def __str__(self):
        try:
            return "{}".format(self.sensor)
        except TypeError:
            logging.basicConfig(filename='IOT.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                                level=logging.WARNING)
            logging.warning('write sth !')
            return ""

    def add_sensors(self, sensor):
        """
        get a sensor and add it to the room's sensors' list
        :param sensor:
        :param other:
        :return:
        """
        logging.basicConfig(filename='IOT.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('Added users!')

        self.sensor.append(sensor)

    @staticmethod
    def rooms_definition(number, num_of_sensors):
        logging.basicConfig(filename='IOT.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('Definition of rooms and number of rooms!')

        room = Room(number)

        for i in range(num_of_sensors):
            # here we should get sensors then use add_sensors function to finally have our room defined
            print("""Please select the type of sensor : 
                1)DarknessSensor
                2)Temperature
                3)SoundRemote
            """)

            sensor_type = input()

            if sensor_type == '1':
                sensor = "sensors.DarknessSensor(sensors.VoltageInput)"
                room.add_sensors(sensor)

            elif sensor_type == '2':
                sensor = "sensors.Temperature"
                room.add_sensors(sensor)

            elif sensor_type == '3':
                sensor = "sensors.SoundRemote()"
                room.add_sensors(sensor)

            else:
                print('no sensor')

        return room


# a = Room.rooms_definition(2, 3)
# print(a.sensor)