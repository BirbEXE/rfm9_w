# Adafruit RMF95W/RFM96W for the Pi Zero 2 W

![PXL_20240112_222247882](https://github.com/BirbEXE/rmf95w/assets/60234159/dbab0cc5-a32c-4701-ab87-37a2f59195c5)

I was trying to use the Pi Zero 2 W with the Adafruit RMF95W and I found the documentation frustratingly unusable for this particular board

All the example code seemed to be fitted for the version which is fitted with an OLED / buttons, and a lot is targetted towards arduinos.

Here's how to set it up, the easy way.

## Wiring Layout

I was going to go into more detail but this'll do for now

ignore the buttons and resistors, just focus on the connections between the Pi's GPIO pins and the RFM95W/96W

![wiring](https://cdn-learn.adafruit.com/assets/assets/000/091/522/original/raspberry_pi_rfm9x_bb_2.png)

## MicroSD setup

To start, you'll need a MicroSD card running Raspberry Pi OS (Legacy, 64 bit) Lite

Setup your network details and username/password in the [Raspberry Pi imager](https://downloads.raspberrypi.org/imager/imager_latest.exe)

SSH into the Pi, and we can continue to the next step!

## Installing Prerequisites

Once you've SSH'ed into your Pi, run the following commands in your terminal:

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-pip
sudo apt install --upgrade python3-setuptools
```

Then you can setup a virtual environment. Whilst this step is technically optional, it is **strongly** reccomended unless you know what you're doing.

To setup a venv, run the following commands

```
sudo apt-get install python3-venv
python -m venv env --system-site-packages
```

You should enter the venv by running this command:

```
source env/bin/activate
```

*note: you will have to run this command every time the Pi reboots.*

After you've entered the venv, run the Adafruit Blinka installer script:

```
cd ~
pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo -E env PATH=$PATH python3 raspi-blinka.py
```

Finally, install the other neccecary python libraries:

```
pip install python-dotenv
pip install Flask
```

## Install RFM95W Library

Still in your venv, run the command

```
sudo pip3 install adafruit-circuitpython-rfm9x
```

## Sending / Recieving data

To download the scripts, enter your venv (if not already inside it), and run the commands:

```
git clone https://github.com/birbexe/rfm9_w.git
cd rfm9_w
```

Once that's downloaded, you have to edit a few things.

First, work out what version of the RFM95W board you have. Adafruit sell a [433MHz version](https://www.adafruit.com/product/3073) and a [868 or 915 MHz version](https://www.adafruit.com/product/3072)

Once that's worked out, type

```
sudo nano .env
```

find line **5** of the file `.env`

Then, add your board version.

for example, if you have the 433 Mhz version, it should look like this:

```
version=433.0
```

or if you have the 868/915Mhz version, it should look like this:

```
version=915.0
```

After you're done editing, simply save the file by pressing `CTRL + X` followed by `Y` and then `ENTER`

## Running the code

Once you have the board prepared, you have to decide whether you want to test it as a reciever, or a transmitter.

if you're using it as a reciever, run `python reciever.py`

This will display any recieved transmissions

if you're using it as a transmitter, run `python transmitter.py`

this will start the flask server, which can be accessed in a web browser, on your Pi's local IP

any text inputted and sent via the flask server will be transmitted through the LoRa board

![image](https://github.com/BirbEXE/rfm9_w/assets/60234159/2a41a815-0bef-45c8-9e56-40456b722c90)

## Contributing

If you feel like you have something to contribute, feel free to [drop a pull request](https://github.com/BirbEXE/rmf95w/pulls)!

<a href="https://github.com/birbexe/rmf95w/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=birbexe/rmf95w" />
</a>
