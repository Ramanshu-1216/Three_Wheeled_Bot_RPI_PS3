import pygame
import md
import time
import pins
import RPi.GPIO as GPIO

MAXSPEED = 53

pygame.init()
pygame.joystick.init()
try:
    joyStick = pygame.joystick.Joystick(0)
    joyStick.init()
except:
    pass

def deb():
    print("here")
    while True:
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                print(round(joyStick.get_axis(5)*100))

def avg(x,y):
    return (abs(x)+abs(y))//2
MOVING = False
def getCoordinates():
    global MOVING
    # pygame.event.post(pygame.event.Event(pygame.JOYAXISMOTION))
    # pygame.event.pump()
    for event in pygame.event.get():
        # print(event)
        # time.sleep(5)
        if event.type == pygame.JOYAXISMOTION:
            MOVING = True
            x = round(joyStick.get_axis(3)*100)
            y = round(joyStick.get_axis(4)*100)
            spd = round(joyStick.get_axis(2)*100)/2 + 50
            
            if y <= -30 and y >= -100 and spd >= 2:
                # time.sleep(5)
                return ( ['F', spd])
            elif x >= 30 and x <= 100 and spd >= 2:
                return ( ['R', spd])
            elif x <= -30 and x >= -100 and spd >= 2:
                return ( ['L', spd])
            elif y >= 30 and y <= 100 and spd >= 2:
                return ( ['B', spd])

            lx = round(joyStick.get_axis(0)*100)
            ly = round(joyStick.get_axis(1)*100)
            print(spd)
            if lx <= -50 and spd > 2:
                return (['SL', spd/2])
            elif lx > 50 and spd > 2:
                return (['SR', spd/2])
            elif ly < -25:
                return (['BALLRCW', 30])
            elif ly > 25:
                print(ly, "ly")
                return (['BALLRACW', -30])
            elif ly <= 10 or ly >= -10:
                return(['STOP', 0])
                
            if x > -30 or x < 30 or y > -30 or y < 30:
                return ['STOP', 0]

            return(['STOP', 0])
        

def Control():
    coordinates = getCoordinates()
    if coordinates != None:
        DIR = coordinates[0]
        SPD = coordinates[1]
        print(coordinates)
        # time.sleep(3)

        if DIR == 'F':
            md.F(SPD)
        elif DIR == 'B':
            md.B(SPD)
        elif DIR == 'L':
            md.L(SPD)
        elif DIR == 'R':
            md.R(SPD)
        elif DIR == 'FL':
            md.FL(SPD)
        elif DIR == 'FR':
            md.FR(SPD)
        elif DIR == 'BL':
            md.BL(SPD)
        elif DIR == 'BR':
            md.BR(SPD)
        elif DIR == 'SL':
            md.SL(SPD)
        elif DIR == 'SR':
            md.SR(SPD)
        elif DIR == 'BALLRACW':
            md.BALLR(SPD)
        elif DIR == 'BALLRCW':
            md.BALLR(SPD)
        else:
            md.STOP()

isThrowing = False


MSPEED = 0

def getButton():
    for event in pygame.event.get():

        # print(event)
        # time.sleep(5)
        if event.type == pygame.JOYBUTTONDOWN:
            return event.button
        elif event.type == pygame.JOYBUTTONUP:
            return event.button + 20


startThrow = False

# 100 PWM -> 40

def Throw():
    global MAXSPEED
    global MSPEED
    global startThrow
    if startThrow and MSPEED < MAXSPEED:
        MSPEED += 1
        time.sleep(.2)
        print(MSPEED)
    elif not startThrow and MSPEED > 0:
        MSPEED -= 1
        time.sleep(.2)
        print(MSPEED)
        

    md.THROW(MSPEED)
    # pygame.event.pump()
    btn = getButton()
    if btn != None:
        if btn == 2:
            startThrow = True
        elif btn == 1:
            startThrow = False
        elif btn == 0 or btn == 20:
            print("SHAAAAAAAAAAAAACT")
            # time.sleep(3)
            GPIO.output(pins.SHACT, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(pins.SHACT, GPIO.LOW)
        elif btn == 4 or btn == 24:
            md.STOP()
            print("STOPING")
            # time.sleep(3)
        # elif btn == 5:
        #     while True:
        #         pygame.event.pump()
        #         btn = getButton()
        #         if btn != None:
        #             print(btn)
        #         time.sleep(2)
        #         if btn == 50:
        #             print("broke")
        #             time.sleep(2)
        #             break


# if __name__ == "__main__":
#     while True:
#         Throw()
        # pygame.event.pump()
        # for event in pygame.event.get():
        #     print(event)
            # if event.type == pygame.JOYAXISMOTION:
            #     print(round(joyStick.get_axis()*100))