import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def adc():
    for i in range(256):
        a = dec2bin(i)

        GPIO.output(dac, a)
        sleep(0.001)

        comp_val = GPIO.input(comp)

        if comp_val == 1:
            return i

    return 255

try:
    while True:
        i = adc()

        
        voltage = 3.3 * i / 256
        print(f"Digital: {i}, Voltage: {voltage:.2f}V")

        sleep(0.01)


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("EOP")