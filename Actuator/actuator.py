import random
from datetime import datetime

''' when sensors added, time, temperature and etc must import from sensors 
and i must add which actuator is doing a task for a specific sensor'''


class Actuator:
    time = datetime.now().hour

    def __init__(self, sensors, location, actuator_type):
        self.actuator_type = actuator_type
        self.sensors = sensors
        self.location = location

    def lights_on(self):
        pass

    '''i need a motivation sensor here cause if i want to turn the lights on, i need to know if someone came inside'''

    def boiler(self):
        temperature = random.randint(0, 100)
        if Actuator.time == 7 and temperature < 100:
            print("boiler activated")

    @staticmethod
    def pull_curtain():
        if Actuator.time == 7:
            print("c")

    def fire_extinguisher(self):
        pass

    '''need smoke sensor'''
