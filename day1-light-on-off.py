import time
from machine import Pin
onboardLED = Pin(25, Pin.OUT)
lightValue = 0
while True:
    lightValue = (lightValue + 1) % 2
    onboardLED.value(lightValue)
    time.sleep(1)

