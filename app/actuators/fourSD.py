import RPi.GPIO as GPIO
import time

num = {' ':(0,0,0,0,0,0,0),
    '0':(1,1,1,1,1,1,0),
    '1':(0,1,1,0,0,0,0),
    '2':(1,1,0,1,1,0,1),
    '3':(1,1,1,1,0,0,1),
    '4':(0,1,1,0,0,1,1),
    '5':(1,0,1,1,0,1,1),
    '6':(1,0,1,1,1,1,1),
    '7':(1,1,1,0,0,0,0),
    '8':(1,1,1,1,1,1,1),
    '9':(1,1,1,1,0,1,1)}
 
def fourSD_register(pins, stop_event):
    GPIO.setmode(GPIO.BCM)
    segments = pins[0:8]
    for segment in segments:
        GPIO.setup(segment, GPIO.OUT)
        GPIO.output(segment, 0)

    digits = pins[8:12]
    for digit in digits:
        GPIO.setup(digit, GPIO.OUT)
        GPIO.output(digit, 1)

    try:
        while True:
            n = time.ctime()[11:13]+time.ctime()[14:16]
            s = str(n).rjust(4)
            for digit in range(4):
                for loop in range(0,7):
                    GPIO.output(segments[loop], num[s[digit]][loop])
                    if (int(time.ctime()[18:19])%2 == 0) and (digit == 1):
                        GPIO.output(25, 1)
                    else:
                        GPIO.output(25, 0)
                GPIO.output(digits[digit], 0)
                time.sleep(0.001)
                GPIO.output(digits[digit], 1)
            if stop_event.is_set():
                break
    finally:
        GPIO.cleanup()