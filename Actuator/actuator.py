from datetime import datetime
from IOT_Sensors.simplesensors import Temperature, SoundRemote, DarknessSensor, Sensors


class Actuator(Temperature, SoundRemote, DarknessSensor):
    time = datetime.now().hour
    actuator_types = ['1.light power', '2.boiler', '3.alarm']

    def __init__(self, actuator_type, rate_sensitivity, sensor_type, installation_located):
        super().__init__(rate_sensitivity, sensor_type, installation_located)
        self.actuator_type = actuator_type

    def light_power(self):  # a function for turning on the lights in different situations
        DarknessSensor.measure_light(self)
        if True:
            print("Lights on; {}".format(Sensors.installation_located[2]))
        else:
            print("do nothing")

    def boiler(self):  # a function for start boiling the water at 7 o'clock
        Temperature.shuffle_rate_sensitivity(self)
        Temperature.temp_control(self)
        if True:
            print("Water will start boiling; {}".format(Sensors.installation_located))
        else:
            print("do nothing")

    def alarming(self):  # a function for alarming
        SoundRemote.alarm(self)
        if True:
            print("alarm; {}".format(Sensors.installation_located[0]))
        else:
            print("do nothing")
        SoundRemote.sound_control(self)
        if True:
            print("this sensor is running; {}".format(Sensors.installation_located))
        else:
            print("do nothing")

    def actuator(self):
        if self.actuator_type == 1:
            Actuator.light_power(self)
        elif self.actuator_type == 2:
            Actuator.boiler(self)
        elif self.actuator_type == 3:
            Actuator.alarming(self)
        else:
            print("This actuator is not installed!")
