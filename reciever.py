# Import Python System Libraries
import time
# Load environment variables
import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
print("Loaded environment variables")
# Import Blinka Libraries
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
# Import RFM9x
import adafruit_rfm9x

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)
print("created I2C interface")

# Configure LoRa Radio
CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, float(os.environ.get("VERSION")))
rfm9x.tx_power = 23
prev_packet = None
print("configured LoRa radio")

while True:
    packet = None

    # check for packet rx
    packet = rfm9x.receive()
    if packet is None:
        pass
    else:
        # Display the packet text and rssi
        prev_packet = packet
        packet_text = str(prev_packet, "utf-8")
        print(packet_text)
        time.sleep(1)

    time.sleep(0.1)