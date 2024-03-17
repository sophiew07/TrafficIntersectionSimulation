# TRAFFIC LIGHT CULMINATING TASK - Celina + Sophie

# Imports go at the top
from microbit import *

# North and South traffic lights
NS_red_pin = pin1   
NS_power_pin = pin2
NS_green_pin = pin3 
NS_blue_pin = pin4  

# East and West traffic lights
EW_red_pin = pin6   
EW_power_pin = pin7
EW_green_pin = pin8
EW_blue_pin = pin9

# crosswalk and override buttons
crosswalkButton = pin10
overrideButton = pin12

# used to turn off the LED display to have more GPIO pins
display.off() 


# the longest leg of the RGB LED
NS_power_pin.write_digital(1)
EW_power_pin.write_digital(1)

# turn on all colours to ensure they all work (2s)
NS_red_pin.write_digital(0)
NS_green_pin.write_digital(0)
NS_blue_pin.write_digital(0)
EW_red_pin.write_digital(0)
EW_green_pin.write_digital(0)
EW_blue_pin.write_digital(0)
sleep(2000)

# individual functions for each light colour (for code simplicity)
def nsRedLight():
    NS_red_pin.write_digital(0)
    NS_green_pin.write_digital(1)
    NS_blue_pin.write_digital(1)
    # N/S red light

def ewRedLight():
    EW_red_pin.write_digital(0)
    EW_green_pin.write_digital(1)
    EW_blue_pin.write_digital(1)
    # E/W red light

def nsGreenLight(temp = False):
    NS_red_pin.write_digital(1)
    NS_green_pin.write_digital(0)
    NS_blue_pin.write_digital(1)
    if temp == True:
        # Signal that traffic is moving north and south, safe to walk the same direction
        pin14.write_digital(0)
        pin15.write_digital(1)
        for i in range(50):
            sleep(100)
            if crosswalkButton.read_digital() == 1:
                crosswalk()
                NS_red_pin.write_digital(1)
                NS_green_pin.write_digital(0)
                NS_blue_pin.write_digital(1)
                pin14.write_digital(0)
                pin15.write_digital(1)
            if overrideButton.read_digital() == 1:
                override()
                NS_red_pin.write_digital(1)
                NS_green_pin.write_digital(0)
                NS_blue_pin.write_digital(1)
                pin14.write_digital(0)
                pin15.write_digital(1)

        # Blinks to signal that the light is about to change (stop walking)
        for blinks in range(5):
            pin14.write_digital(0)
            pin15.write_digital(1)
            pin16.write_analog(1000)
            sleep(500)
            pin14.write_digital(0)
            pin15.write_digital(0)
            pin16.write_analog(0)
            sleep(500)

        # Lights are off to signal that no cars or pedestrians should be moving 
        pin14.write_digital(0)
        pin15.write_digital(0)

    # N/S green light

def ewGreenLight():
    EW_red_pin.write_digital(1)
    EW_green_pin.write_digital(0)
    EW_blue_pin.write_digital(1)
    # Signal that traffic is moving east and west, safe to walk the same direction
    pin14.write_digital(1)
    pin15.write_digital(0)
    sleep(5000)

    # Blinks to signal that the light is about to change (stop walking)
    for blinks in range(5):
        pin14.write_digital(1)
        pin15.write_digital(0)
        pin16.write_analog(1000)
        sleep(500)
        pin14.write_digital(0)
        pin15.write_digital(0)
        pin16.write_analog(0)
        sleep(500)

    pin14.write_digital(0)
    pin15.write_digital(0)
    # E/W green light

def nsYellowLight():
    NS_red_pin.write_digital(0)
    NS_green_pin.write_digital(0)
    NS_blue_pin.write_digital(1)
    # N/S yellow light

def ewYellowLight():
    EW_red_pin.write_digital(0)
    EW_green_pin.write_digital(0)
    EW_blue_pin.write_digital(1)
    # E/W yellow light

# what happens if you push the crosswalk buttons
def crosswalk():
    nsGreenLight()
    ewRedLight()
    sleep(3000)

    nsYellowLight()
    ewRedLight()
    sleep(1000)

    nsRedLight()
    ewRedLight()
    sleep(1000)

    nsRedLight()
    ewGreenLight()

    nsRedLight()
    ewYellowLight()
    sleep(1000)

    nsRedLight()
    ewRedLight() 
    sleep(1000)

def override():
    nsYellowLight()
    ewRedLight()
    sleep(1000)

    nsRedLight()
    ewRedLight()
    sleep(1000)

    nsRedLight()
    ewGreenLight()

    nsRedLight()
    ewYellowLight()
    sleep(1000)

    nsRedLight()
    ewRedLight()
    sleep(1000)

while True:
    ewRedLight()
    nsGreenLight(True)

    nsYellowLight()
    ewRedLight()
    sleep(1000)

    nsRedLight()
    sleep(1000)
    ewRedLight()
    sleep(1000)

    nsRedLight()
    ewGreenLight()

    nsRedLight()
    ewYellowLight()
    sleep(1000)

    nsRedLight()
    ewRedLight()
    sleep(1000)
