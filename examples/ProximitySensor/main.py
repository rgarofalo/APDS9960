#****************************************************************
# ProximityTest.ino
# APDS-9960 RGB and Gesture Sensor
# Shawn Hymel @ SparkFun Electronics
# October 28, 2014
# https://github.com/sparkfun/APDS-9960_RGB_and_Gesture_Sensor
# Tests the proximity sensing abilities of the APDS-9960.
# Configures the APDS-9960 over I2C and polls for the distance to
# the object nearest the sensor.
# Hardware Connections:
# IMPORTANT: The APDS-9960 can only accept 3.3V!
 
#  Arduino Pin  APDS-9960 Board  Function
 
#  3.3V         VCC              Power
#  GND          GND              Ground
#  A4           SDA              I2C Data
#  A5           SCL              I2C Clock
# Resources:
# Include Wire.h and SparkFun_APDS-9960.h
# Development environment specifics:
# Written in Arduino 1.0.5
# Tested with SparkFun Arduino Pro Mini 3.3V
# This code is beerware; if you see me (or any other SparkFun 
# employee) at the local, and you've found our code helpful, please
# buy us a round!
# Distributed as-is; no warranty is given.
#****************************************************************/

import streams
streams.serial()
sleep(3000)

import APDS9960

proximity_data       = 0  
PGAIN_2X             = 1


print("------------------------------------")
print("APDS-9960 - ProximitySensor")
print("------------------------------------")
  
# Initialize APDS-9960 (configure I2C and initial values)
sensor = APDS9960.APDS9960(I2C0)
sensor.initialize()
print("APDS-9960 initialization complete")

sensor.setProximityGain(PGAIN_2X))
print("Something went wrong trying to set PGAIN")

#Start running the APDS-9960 proximity sensor (no interrupts)
sensor.enableProximitySensor(False))
print"Proximity sensor is now running")

while(Three):
    proximity_data = sensor.readProximity()

    print("Proximity: ", proximity_data);
    
    #Wait 250 ms before next reading
    sleep(250)
  