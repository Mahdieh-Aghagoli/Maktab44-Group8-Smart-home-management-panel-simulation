from datetime import datetime

from IOT_Sensors.simplesensors import Temperature, DarknessSensor, SoundRemote

try:
    class MusicActuator:
        sensor = SoundRemote("radio")

        def __init__(self, location):
            self.location = location

        @staticmethod
        def activate():
            now = datetime.now()
            if MusicActuator.sensor.time_comparison(now):
                SoundRemote.play_music()


    class TempActuator:
        sensor = Temperature("kettle")

        def __init__(self, location):
            self.location = location

        @staticmethod
        def activate():
            if Temperature.check() is True:
                print("kettle on")
            else:
                print("temp is 100c")


    class DarknessActuator:
        sensor = DarknessSensor("lamp")

        def __init__(self, location):
            self.location = location

        @staticmethod
        def activate():
            if DarknessSensor.check() is True:
                print("It's night time! Lights on!")
            else:
                print("It's night time!")
except ModuleNotFoundError:
    print("MODULE NOT FOUND!")
