#!/usr/bin/env python3

"""A demo of the Google CloudSpeech recognizer."""

import aiy.audio
import aiy.cloudspeech
import aiy.voicehat

import microgear.client as microgear
import logging
import time

appid = 'SmartLightIOT'
gearkey = 'xxxxxxxxxx'
gearsecret =  'xxxxxxxxxxxxxxx'

microgear.create(gearkey,gearsecret,appid,{'debugmode': True})

def connection():
    logging.info("Now I am connected with Netpie")

def subscription(topic,message):
    logging.info(topic+" "+message)
    netpieLight(message)


def disconnect():
    logging.info("disconnected")

microgear.setalias("RaspberryPI")
microgear.on_connect = connection
microgear.on_message = subscription
microgear.on_disconnect = disconnect
microgear.subscribe("/led")
microgear.connect()

recognizer = aiy.cloudspeech.get_recognizer()
recognizer.expect_phrase('turn off')
recognizer.expect_phrase('turn on')
recognizer.expect_phrase('blink')

stateled1 = '0'
stateled2 = '0'
stateled3 = '0'
r1 = '100'
r2 = '100'
r3 = '100'

led1 = aiy._drivers._led.LED(channel=25)
led2 = aiy._drivers._led.LED(channel=18)
led3 = aiy._drivers._led.LED(channel=23)

led1.start()
led2.start()
led3.start()

aiy.audio.get_recorder().start()

def netpieLight(message):
    global stateled1,stateled2,stateled3,r1,r2,r3
    if message == "b'11'" :
        led1._parse_state(aiy.voicehat.LED.ON, 0)
        stateled1 = '1'
        microgear.chat('RaspberryPI','You Said : " "/'
                            + stateled1 + '/' + stateled2 + '/' + stateled3
                            + '/' + r1 + '/' + r2 + '/' + r3)

    elif message == "b'10'" :
        led1._parse_state(aiy.voicehat.LED.OFF, 0)
        stateled1 = '0'
        microgear.chat('RaspberryPI','You Said : " "/'
                            + stateled1 + '/' + stateled2 + '/' + stateled3
                            + '/' + r1 + '/' + r2 + '/' + r3)

    elif message == "b'21'" :
        led2._parse_state(aiy.voicehat.LED.ON, 0)
        stateled2 = '1'
        microgear.chat('RaspberryPI','You Said : " "/'
                            + stateled1 + '/' + stateled2 + '/' + stateled3
                            + '/' + r1 + '/' + r2 + '/' + r3)

    elif message == "b'20'" :
        led2._parse_state(aiy.voicehat.LED.OFF, 0)
        stateled2 = '0'
        microgear.chat('RaspberryPI','You Said : " "/'
                            + stateled1 + '/' + stateled2 + '/' + stateled3
                            + '/' + r1 + '/' + r2 + '/' + r3)

    elif message == "b'31'" :
        led3._parse_state(aiy.voicehat.LED.ON, 0)
        stateled3 = '1'
        microgear.chat('RaspberryPI','You Said : " "/'
                            + stateled1 + '/' + stateled2 + '/' + stateled3
                            + '/' + r1 + '/' + r2 + '/' + r3)

    elif message == "b'30'" :
        led3._parse_state(aiy.voicehat.LED.OFF, 0)
        stateled3 = '0'
        microgear.chat('RaspberryPI','You Said : " "/'
                            + stateled1 + '/' + stateled2 + '/' + stateled3
                            + '/' + r1 + '/' + r2 + '/' + r3)

    elif message[0:3] in "b'13" :
        r1 = int(message[7:8])*10
        led1._parse_state(aiy.voicehat.LED.DIM, r1)
        stateled1 = '1'
        r1 = str(r1)
        microgear.chat('RaspberryPI','You Said : " "/'
                            + stateled1 + '/' + stateled2 + '/' + stateled3
                            + '/' + r1 + '/' + r2 + '/' + r3)

    elif message[0:3] in "b'23" :
        r2 = int(message[7:8])*10
        led2._parse_state(aiy.voicehat.LED.DIM, r2)
        stateled2 = '1'
        r2 = str(r2)
        microgear.chat('RaspberryPI','You Said : " "/'
                            + stateled1 + '/' + stateled2 + '/' + stateled3
                            + '/' + r1 + '/' + r2 + '/' + r3)

    elif message[0:3] in "b'33" :
        r3 = int(message[7:8])*10
        led3._parse_state(aiy.voicehat.LED.DIM, r3)
        stateled3 = '1'
        r3 = str(r3)
        microgear.chat('RaspberryPI','You Said : " "/'
                            + stateled1 + '/' + stateled2 + '/' + stateled3
                            + '/' + r1 + '/' + r2 + '/' + r3)



def main():

    global stateled1,stateled2,stateled3,r1,r2,r3
    while True:
        text = recognizer.recognize()
        if text is None:
            print('Sorry, I did not hear you.')
        else:
            print('You said "', text, '"')
            if 'เปิดไฟสีเหลือง' in text:
                led1._parse_state(aiy.voicehat.LED.ON, 0)
                stateled1 = '1'
                r1 = '0'
            elif 'ปิดไฟสีเหลือง' in text:
                led1._parse_state(aiy.voicehat.LED.OFF, 0)
                stateled1 = '0'
                r1 = '100'
            elif 'ไฟสีเหลืองกระพริบ' in text:
                led1._parse_state(aiy.voicehat.LED.BLINK, 0)
                stateled1 = '1'
                r1 = '100'
            elif 'หรี่ไฟสีเหลือง' in text:
                led1._parse_state(aiy.voicehat.LED.DIM, 90)
                stateled1 = '1'
                r1 = '90'
            elif 'เปิดไฟสีขาว' in text:
                led2._parse_state(aiy.voicehat.LED.ON, 0)
                stateled2 = '1'
                r2 = '0'
            elif 'ปิดไฟสีขาว' in text:
                led2._parse_state(aiy.voicehat.LED.OFF, 0)
                stateled2 = '0'
                r2 = '100'
            elif 'ไฟสีขาวกระพริบ' in text:
                led2._parse_state(aiy.voicehat.LED.BLINK, 0)
                stateled2 = '1'
                r2 = '0'
            elif 'หรี่ไฟสีขาว' in text:
                led2._parse_state(aiy.voicehat.LED.DIM, 90)
                stateled2 = '1'
                r2 = '90'
            elif 'เปิดไฟสีฟ้า' in text:
                led3._parse_state(aiy.voicehat.LED.ON, 0)
                stateled3 = '1'
                r3 = '0'
            elif 'ปิดไฟสีฟ้า' in text:
                led3._parse_state(aiy.voicehat.LED.OFF, 0)
                stateled3 = '0'
                r3 = '100'
            elif 'ไฟสีฟ้ากระพริบ' in text:
                led3._parse_state(aiy.voicehat.LED.BLINK, 0)
                stateled3 = '1'
                r3 = '0'
            elif 'หรี่ไฟสีฟ้า' in text:
                led3._parse_state(aiy.voicehat.LED.DIM, 0)
                stateled3 = '1'
                r3 = '90'
            elif 'turn on the Yellow Light'  in text:
                led1._parse_state(aiy.voicehat.LED.ON, 0)
                stateled1 = '1'
                r1 = '0'
            elif 'turn off the Yellow Light' in text:
                led1._parse_state(aiy.voicehat.LED.OFF, 0)
                stateled1 = '0'
                r1 = '100'
            elif 'blink Yellow Light' in text:
                led1._parse_state(aiy.voicehat.LED.BLINK, 0)
                stateled1 = '1'
                r1 = '0'
            elif 'turn on the white Light' in text:
                led2._parse_state(aiy.voicehat.LED.ON, 0)
                stateled2 = '1'
                r2 = '0'
            elif 'turn off the white Light' in text:
                led2._parse_state(aiy.voicehat.LED.OFF, 0)
                stateled2 = '0'
                r2 = '100'
            elif 'blink white Light' in text:
                led2._parse_state(aiy.voicehat.LED.BLINK, 0)
                stateled2 = '1'
                r2 = '0'
            elif 'turn on the blue Light' in text:
                led3._parse_state(aiy.voicehat.LED.ON, 0)
                stateled3 = '1'
                r3 = '0'
            elif 'turn off the blue Light' in text:
                led3._parse_state(aiy.voicehat.LED.OFF, 0)
                stateled3 = '0'
                r3 = '100'
            elif 'blink blue Light' in text:
                led3._parse_state(aiy.voicehat.LED.BLINK, 0)
                stateled3 = '1'
                r3 = '0'
            elif 'dim The Yellow Light' in text:
                led1._parse_state(aiy.voicehat.LED.DIM, 90)
                stateled1 = '1'
                r1 = '90'
            elif 'dim The White Light' in text:
                led2._parse_state(aiy.voicehat.LED.DIM, 90)
                stateled2 = '1'
                r2 = '90'
            elif 'dim The Blue Light' in text:
                led3._parse_state(aiy.voicehat.LED.DIM, 90)
                stateled3 = '1'
                r3 = '90'

        if text is None:
            print('ไม่มีการส่งข้อมูล')
            microgear.chat('RaspberryPI','You Said : " "/'
                            + stateled1 + '/' + stateled2 + '/' + stateled3
                            + '/' + r1 + '/' + r2 + '/' + r3)
        elif 'Goodbye' in text:
            microgear.connect(False)
            break
        else:
            microgear.chat('RaspberryPI','You Said : " ' + text + ' "/'
                            + stateled1 + '/' + stateled2 + '/' + stateled3 + '/'
                            + r1 + '/' + r2 + '/' + r3)

if __name__ == '__main__':
    main()
