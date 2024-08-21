import logging
import time
from mics6814 import MICS6814

# Initialize the MICS6814 gas sensor
MICS6814_I2C_ADDR = 0x18
gas = MICS6814(i2c_addr=MICS6814_I2C_ADDR)
gas.set_led(0, 0, 0)

# Set up logging format
logging.basicConfig(
    format="%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S"
)

print("""gas_readings.py - Print readings from the MICS6814 Gas sensor.

Press Ctrl+C to exit!

""")

# Start reading from the sensor
try:
    while True:
        # Read all gas sensor values
        readings = gas.read_all()

	"""
	Oxidising is NO2
	Reducing is CO
	NH3 is NH3 (Amonia)
	"""
        # Log the readings
        logging.info(" | ".join(str(readings).splitlines()))

        # Wait for 1 second before taking the next reading
        time.sleep(1.0)

except KeyboardInterrupt:
    # Graceful exit on Ctrl+C
    pass
