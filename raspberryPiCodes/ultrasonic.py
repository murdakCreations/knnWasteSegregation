# Raspberry Pi 4.0 code for interfacing with ultrasonic sensor

import RPi.GPIO as GPIO
#imports modules required in program
import time #time module is used to add delays
GPIO.setmode(GPIO.BCM)
#Activates broadcam chip specific pin numbers.
#GPIO.setmode(GPIO.BOARD) - activates board pin numbers

TRIG_PIN = 11 #assign TRIG_PIN variable to GPIO pin 11
ECHO_PIN = 12 #assign ECHO_PIN variable to GPIO pin 12

#GPIO.setwarnings(False)
GPIO.setup(TRIG_PIN, GPIO.OUT) #trig pin is output
GPIO.setup(ECHO_PIN, GPIO.IN) #trig pin is input
GPIO.output(TRIG_PIN, GPIO.LOW) #drives trig pin to 0V

time.sleep(2) #delay of 2 seconds
print("slept")

GPIO.output(TRIG_PIN, GPIO.HIGH) #set trig pin high

time.sleep(0.00001) #keeps trig pin high for 10 microseconds
#this is used to trigger/start the ultrasonic module
#sends 8 ultrasonic bursts at 40KHz
print("slept")

GPIO.output(TRIG_PIN, GPIO.LOW)
#Set trig pin low

while GPIO.input(ECHO_PIN) == 0:
    #check when the echo pin goes low and pulse and
    pulse_send=time.time() #note down this time stamp in pulse_send
    #print("0")
    #print(pulse_send)

while GPIO.input(ECHO_PIN) == 1:
    #check when the echo pin goes high and
    pulse_received = time.time() #note down this time stamp
    print("1")

pulse_duration = pulse_received-pulse_send
#Pulse duration is the time difference between hen the pulse was received and sent

pulse_duration = round(pulse_duration/2,2)
#The round function rounds off the value upto 2 decimal places.

distance = 34000*pulse_duration
#calcualte and display the distance

print("Object is at ", distance, "cm from the ultrasonic sensor")

GPIO.cleanup()
#cleans/resets all the ports/pins used in the program

#speed = distance/time
#distance = speed * time
#speed of sound is 340 m/s in air medium
#To calculate the dinstance in cm, the speed of sound is 34000cm/s
#note that we have to calculate the distance from the ultrasonic sensor of the object
#but here pulse duration we have considered is from the time it is sent
#till it hits the target and comes back.
#But as we noted earlier we just need distance from ultrasonic
#sensor to object so out pulse duration will be half