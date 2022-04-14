import RPi.GPIO as GPIO
import time
import pins


def f(speedA, speedB, speedC):
    GPIO.output(pins.DIR1, GPIO.LOW)    # S
    GPIO.output(pins.DIR2, GPIO.LOW)    # C
    GPIO.output(pins.DIR3, GPIO.HIGH)   # AC
    pins.SPD1.ChangeDutyCycle(0)
    pins.SPD2.ChangeDutyCycle(speedB)
    pins.SPD3.ChangeDutyCycle(speedC)


def l(speedA, speedB, speedC):
    GPIO.output(pins.DIR1, GPIO.LOW)    # C
    GPIO.output(pins.DIR2, GPIO.LOW)    # AC
    GPIO.output(pins.DIR3, GPIO.HIGH)   # AC
    pins.SPD1.ChangeDutyCycle(speedA)
    pins.SPD2.ChangeDutyCycle(speedB)
    pins.SPD3.ChangeDutyCycle(speedC)


def r(speedA, speedB, speedC):
    GPIO.output(pins.DIR1, GPIO.HIGH)   # AC
    GPIO.output(pins.DIR2, GPIO.LOW)    # C
    GPIO.output(pins.DIR3, GPIO.HIGH)   # C
    pins.SPD1.ChangeDutyCycle(speedA)
    pins.SPD2.ChangeDutyCycle(speedB)
    pins.SPD3.ChangeDutyCycle(speedC)


def b(speedA, speedB, speedC):
    GPIO.output(pins.DIR1, GPIO.LOW)  # stop
    GPIO.output(pins.DIR2, GPIO.HIGH)   # AC
    GPIO.output(pins.DIR3, GPIO.LOW)    # C
    pins.SPD1.ChangeDutyCycle(0)
    pins.SPD2.ChangeDutyCycle(speedB)
    pins.SPD3.ChangeDutyCycle(speedC)


def fl(speedA, speedB, speedC):
    GPIO.output(pins.DIR1, GPIO.LOW)    # C
    GPIO.output(pins.DIR2, GPIO.LOW)    # Stop
    GPIO.output(pins.DIR3, GPIO.HIGH)   # AC
    pins.SPD1.ChangeDutyCycle(speedA)
    pins.SPD2.ChangeDutyCycle(0)
    pins.SPD3.ChangeDutyCycle(speedC)


def br(speedA, speedB, speedC):
    GPIO.output(pins.DIR1, GPIO.HIGH)   # AC
    GPIO.output(pins.DIR2, GPIO.LOW)    # S
    GPIO.output(pins.DIR3, GPIO.LOW)    # C
    pins.SPD1.ChangeDutyCycle(speedA)
    pins.SPD2.ChangeDutyCycle(0)
    pins.SPD3.ChangeDutyCycle(speedC)


def fr(speedA, speedB, speedC):
    GPIO.output(pins.DIR1, GPIO.HIGH)   # AC
    GPIO.output(pins.DIR2, GPIO.LOW)    # C
    GPIO.output(pins.DIR3, GPIO.LOW)    # Stop
    pins.SPD1.ChangeDutyCycle(speedA)
    pins.SPD2.ChangeDutyCycle(speedB)
    pins.SPD3.ChangeDutyCycle(0)


def bl(speedA, speedB, speedC):
    GPIO.output(pins.DIR1, GPIO.LOW)    # C
    GPIO.output(pins.DIR2, GPIO.HIGH)   # AC
    GPIO.output(pins.DIR3, GPIO.LOW)    # Stop
    pins.SPD1.ChangeDutyCycle(speedA)
    pins.SPD2.ChangeDutyCycle(speedB)
    pins.SPD3.ChangeDutyCycle(0)
