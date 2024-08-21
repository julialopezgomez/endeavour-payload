import time
import board
from adafruit_dps310.basic import DPS310

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
dps310 = DPS310(i2c)

dps310.sea_level_pressure = 1002

while True:
    print("Temperature = %.2f *C" % dps310.temperature)
    print("Pressure = %.2f hPa" % dps310.pressure)
    print("Sea Level Pressure = %.2f hPa" % dps310.sea_level_pressure)
    print("Altitude = %.2f m above sea level" % dps310.altitude)
    print("")
    time.sleep(1.0)
