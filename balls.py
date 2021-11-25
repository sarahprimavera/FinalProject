#from gpiozero import LED
#import time
#green = LED(4)
#i = 0
#while i < 30:
 #   green.off()
  #  time.sleep(0.5)
   # green.on()
    #time.sleep(0.5)
    #i += 1
from gpiozero import AngularServo
from time import sleep

servo = AngularServo(18, min_pulse_width=0.0005, max_pulse_width=0.0025)
i=0

while i<3:
    servo.angle = 90
    servo.angle = 90
    sleep(1.5)
    servo.angle = -90
    servo.angle = -90
    sleep(1.5)
    i += 1
    
servo.close()
