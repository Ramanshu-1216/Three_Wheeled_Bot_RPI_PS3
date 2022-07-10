from flask import Flask, render_template, Response
import time
import cv2
from subprocess import check_output

app = Flask(__name__)

IPAddr = str(check_output(["hostname", "-I"]).split()[0])[2:-1]
print(IPAddr)

cv2.destroyAllWindows()

# time.sleep(2)
print("...........................")
camera = cv2.VideoCapture(0)

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

DIRB = 11
SPDB_PWM_PIN = 22

THRL = 38
THRR = 40

SHACT = 36

THSPDL_PWM_PIN = 18
THSPDR_PWM_PIN = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(DIR1, GPIO.OUT)
GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(DIR3, GPIO.OUT)
GPIO.setup(PWM_PIN_1, GPIO.OUT)
GPIO.setup(PWM_PIN_2, GPIO.OUT)
GPIO.setup(PWM_PIN_3, GPIO.OUT)

GPIO.setup(SHACT, GPIO.OUT)

GPIO.setup(DIRB, GPIO.OUT)
GPIO.setup(SPDB_PWM_PIN, GPIO.OUT)

GPIO.setup(THRL, GPIO.OUT)
GPIO.setup(THRR, GPIO.OUT)

GPIO.setup(THSPDL_PWM_PIN, GPIO.OUT)
GPIO.setup(THSPDR_PWM_PIN, GPIO.OUT)


SPD1 = GPIO.PWM(PWM_PIN_1, 1000)
SPD2 = GPIO.PWM(PWM_PIN_2, 1000)
SPD3 = GPIO.PWM(PWM_PIN_3, 1000)

SPDB = GPIO.PWM(SPDB_PWM_PIN, 1000)

THSPDL = GPIO.PWM(THSPDL_PWM_PIN, 1000)
THSPDR = GPIO.PWM(THSPDR_PWM_PIN, 1000)

SPD1.start(0)
SPD2.start(0)
SPD3.start(0)

SPDB.start(0)

THSPDL.start(0)
THSPDR.start(0)

# high cw low acw

def B(speed):
    GPIO.output(DIR1, GPIO.LOW)    # S
    GPIO.output(DIR2, GPIO.LOW)    # C
    GPIO.output(DIR3, GPIO.HIGH)   # AC
    SPD1.ChangeDutyCycle(speed)
    SPD2.ChangeDutyCycle(speed)
    SPD3.ChangeDutyCycle(0)

def F(speed):
    GPIO.output(DIR1, GPIO.HIGH)    # S
    GPIO.output(DIR2, GPIO.HIGH)    # C
    GPIO.output(DIR3, GPIO.LOW)   # AC
    SPD1.ChangeDutyCycle(speed)
    SPD2.ChangeDutyCycle(speed)
    SPD3.ChangeDutyCycle(0)


def L(speed):
    GPIO.output(DIR1, GPIO.HIGH)   # AC
    GPIO.output(DIR2, GPIO.LOW)    # C
    GPIO.output(DIR3, GPIO.HIGH)   # C
    SPD1.ChangeDutyCycle(speed/2)
    SPD2.ChangeDutyCycle(speed/2)
    SPD3.ChangeDutyCycle(speed)


def R(speed):
    GPIO.output(DIR1, GPIO.LOW)   # AC
    GPIO.output(DIR2, GPIO.HIGH)    # C
    GPIO.output(DIR3, GPIO.LOW)   # C
    SPD1.ChangeDutyCycle(speed/2)
    SPD2.ChangeDutyCycle(speed/2)
    SPD3.ChangeDutyCycle(speed)


def FL(speed):
    GPIO.output(DIR1, GPIO.HIGH)    # C
    GPIO.output(DIR2, GPIO.LOW)    # Stop
    GPIO.output(DIR3, GPIO.HIGH)   # AC
    SPD1.ChangeDutyCycle(speed)
    SPD2.ChangeDutyCycle(0)
    SPD3.ChangeDutyCycle(speed)


def BR(speed):
    GPIO.output(DIR1, GPIO.LOW)    # C
    GPIO.output(DIR2, GPIO.HIGH)    # Stop
    GPIO.output(DIR3, GPIO.LOW)   # AC
    SPD1.ChangeDutyCycle(speed)
    SPD2.ChangeDutyCycle(0)
    SPD3.ChangeDutyCycle(speed)

def FR(speed):
    GPIO.output(DIR1, GPIO.HIGH)   # AC
    GPIO.output(DIR2, GPIO.HIGH)    # C
    GPIO.output(DIR3, GPIO.LOW)    # Stop
    SPD1.ChangeDutyCycle(0)
    SPD2.ChangeDutyCycle(speed)
    SPD3.ChangeDutyCycle(speed)


def BL(speed):
    GPIO.output(DIR1, GPIO.LOW)   # AC
    GPIO.output(DIR2, GPIO.LOW)    # C
    GPIO.output(DIR3, GPIO.HIGH)    # Stop
    SPD1.ChangeDutyCycle(0)
    SPD2.ChangeDutyCycle(speed)
    SPD3.ChangeDutyCycle(speed)

def SL(speed):
    GPIO.output(DIR1, GPIO.HIGH)    # C
    GPIO.output(DIR2, GPIO.LOW)    # C
    GPIO.output(DIR3, GPIO.LOW)    # C
    SPD1.ChangeDutyCycle(speed)
    SPD2.ChangeDutyCycle(speed)
    SPD3.ChangeDutyCycle(speed)

def SR(speed):
    GPIO.output(DIR1, GPIO.LOW)    # AC
    GPIO.output(DIR2, GPIO.HIGH)    # AC
    GPIO.output(DIR3, GPIO.HIGH)    # AC
    SPD1.ChangeDutyCycle(speed)
    SPD2.ChangeDutyCycle(speed)
    SPD3.ChangeDutyCycle(speed)

def BALLR(speed):
    GPIO.output(DIRB, GPIO.HIGH if speed > 0 else GPIO.LOW)
    SPDB.ChangeDutyCycle(30)    

def STOP():
    GPIO.output(DIR1, GPIO.HIGH)    # AC
    GPIO.output(DIR2, GPIO.HIGH)    # AC
    GPIO.output(DIR3, GPIO.HIGH)    # AC
    GPIO.output(DIRB, GPIO.HIGH)    # AC
    SPD1.ChangeDutyCycle(0)
    SPD2.ChangeDutyCycle(0)
    SPD3.ChangeDutyCycle(0)
    SPDB.ChangeDutyCycle(0)    

def THROW(speed):
    GPIO.output(THRL, GPIO.LOW)    # AC
    GPIO.output(THRR, GPIO.LOW)    # AC
    THSPDL.ChangeDutyCycle(speed)
    THSPDR.ChangeDutyCycle(speed/2)

MSPEED = 0
PWM = 75
MAXSPEED = round((PWM/255) * 100)
PWMSPD = [40, 47, 57]
# PWMPTRCNT = 3
PWMPTR = 0
startThrow = False
PWMCHNG = False
btn = None


#

# def deb():
#     print("here")
#     while True:
#         F(100)
        # pygame.event.pump()
        # for event in pygame.event.get():
        #     print(event)

# deb()


def gen_frames():  # generate frame by frame from camera
    print("I am in here")
    global DIR1, DIR2, DIR3, PWM_PIN_1, PWM_PIN_2, PWM_PIN_3, DIRB, SPDB_PWM_PIN, THRL, THRR, SHACT, THSPDL_PWM_PIN, THSPDR_PWM_PIN, SPD1, SPD2, SPD3, SPDB, MSPEED, PWM, MAXSPEED, PWMSPD, PWMPTR, startThrow, PWMCHNG, btn
    while True:
        # Capture frame-by-frame


        pygame.event.pump()
        print(pygame.event.get())
        for event in pygame.event.get():
            print("IN for___________________________________")
            if event.type == pygame.JOYAXISMOTION:
                x = round(joyStick.get_axis(2)*100)
                y = round(joyStick.get_axis(3)*100)
                spd = round(joyStick.get_axis(5)*100)/2 + 50
                lx = round(joyStick.get_axis(0)*100)
                ly = round(joyStick.get_axis(1)*100)
                print(spd)
                
                if y <= -30 and y >= -100 and spd >= 2:
                    print("Forward")
                    F(spd)
                elif x >= 30 and x <= 100 and spd >= 2:
                    R(spd)
                elif x <= -30 and x >= -100 and spd >= 2:
                    L(spd)
                elif y >= 30 and y <= 100 and spd >= 2:
                    B(spd)
                elif lx <= -50 and spd > 2:
                    SL(spd/2)
                elif lx > 50 and spd > 2:
                    SR(spd/2)
                elif ly < -25:
                    BALLR(30)
                elif ly > 25:
                    BALLR(-30)
                # elif ly <= 10 and ly >= -10:
                #     print("STOP1", ly)
                #     STOP()  
                elif (x > -30 and x < 30) or (y > -30 and y < 30):
                    print("STOP2")
                    STOP()

            elif event.type == pygame.JOYBUTTONDOWN:
                btn = event.button
            elif event.type == pygame.JOYBUTTONUP:
                btn = event.button + 20
            
            if btn != None:
                print(btn)
                if btn == 3:
                    print("PWMPTRRRRRRRRRRRRRRRRRRRRRRRRRR",PWMPTR)
                    startThrow = True
                elif btn == 1:
                    startThrow = False
                elif btn == 0:
                    print("SHAAAAAAAAAAAAACT")
                    # time.sleep(3)
                    GPIO.output(SHACT, GPIO.HIGH)
                    time.sleep(1)
                    GPIO.output(SHACT, GPIO.LOW)
                elif btn == 7:
                    STOP()
                    print("STOPING")
                elif btn == 4:
                    PWMPTR += 1
                    PWMPTR = PWMPTR % len(PWMSPD)
                btn = None
        if startThrow:
            if MSPEED < PWMSPD[PWMPTR]:
                MSPEED += 1
                time.sleep(.2)
                print(MSPEED)
            else:
                if MSPEED > PWMSPD[PWMPTR]:
                    MSPEED -= 1
                    time.sleep(.2)
                    print(MSPEED)
        elif not startThrow and MSPEED > 0:
            MSPEED -= 1
            time.sleep(.2)
            print(MSPEED)
        

        THROW(MSPEED)

        success, frame = camera.read()  # read the camera frame
        if not success:
            print("Coming")
            break
        else:
            # print("coing here")

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/video_feed')
def video_feed():
    # Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    # camera = cv2.VideoCapture(3)
    """Video streaming home page."""
    return render_template('index.html')


# if __name__ == '__main__':
app.run(debug=False, host=IPAddr, port=8080)
