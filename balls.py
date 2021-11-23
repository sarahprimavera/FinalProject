from gpiozero import LED
import time
green = LED(4)
i = 0
while i < 30:
    green.off()
    time.sleep(0.5)
    green.on()
    time.sleep(0.5)
    i += 1
