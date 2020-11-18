class Home:
    def __init__(self,rooms, sensors, password):
        self.rooms = rooms
        self.sensors = sensors  # i think there is no need for this!
        self.password = password

    def __str__(self):
        return"""
        your rooms : {}
        sensors in your home : {}
        """.format(self.rooms, self.sensors)

    @staticmethod
    def home_definition():
        pass

    @staticmethod
    def home_db():
        file = r"home_info.txt"
        return file