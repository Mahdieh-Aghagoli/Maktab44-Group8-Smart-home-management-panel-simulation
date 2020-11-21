import logging
import random
from datetime import datetime
from os import listdir
from os.path import isfile, join

import pygame
import os


class Sensors:
    rate_sensitivity_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sensor_type = ['sound_sensor', 'temperature_sensor', 'DarknessSensor']
    installation_located = ['radio', 'kettle', 'lamp']

    def __init__(self, type_of_sensor, location):
        logging.basicConfig(filename='IOT.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info("Sensors information!")

        """sensor attributes for initializing """
        self.rate_sensitivity = random.choice(Sensors.rate_sensitivity_list)
        self.type_of_sensor = type_of_sensor
        self.location = location
        self.running = True

    def shuffle_rate_sensitivity(self):
        # return shuffle.rate_sensitivity  # Determine the sensitivity rate randomly
        self.rate_sensitivity = random.choice(Sensors.rate_sensitivity_list)
        return self.rate_sensitivity


class DarknessSensor(Sensors):
    darkness = [1, 2, 3, 4]

    def __init__(self, location):
        """inheritance of Sensors class"""
        super().__init__(self, location)
        self.type_of_sensor = "DarknessSensor"
        self.rate_sensitivity = random.choice(DarknessSensor.darkness)

    logging.basicConfig(filename='IOT.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                        level=logging.INFO)
    logging.info("Get information about Darkness sensor!")

    # Light level descriptions
    def shuffle_rate_sensitivity(self):
        # return shuffle.rate_sensitivity  # Determine the sensitivity rate randomly
        self.rate_sensitivity = random.choice(DarknessSensor.darkness)
        return self.rate_sensitivity

    def is_night(self):
        if self.shuffle_rate_sensitivity() == 1 or self.shuffle_rate_sensitivity() == 2:
            return True

    @staticmethod
    def check():
        rand_darkness = random.choice(DarknessSensor.darkness)
        if rand_darkness == 1 or rand_darkness == 2:
            return True


class Temperature(Sensors):
    temperature = [1, 2, 3, 4, 5]

    def __init__(self, location):
        """inheritance of Sensors class"""
        super().__init__(self, location)
        self.type_of_sensor = "Temperature"
        self.rate_sensitivity = random.choice(Temperature.temperature)

    def shuffle_rate_sensitivity(self):
        self.rate_sensitivity = random.choice(Temperature.temperature)
        return self.rate_sensitivity  # Determine the sensitivity rate randomly

    def temperature_control(self):
        if self.shuffle_rate_sensitivity() == 1:
            return "freezing"
        if self.shuffle_rate_sensitivity() == 2:
            return "cool"
        if self.shuffle_rate_sensitivity() == 3:
            return "mild"
        if self.shuffle_rate_sensitivity() == 4:
            return "warm"
        if self.shuffle_rate_sensitivity() == 5:
            return "hot"

    @staticmethod
    def check():
        temp = random.randint(0, 100)
        if temp < 100:
            print("temperature is {}".format(temp))
            return True


class SoundRemote(Sensors):
    def __init__(self, location):
        """inheritance of Sensors class"""
        super().__init__(self, location)
        self.type_of_sensor = "SoundRemote"
        self.time = datetime.now()

    def time_comparison(self, now):
        music_time1 = self.time.replace(hour=18, minute=0)
        music_time2 = self.time.replace(hour=18, minute=30)
        if now.hour == music_time1.hour and music_time1.minute <= now.minute <= music_time2.minute:
            return True
        else:
            return False

    @staticmethod
    def play_music():

        default_directory = "Music/"
        running = True

        if not os.path.exists(default_directory):
            os.makedirs(default_directory)
            print("Empty folder...")
            exit()

        pygame.mixer.init()
        # files names
        playlist = [f for f in listdir(default_directory) if isfile(join(default_directory, f))]
        # shuffle playlist
        random.shuffle(playlist)
        music = default_directory + playlist.pop()
        print(music)
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy() or running:
            if len(playlist) > 0:
                music = default_directory + playlist.pop()
                print(music)
                pygame.mixer.music.queue(music)
            else:
                continue
