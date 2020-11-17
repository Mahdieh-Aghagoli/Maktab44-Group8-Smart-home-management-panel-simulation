import random
# from random import shuffle


class Sensors:
    # rate_sensitivity = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sensor_type = ['motion_sensor', 'temperature_sensor', 'DarknessSensor']
    installation_located = ['door', 'kettle', 'lamp']

    def __init__(self, rate_sensitivity, sensor_type, installation_located):
        """sensor attributes for initializing """
        self.rate_sensitivity = rate_sensitivity
        self.sensor_type = sensor_type
        self.installation_located = installation_located
        self.running = True

    def shuffle_rate_sensitivity(self):
        # return shuffle.rate_sensitivity  # Determine the sensitivity rate randomly
        self.rate_sensitivity = random.randint(0, 9)
        return self.rate_sensitivity


class VoltageInput:

    def __init__(self, analog_pin):
        """Setting up the analog pin please"""
        self.aio = self.aio(analog_pin)
        self.aio.setBit(12)
        print("check")

    @property
    def voltage(self):
        """Get the voltage value from the analog port"""
        raw_value = self.Aio.read()
        print("check")
        return raw_value / 4095.0 * 5.0

    def Aio(self, analog_pin):
        pass


class DarknessSensor:
    # Light level descriptions
    light_extremely_dark = "extremely_dark"
    light_very_dark = "very_dark"
    light_dark = "almost_dark"
    light_normal = "normal"
    # voltage levels
    extremely_dark_max_voltage = 2.0
    very_dark_max_voltage = 3.0
    dark_max_voltage = 4.0

    def __init__(self, analog_pin):
        """Setting up the default values of the sensor reading"""
        self.voltage_input = VoltageInput(analog_pin)
        self.voltage = 0.0
        self.ambient_light = self.light_extremely_dark
        self.measure_light()

    def measure_light(self):
        """Measuring the values of the light needed based on the voltage"""
        self.voltage = self.voltage_input.voltage
        if self.voltage < self.extremely_dark_max_voltage:
            self.ambient_light = self.light_extremely_dark
        elif self.voltage < self.very_dark_max_voltage:
            self.ambient_light = self.light_very_dark
        elif self.voltage < self.dark_max_voltage:
            self.ambient_light = self.light_dark
        else:
            self.ambient_light = self.light_normal


class Temperature(Sensors):

    def __init__(self, rate_sensitivity, sensor_type, installation_located):
        """inheritance of Sensors class"""
        super().__init__(rate_sensitivity, sensor_type, installation_located)


    def shuffle_rate_sensivitivy(self):
        self.rate_sensitivity = random.randint(0, 100)
        return self.rate_sensitivity  #Determine the sensitivity rate randomly

    def temp_control(self):
        if self.installation_located == self.installation_located[1]: #if located was in kettle
            if self.rate_sensitivity > 100:
                print("The max tate of sensitivity of temperture is .{} so you must to turn it off".format(self.rate_sensitivity))
            else:
                print("every thing is safe")


class Soundremote(Sensors):

    def __init__(self, rate_sensitivity, sensor_type, installation_located):
        """inheritance of Sensors class"""
        super().__init__(rate_sensitivity, sensor_type, installation_located)


    # def shuffle_rate_sensivitivy(self):
    #     self.rate_sensitivity = random.randint(0, 100)
    #     return self.rate_sensitivity  #Determine the sensitivity rate randomly

    def play_music(self):

        defaultDirectory = "Music/"
        running = True

        if not os.path.exists(defaultDirectory):
            os.makedirs(defaultDirectory)
            print("Empty folder...")
            exit()

        pygame.mixer.init()
        # files names
        playlist = [f for f in listdir(defaultDirectory) if isfile(join(defaultDirectory, f))]
        # shuffle playlist
        shuffle(playlist)
        music = defaultDirectory + playlist.pop()
        print(music)
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy() or running:
            if len(playlist) > 0:
                music = defaultDirectory + playlist.pop()
                print(music)
                pygame.mixer.music.queue(music)
            else:
                continue

    def alarm(self):
        from datetime import datetime as dt
        format = '%Y-%m-%d %H:%M:%S'
        currtime = dt.now()
        print("update time is {}".format(currtime))
        alarmTime = dt.strptime('2020-11-17 14:05:00', format)
        if alarmTime:
            self.play_music()

    def sound_control(self):
        if self.installation_located == self.installation_located[0]: #if located was in radio
            self.alarm()









