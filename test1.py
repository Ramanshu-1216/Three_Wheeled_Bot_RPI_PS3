import RPi.GPIO as GPIO
import pygame
import time

pygame.init()
pygame.joystick.init()
try:
    joyStick = pygame.joystick.Joystick(0)
    joyStick.init()
except:
    pass

DIR3 = 35   # 37
DIR1 = 37   # 35
DIR2 = 31   # 31
PWM_PIN_1 = 32
PWM_PIN_2 = 12
PWM_PIN_3 = 33

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(DIR1, GPIO.OUT)
GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(DIR3, GPIO.OUT)
GPIO.setup(PWM_PIN_1, GPIO.OUT)
GPIO.setup(PWM_PIN_2, GPIO.OUT)
GPIO.setup(PWM_PIN_3, GPIO.OUT)

SPD1 = GPIO.PWM(PWM_PIN_1, 1000)
SPD2 = GPIO.PWM(PWM_PIN_2, 1000)
SPD3 = GPIO.PWM(PWM_PIN_3, 1000)
SPD1.start(0)
SPD2.start(0)
SPD3.start(0)

while True:
    GPIO.output(DIR1, GPIO.HIGH)    # S
    GPIO.output(DIR2, GPIO.HIGH)    # C
    GPIO.output(DIR3, GPIO.LOW)   # AC
    SPD1.ChangeDutyCycle(100)
    SPD2.ChangeDutyCycle(100)
    SPD3.ChangeDutyCycle(0)