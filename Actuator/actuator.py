from datetime import datetime
from IOT_Sensors.sensors import Temperature, SoundRemote, DarknessSensor

''' when sensors added, time, temperature and etc must import from sensors 
and i must add which actuator is doing a task for a specific sensor'''


class Actuator(Temperature, SoundRemote, DarknessSensor):
    time = datetime.now().hour
    actuator_type = ['light_power', 'boiler', 'pull_curtain', 'fire_extinguisher']

    def light_power(self):  # a function for turning on the lights in different situations
        if DarknessSensor.measure_light():
            print("please turn on the lamp {}".format(installation_located[2]))
        else:
            print("bela bela bela")
        '''code for turning on the light when its dark outside'''

    '''i need a motivation sensor here cause if i want to turn the lights on, i need to know if someone came inside'''

    def boiler(self):  # a function for start boiling the water at 7 o'clock
        current_time = datetime.now().hour
        if current_time == 7 and self.rate_sensitivity < 100:
            print("Water will start boiling")

    @staticmethod
    def pull_curtain():  # a function for pulling the curtain at 7 o'clock
        current_time = datetime.now().hour
        if current_time == 7:
            print("Good Morning!")

    def fire_extinguisher(self):
        pass

    '''need smoke sensor'''
