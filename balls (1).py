from gpiozero import LED
from gpiozero import AngularServo
from time import sleep
import time
import random

green = LED(4)
red = LED(27)

def turn180():
    servo = AngularServo(18, min_pulse_width=0.0005, max_pulse_width=0.0025)
    servo.angle = 90
    servo.angle = 90
    sleep(1.5)
    servo.angle = -90
    servo.angle = -90
    sleep(1.5)
    servo.close()

i=0

while(i==0):
    sleep(1)
    value = random.randint(1,5)
    red.off()
    green.on()
    sleep(value)
    green.off()
    red.on()
    turn180()



    
    