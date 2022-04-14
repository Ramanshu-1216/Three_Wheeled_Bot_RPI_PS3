#include <PS3BT.h>
#include <usbhub.h>

#ifdef dobogusinclude
#include <spi4teensy3.h>
#endif
#include <SPI.h>

#define dir_1 2
#define dir_2 4
#define dir_3 6
#define pwm_1 3
#define pwm_2 5
#define pwm_3 7

USB Usb;

BTD Btd(&Usb);

PS3BT PS3(&Btd, 0x00, 0x15, 0x83, 0x3D, 0x0A, 0x57);
bool printTemperature, printAngle;

void setup()
{

     pinMode(dir_1, OUTPUT);
     pinMode(dir_2, OUTPUT);
     pinMode(dir_3, OUTPUT);
     pinMode(pwm_1, OUTPUT);
     pinMode(pwm_2, OUTPUT);
     pinMode(pwm_3, OUTPUT);

     Serial.begin(2000000);

#if !defined(__MIPSEL__)
     while (!Serial)
          ;
#endif
     if (Usb.Init() == -1)
     {
          Serial.print(F("\r\nOSC did not start"));
          while (1)
               ;
     }
     Serial.print(F("\r\nPS3 Bluetooth Library Started"));
}

void loop()
{
     Usb.Task();

     if (PS3.PS3Connected || PS3.PS3NavigationConnected)
     {
          if (PS3.getAnalogHat(LeftHatX) > 137 || PS3.getAnalogHat(LeftHatX) < 117 || PS3.getAnalogHat(LeftHatY) > 137 || PS3.getAnalogHat(LeftHatY) < 117 || PS3.getAnalogHat(RightHatX) > 137 || PS3.getAnalogHat(RightHatX) < 117 || PS3.getAnalogHat(RightHatY) > 137 || PS3.getAnalogHat(RightHatY) < 117)
          {

               if (PS3.PS3Connected)
               { // The Navigation controller only have one joystick

                    // FORWARD
                    if (PS3.getAnalogHat(RightHatX) == 127 && PS3.getAnalogHat(RightHatY) == 0)
                    {
                         Serial.print("\r\nForward");
                         digitalWrite(dir_2, LOW);  // M2 ANTI-CLOCKWISE
                         digitalWrite(dir_3, HIGH); // M3 CLOCKWISE
                         analogWrite(pwm_2, 255 - PS3.getAnalogHat(LeftHatY) * 2);
                         analogWrite(pwm_3, 255 - PS3.getAnalogHat(LeftHatY) * 2);
                    }

                    // REVERSE
                    if (PS3.getAnalogHat(RightHatX) == 127 && PS3.getAnalogHat(RightHatY) == 255)
                    {
                         Serial.print("\r\nReverse");
                         digitalWrite(dir_2, HIGH); // M3 CLOCKWISE
                         digitalWrite(dir_3, LOW);  // M2 ANTI-CLOCKWISE

                         analogWrite(pwm_2, 255 - PS3.getAnalogHat(LeftHatY) * 2);
                         analogWrite(pwm_3, 255 - PS3.getAnalogHat(LeftHatY) * 2);
                    }

                    // RIGHT
                    if (PS3.getAnalogHat(RightHatX) == 255 && PS3.getAnalogHat(RightHatY) == 127)
                    {
                         Serial.print("\r\nRight");
                         digitalWrite(dir_1, LOW);  // M1 ANTI-CLOCKWISE
                         digitalWrite(dir_2, HIGH); // M2 CLOCKWISE
                         digitalWrite(dir_3, HIGH); // M3 CLOCKWISE

                         analogWrite(pwm_1, 255 - PS3.getAnalogHat(LeftHatY) * 2);
                         analogWrite(pwm_2, (255 - PS3.getAnalogHat(LeftHatY) * 2) / 2);
                         analogWrite(pwm_3, (255 - PS3.getAnalogHat(LeftHatY) * 2) / 2);
                    }

                    // LEFT
                    if (PS3.getAnalogHat(RightHatX) == 0 && PS3.getAnalogHat(RightHatY) == 127)
                    {
                         Serial.print("\r\nLeft");
                         digitalWrite(dir_1, HIGH); // M1 CLOCKWISE
                         digitalWrite(dir_2, LOW);  // M2 ANTI-CLOCKWISE
                         digitalWrite(dir_3, LOW);  // M3 ANTI-CLOCKWISE

                         analogWrite(pwm_1, 255 - PS3.getAnalogHat(LeftHatY) * 2);
                         analogWrite(pwm_2, (255 - PS3.getAnalogHat(LeftHatY) * 2) / 2);
                         analogWrite(pwm_3, (255 - PS3.getAnalogHat(LeftHatY) * 2) / 2);
                    }

                    //        //RIGHT_TOP
                    //        if(PS3.getAnalogHat(RightHatX)==255 && PS3.getAnalogHat(RightHatY)==0){
                    //            Serial.print("\r\nRight-Top");
                    //            digitalWrite(dir_1,LOW);  //M1 ANTI-CLOCKWISE
                    //            digitalWrite(dir_3,HIGH);   //M3 CLOCKWISE
                    //
                    //            analogWrite(pwm_1,255-PS3.getAnalogHat(LeftHatY)*2);
                    //            analogWrite(pwm_3,255-PS3.getAnalogHat(LeftHatY)*2);
                    //
                    //        }
                    //
                    //        //LEFT_TOP
                    //        if(PS3.getAnalogHat(RightHatX)==0 && PS3.getAnalogHat(RightHatY)==0){
                    //            Serial.print("\r\nLeft-Top");
                    //            digitalWrite(dir_1,HIGH);  //M1 CLOCKWISE
                    //            digitalWrite(dir_2,LOW);   //M2 ANTI-CLOCKWISE
                    //
                    //
                    //            analogWrite(pwm_1,255-PS3.getAnalogHat(LeftHatY)*2);
                    //            analogWrite(pwm_2,255-PS3.getAnalogHat(LeftHatY)*2);
                    //
                    //        }
                    //
                    //        //LEFT_BOTTOM
                    //        if(PS3.getAnalogHat(RightHatX)==0 && PS3.getAnalogHat(RightHatY)==255){
                    //            Serial.print("\r\nLeft-Bottom");
                    //            digitalWrite(dir_1,HIGH);  //M1 CLOCKWISE
                    //            digitalWrite(dir_3,LOW);   //M3 ANTI-CLOCKWISE
                    //
                    //            analogWrite(pwm_1,255-PS3.getAnalogHat(LeftHatY)*2);
                    //            analogWrite(pwm_3,255-PS3.getAnalogHat(LeftHatY)*2);
                    //
                    //        }
                    //
                    //        //RIGHT_BOTTOM
                    //        if(PS3.getAnalogHat(RightHatX)==255 && PS3.getAnalogHat(RightHatY)==255){
                    //            Serial.print("\r\nRight-Bottom");
                    //            digitalWrite(dir_1,LOW);  //M1 ANTI-CLOCKWISE
                    //            digitalWrite(dir_2,HIGH);   //M2 CLOCKWISE
                    //
                    //            analogWrite(pwm_1,255-PS3.getAnalogHat(LeftHatY)*2);
                    //            analogWrite(pwm_2,255-PS3.getAnalogHat(LeftHatY)*2);
                    //        }

                    if (PS3.getAnalogHat(LeftHatX))
                    {
                         Serial.print(F("\r\nLeftHatX: "));
                         Serial.print(PS3.getAnalogHat(LeftHatX));
                    }

                    // ROTATE TO RIGHT
                    if (PS3.getAnalogHat(LeftHatX) > 127)
                    {
                         Serial.print("\r\nRotate to right");
                         digitalWrite(dir_1, LOW); // M1 ANTI-CLOCKWISE
                         digitalWrite(dir_2, LOW); // M2 CLOCKWISE
                         digitalWrite(dir_3, LOW);

                         analogWrite(pwm_1, PS3.getAnalogHat(LeftHatX) * 2 - 255);
                         analogWrite(pwm_2, PS3.getAnalogHat(LeftHatX) * 2 - 255);
                         analogWrite(pwm_3, PS3.getAnalogHat(LeftHatX) * 2 - 255);
                    }

                    // ROTATE TO LEFT
                    if (PS3.getAnalogHat(LeftHatX) < 127)
                    {
                         Serial.print("\r\nRotate to left");
                         digitalWrite(dir_1, HIGH); // M1 ANTI-CLOCKWISE
                         digitalWrite(dir_2, HIGH); // M2 CLOCKWISE
                         digitalWrite(dir_3, HIGH);

                         analogWrite(pwm_1, 255 - PS3.getAnalogHat(LeftHatX) * 2);
                         analogWrite(pwm_2, 255 - PS3.getAnalogHat(LeftHatX) * 2);
                         analogWrite(pwm_3, 255 - PS3.getAnalogHat(LeftHatX) * 2);
                    }
               }
          }
     }

     // Analog button values can be read from almost all buttons
     if (PS3.getAnalogButton(L2) || PS3.getAnalogButton(R2))
     {
          Serial.print(F("\r\nL2: "));
          Serial.print(PS3.getAnalogButton(L2));
          if (PS3.PS3Connected)
          {
               Serial.print(F("\tR2: "));
               Serial.print(PS3.getAnalogButton(R2));
          }
     }

     if (PS3.getButtonClick(PS))
     {
          Serial.print(F("\r\nPS"));
          PS3.disconnect();
     }
     else
     {
          if (PS3.getButtonClick(TRIANGLE))
          {
               Serial.print(F("\r\nTriangle"));
               PS3.setRumbleOn(RumbleLow);
          }
          if (PS3.getButtonClick(CIRCLE))
          {
               Serial.print(F("\r\nCircle"));
               PS3.setRumbleOn(RumbleHigh);
          }
          if (PS3.getButtonClick(CROSS))
               Serial.print(F("\r\nCross"));

          if (PS3.getButtonClick(UP))
          {
               Serial.print(F("\r\nUp"));
               if (PS3.PS3Connected)
               {
                    PS3.setLedOff();
                    PS3.setLedOn(LED4);
               }
          }

          if (PS3.getButtonClick(RIGHT))
          {
               Serial.print(F("\r\nRight"));

               if (PS3.PS3Connected)
               {
                    PS3.setLedOff();
                    PS3.setLedOn(LED1);
               }
          }

          if (PS3.getButtonClick(DOWN))
          {
               Serial.print(F("\r\nDown"));
               if (PS3.PS3Connected)
               {
                    PS3.setLedOff();
                    PS3.setLedOn(LED2);
               }
          }

          if (PS3.getButtonClick(LEFT))
          {
               Serial.print(F("\r\nLeft"));
               if (PS3.PS3Connected)
               {
                    PS3.setLedOff();
                    PS3.setLedOn(LED3);
               }
          }

          if (PS3.getButtonClick(L1))
               Serial.print(F("\r\nL1"));

          if (PS3.getButtonClick(L3))
          {
               digitalWrite(dir_1, HIGH);
               digitalWrite(dir_2, HIGH);
               digitalWrite(dir_3, HIGH);

               analogWrite(pwm_1, 0);
               analogWrite(pwm_2, 0);
               analogWrite(pwm_3, 0);
               Serial.print(F("\r\nL3"));
          }

          if (PS3.getButtonClick(R1))
               Serial.print(F("\r\nR1"));
          if (PS3.getButtonClick(R3))
               Serial.print(F("\r\nR3"));

          if (PS3.getButtonClick(SELECT))
          {
               Serial.print(F("\r\nSelect - "));
               PS3.printStatusString();
          }

          if (PS3.getButtonClick(START))
          {
               Serial.print(F("\r\nStart"));
               printAngle = !printAngle;
          }
     }

#if 0 // Set this to 1 in order to see the angle of the controller
    if (printAngle) {
      Serial.print(F("\r\nPitch: "));
      Serial.print(PS3.getAngle(Pitch));
      Serial.print(F("\tRoll: "));
      Serial.print(PS3.getAngle(Roll));
    }
#endif
}