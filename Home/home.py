class Home:
    def __init__(self, rooms, sensors, password):
        def __init__(self, room_number):
            logging.basicConfig(filename='IOT.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                                level=logging.INFO)
            logging.info('Rooms and sensors!')
        self.rooms = rooms
        self.sensors = sensors  # i think there is no need for this!
        self.password = password

    @property
    def __str__(self):
        return """
        your rooms : {}
        sensors in your home : {}
        """.format(self.rooms, self.sensors)
        logging.basicConfig(filename='IOT.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info(' !')

    @staticmethod
    def home_definition():
        pass

    @staticmethod
    def home_db():
        file = r"home_info.txt"
        return file
