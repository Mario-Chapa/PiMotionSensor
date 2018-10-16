#!/usr/bin/env python
"""
	Detects motion and outputs a sound via a buzzer buzzer. 
"""

import RPi.GPIO as GPIO
import time
from os import system as sys

# reference
# https://stackoverflow.com/questions/287871/print-in-terminal-with-colors#287944
class color:
    HEADER = '\x1b[1;30;44m'
    ERROR = '\x1b[1;31;40m'
    RESET = '\x1b[0m'

def clear():
    sys('clear')
    print(color.HEADER + "  == Motion Sensor Monitor ==  " + color.RESET)

on_led     = 17
pir_sensor = 27
buzzer      =  4

GPIO.setmode(GPIO.BCM)

GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(pir_sensor, GPIO.IN)
GPIO.setup(on_led, GPIO.OUT)

# if startup was OK, turn on status indicator
GPIO.output(on_led,True)

current_state = 0
try:
    while True:
        time.sleep(0.3)
        current_state = GPIO.input(pir_sensor)

        clear()
        print(" ")
        print("  Sensor pin (%s) state: %s" % (pir_sensor, current_state))
        if current_state == 1:
            GPIO.output(buzzer,True)
            time.sleep(0.1)
            GPIO.output(buzzer,False)
except KeyboardInterrupt:
    print(" ")
    print(color.ERROR + " Script terminated by User. Bye." + color.RESET)
    pass
finally:
    GPIO.output(on_led,False)
    GPIO.cleanup()
