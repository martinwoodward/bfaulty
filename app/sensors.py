try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus
from bme280 import BME280
from TCS34725 import TCS34725
from ADS1015 import ADS1015

import time

class sensors:
    def __init__(self):
        self.bus = SMBus(1)
        self.bme280 = BME280(i2c_dev=self.bus)
        self.ads = ADS1015()
        self.light = TCS34725(0X29, debug=False)


    def get_readings(self):
        # Ignore first results & initialize sensors
        temperature = self.bme280.get_temperature()
        pressure = self.bme280.get_pressure()
        humidity = self.bme280.get_humidity()
        soil0 = self.ads.read(0)
        self.light.TCS34725_init()

        time.sleep(0.1)

        temperature = self.bme280.get_temperature()
        pressure = self.bme280.get_pressure()
        humidity = self.bme280.get_humidity()

        # soil ranges from dry: 1400 to full wet: 800 so give as a percentage
        soil0 = (1400 - self.ads.read(0))/6
        lux = self.light.Get_Lux()
        colorTemp = 0 #self.light.Get_ColorTemp()

        time_str = time.strftime("%H:%M:%S")

        return {
            "time": time_str,
            "temperature": temperature,
            "pressure": pressure,
            "humidity": humidity,
            "soil0": soil0,
            "lux": lux,
            "colourTemp": colorTemp
        }
