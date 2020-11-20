from datetime import datetime
from IOT_Sensors.sensors import Temperature, SoundRemote, DarknessSensor, Sensors


class Actuator(Temperature, SoundRemote, DarknessSensor):
    time = datetime.now().hour
    actuator_type = ['light_power', 'boiler', 'pull_curtain', 'fire_extinguisher']

    def __init__(self, actuator_type, rate_sensitivity, sensor_type, installation_located):
        super().__init__(rate_sensitivity, sensor_type, installation_located)
        self.actuator_type = actuator_type

    def light_power(self):  # a function for turning on the lights in different situations
        DarknessSensor.measure_light(self)
        if True:
            print("Lights on".format(Sensors.installation_located[2]))
        else:
            print("do nothing")

    def boiler(self):  # a function for start boiling the water at 7 o'clock
        Temperature.shuffle_rate_sensitivity(self)
        Temperature.temp_control(self)
        if True:
            print("Water will start boiling".format(Sensors.installation_located))
        else:
            print("do nothing")

    def alarming(self):
        SoundRemote.alarm(self)
        if True:
            print("alarm {}".format(Sensors.installation_located[0]))
        else:
            print("do nothing")
        SoundRemote.sound_control(self)
        if True:
            print("this sensor is running {}".format(Sensors.installation_located))
        else:
            print("do nothing")
