#!/usr/bin/python

import RPi.GPIO as GPIO
import subprocess
import threading
import time

GPIO.setmode (GPIO.BCM)
GPIO.setwarnings (False)

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

class RaspberryThread(threading.Thread):
    def __init__(self, function):
        self.running = False
        self.function = function
        super(RaspberryThread, self).__init__()

    def start(self):
        self.running = True
        super(RaspberryThread, self).start()

    def run(self):
        while self.running:
            self.function()

    def stop(self):
        self.running = False


def wait():
        global playProcess
        while True:
                global playProcess
                x = 1
                print "LOOPING"
                time.sleep(.01)
                playProcess=subprocess.Popen(['omxplayer','-b','/home/videos/WAIT.mp4'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE, close_fds=True)
                time.sleep(47)
                playProcess.stdin.write('q')
                time.sleep(.4)
                x += 1

def videos():
        global playProcess
         while True:
            if GPIO.input(10):
               playProcess.stdin.write('q')
               time.sleep(.5)
               print "Play ACE"
               sippycup_video=subprocess.Popen(['omxplayer','-b','/home/videos/VIDEO_ACE.mp4'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE, close_fds=True)
               time.sleep(92)
               sippycup_video.stdin.write('q')
               time.sleep(.5)


            if GPIO.input(11):
                    playProcess.stdin.write('q')
                    time.sleep(.5)
                    print "Play X"
                    dodgeballs_video=subprocess.Popen(['omxplayer','-b','/home/videos/VIDEO_X.mp4'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE, close_fds=True)
                    time.sleep(94)
                    dodgeballs_video.stdin.write('q')
                    time.sleep(.9)


            if GPIO.input(12):
                    playProcess.stdin.write('q')
                    time.sleep(.5)
                    print "Play invitacion"
                    invitacion_video=subprocess.Popen(['omxplayer','-b','/home/videos/LOC_Invitacion.mp4'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE, close_fds=True)
                    time.sleep(4)
                    invitacion_video.stdin.write('q')
                    time.sleep(.9)

v1 = RaspberryThread( function = wait ) # Videos thread
v2 = RaspberryThread( function = videos )   # Videos thread

v1.start()
v2.start()

while True:
    pass

GPIO.cleanup() #Reset GPIOs


