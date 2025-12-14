# Imports
from machine import Pin
import time

#Set up our LED names and GPIO pin numbers
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

counter = 1 # Set the counter to 1

while True: # While forever
    
    print(counter) # Print the current counter
    
    # Traffic light STOP
    red.value(1) # ON
    amber.value(0) # OFF
    green.value(0) # OFF
    
    time.sleep(20) # Wait for STOP
    
    # Traffic light GET READY
    red.value(1) # ON
    amber.value(1) # ON
    green.value(0) # OFF
    
    time.sleep(1) # Wait for GET READY
    
    # Traffic light GO
    red.value(0) # OFF
    amber.value(0) # OFF
    green.value(1) # ON
    
    time.sleep(30) # Wait for GO
    
    # Traffic light SLOW
    red.value(0) # OFF
    amber.value(1) # ON
    green.value(0) # OFF
    
    time.sleep(2) # Wait for SLOW
    
    counter += 1 # Add 1 to our counter

