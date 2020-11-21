from IOT_Sensors import simplesensors
from datetime import datetime

class Music:
    def __init__(self, location):
        self.sensor = simplesensors.SoundRemote("radio")
        self.location = location

    def play_music(self):
        now = datetime.now()
        if self.sensor.time_comparison(now):
            simplesensors.SoundRemote.play_music()



a = Music("Radio")
a.play_music()
print(a.sensor)
a.sensor = "DarknessSensor"
print(a.sensor)
