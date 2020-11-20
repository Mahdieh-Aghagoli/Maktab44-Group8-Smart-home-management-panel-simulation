import logging
import os
import random
# from random import shuffle
from datetime import datetime
from os import listdir
from os.path import isfile, join
import pygame


class Sensors:
    # rate_sensitivity = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sensor_type = ['sound_sensor', 'temperature_sensor', 'DarknessSensor']
    installation_located = ['radio', 'kettle', 'lamp']

    def __init__(self, rate_sensitivity):
        logging.basicConfig(filename='IOT.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info("Sensors information!")
        """sensor attributes for initializing """
        self.rate_sensitivity = rate_sensitivity
        self.sensor_type = []
        self.installation_located = []
        self.running = True

    def shuffle_rate_sensitivity(self):
        # return shuffle.rate_sensitivity  # Determine the sensitivity rate randomly
        self.rate_sensitivity = random.randint(0, 9)
        return self.rate_sensitivity


class DarknessSensor(Sensors):

    def __init__(self, rate_sensitivity, sensor_type, installation_located):
        """inheritance of Sensors class"""
        super().__init__(rate_sensitivity, sensor_type, installation_located)

    logging.basicConfig(filename='IOT.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                        level=logging.INFO)
    logging.info("Get information about Darkness sensor!")
    # Light level descriptions
    def shuffle_rate_sensitivity(self):
        # return shuffle.rate_sensitivity  # Determine the sensitivity rate randomly
        self.rate_sensitivity = random.randint(0, 9)
        return self.rate_sensitivity

    night = "extremely_dark"
    day = "normal"
    night_r = 1
    day_r = 10

    def measure_light(self):
        """Measuring the values of the light needed based on the voltage"""
        if self.shuffle_rate_sensitivity() == night_r:
            print("please active actuator {}".format(self.installation_located[2]))
        else:
            print("It is day")


class Temperature(Sensors):

    def __init__(self, rate_sensitivity, sensor_type, installation_located):
        """inheritance of Sensors class"""
        super().__init__(rate_sensitivity, sensor_type, installation_located)

    def shuffle_rate_sensitivity(self):
        self.rate_sensitivity = random.randint(0, 100)
        return self.rate_sensitivity  # Determine the sensitivity rate randomly

    def temp_control(self):
        if self.installation_located == self.installation_located[1]:
            if self.rate_sensitivity > 100 and datetime.now().hour:
                return True
            else:
                return False


class SoundRemote(Sensors):

    def __init__(self, rate_sensitivity, sensor_type, installation_located):
        """inheritance of Sensors class"""
        super().__init__(rate_sensitivity, sensor_type, installation_located)

    def shuffle_rate_sensitivity(self):
        self.rate_sensitivity = random.randint(0, 100)
        return self.rate_sensitivity  # Determine the sensitivity rate randomly

    def temp_control(self):
        if self.installation_located == self.installation_located[0]:
            if self.rate_sensitivity > 100 and datetime.now().hour:
                return True
            else:
                return False

