#!/usr/bin/python
# -*- coding:utf-8 -*-

#import python, dotenv + flask libraries
import logging
import time
import traceback
import requests
import json
from flask import Flask, request, render_template
import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
print("Loaded environment variables")

# Import Python System Libraries
import time
# Import Blinka Libraries
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
# Import RFM9x
import adafruit_rfm9x

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)
print("Created I2C interface")

# Configure LoRa Radio
CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, float(os.environ.get("VERSION")))
rfm9x.tx_power = 23
prev_packet = None
print("Configured LoRa radio")

try:
    app = Flask(__name__)

    @app.route('/')
    def my_form():
        return render_template('form.html')

    @app.route('/', methods=['POST'])
    def my_form_post():
        text = request.form['msg']
        packet = None
        data = bytes(text+"\r\n","utf-8")
        rfm9x.send(data)
        print(f'Sent {text}!', 25, 15, 1)
        return render_template('form.html')

    app.run(port=8000, host="0.0.0.0")

except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    exit()