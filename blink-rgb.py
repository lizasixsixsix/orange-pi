#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Based on blink_led.py example from https://github.com/Jeremie-C/OrangePi.GPIO

import OPi.GPIO as GPIO

from time import sleep

# Set Orange Pi PC board
GPIO.setboard(GPIO.PCPCPLUS)

# Set BCM numbering
GPIO.setmode(GPIO.BCM)

# Set pins as an output
GPIO.setup(8, GPIO.OUT)    # BCM 8 (physical 24)
GPIO.setup(7, GPIO.OUT)    # BCM 7 (physical 26)
GPIO.setup(1, GPIO.OUT)    # BCM 1 (physical 28)

try:
    print ("Press CTRL+C to exit")

    # 0 --- LOW/False
    # 1 --- HIGH/True

    while True:
        GPIO.output(8, 1)
        sleep(0.1)
        GPIO.output(8, 0)
        sleep(0.1)

        GPIO.output(7, 1)
        sleep(0.1)
        GPIO.output(7, 0)
        sleep(0.1)

        GPIO.output(1, 1)
        sleep(0.1)
        GPIO.output(1, 0)
        sleep(0.1)

        sleep(0.5)

except KeyboardInterrupt:
    GPIO.output(7, 0)
    GPIO.output(7, 0)
    GPIO.output(7, 0)

    GPIO.cleanup()

    print ("Bye.")
