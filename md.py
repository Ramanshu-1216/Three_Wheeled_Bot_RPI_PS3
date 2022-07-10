import RPi.GPIO as GPIO
import time
import pins

# high cw low zacw

def B(speed):
    GPIO.output(pins.DIR1, GPIO.LOW)    # S
    GPIO.output(pins.DIR2, GPIO.LOW)    # C
    GPIO.output(pins.DIR3, GPIO.HIGH)   # AC
    pins.SPD1.ChangeDutyCycle(speed)
    pins.SPD2.ChangeDutyCycle(speed)
    pins.SPD3.ChangeDutyCycle(0)

def F(speed):
    GPIO.output(pins.DIR1, GPIO.HIGH)    # S
    GPIO.output(pins.DIR2, GPIO.HIGH)    # C
    GPIO.output(pins.DIR3, GPIO.LOW)   # AC
    pins.SPD1.ChangeDutyCycle(speed)
    pins.SPD2.ChangeDutyCycle(speed)
    pins.SPD3.ChangeDutyCycle(0)


def L(speed):
    GPIO.output(pins.DIR1, GPIO.HIGH)   # AC
    GPIO.output(pins.DIR2, GPIO.LOW)    # C
    GPIO.output(pins.DIR3, GPIO.HIGH)   # C
    pins.SPD1.ChangeDutyCycle(speed/2)
    pins.SPD2.ChangeDutyCycle(speed/2)
    pins.SPD3.ChangeDutyCycle(speed)


def R(speed):
    GPIO.output(pins.DIR1, GPIO.LOW)   # AC
    GPIO.output(pins.DIR2, GPIO.HIGH)    # C
    GPIO.output(pins.DIR3, GPIO.LOW)   # C
    pins.SPD1.ChangeDutyCycle(speed/2)
    pins.SPD2.ChangeDutyCycle(speed/2)
    pins.SPD3.ChangeDutyCycle(speed)


def FL(speed):
    GPIO.output(pins.DIR1, GPIO.HIGH)    # C
    GPIO.output(pins.DIR2, GPIO.LOW)    # Stop
    GPIO.output(pins.DIR3, GPIO.HIGH)   # AC
    pins.SPD1.ChangeDutyCycle(speed)
    pins.SPD2.ChangeDutyCycle(0)
    pins.SPD3.ChangeDutyCycle(speed)


def BR(speed):
    GPIO.output(pins.DIR1, GPIO.LOW)    # C
    GPIO.output(pins.DIR2, GPIO.HIGH)    # Stop
    GPIO.output(pins.DIR3, GPIO.LOW)   # AC
    pins.SPD1.ChangeDutyCycle(speed)
    pins.SPD2.ChangeDutyCycle(0)
    pins.SPD3.ChangeDutyCycle(speed)

def FR(speed):
    GPIO.output(pins.DIR1, GPIO.HIGH)   # AC
    GPIO.output(pins.DIR2, GPIO.HIGH)    # C
    GPIO.output(pins.DIR3, GPIO.LOW)    # Stop
    pins.SPD1.ChangeDutyCycle(0)
    pins.SPD2.ChangeDutyCycle(speed)
    pins.SPD3.ChangeDutyCycle(speed)


def BL(speed):
    GPIO.output(pins.DIR1, GPIO.LOW)   # AC
    GPIO.output(pins.DIR2, GPIO.LOW)    # C
    GPIO.output(pins.DIR3, GPIO.HIGH)    # Stop
    pins.SPD1.ChangeDutyCycle(0)
    pins.SPD2.ChangeDutyCycle(speed)
    pins.SPD3.ChangeDutyCycle(speed)

def SL(speed):
    GPIO.output(pins.DIR1, GPIO.HIGH)    # C
    GPIO.output(pins.DIR2, GPIO.LOW)    # C
    GPIO.output(pins.DIR3, GPIO.LOW)    # C
    pins.SPD1.ChangeDutyCycle(speed)
    pins.SPD2.ChangeDutyCycle(speed)
    pins.SPD3.ChangeDutyCycle(speed)

def SR(speed):
    GPIO.output(pins.DIR1, GPIO.LOW)    # AC
    GPIO.output(pins.DIR2, GPIO.HIGH)    # AC
    GPIO.output(pins.DIR3, GPIO.HIGH)    # AC
    pins.SPD1.ChangeDutyCycle(speed)
    pins.SPD2.ChangeDutyCycle(speed)
    pins.SPD3.ChangeDutyCycle(speed)

def BALLR(speed):
    GPIO.output(pins.DIRB, GPIO.HIGH if speed > 0 else GPIO.LOW)
    pins.SPDB.ChangeDutyCycle(30)    

def STOP():
    GPIO.output(pins.DIR1, GPIO.HIGH)    # AC
    GPIO.output(pins.DIR2, GPIO.HIGH)    # AC
    GPIO.output(pins.DIR3, GPIO.HIGH)    # AC
    GPIO.output(pins.DIRB, GPIO.HIGH)    # AC
    pins.SPD1.ChangeDutyCycle(0)
    pins.SPD2.ChangeDutyCycle(0)
    pins.SPD3.ChangeDutyCycle(0)
    pins.SPDB.ChangeDutyCycle(0)    

def THROW(speed):
    GPIO.output(pins.THRL, GPIO.LOW)    # AC
    GPIO.output(pins.THRR, GPIO.LOW)    # AC
    pins.THSPDL.ChangeDutyCycle(speed)
    pins.THSPDR.ChangeDutyCycle(speed/2)