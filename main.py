#hi
### The main code for the microphone and GPIO interface
import RPi.GPIO as GPIO

###Set GPIOs slots below
VolIn = 24 #VOLume IN. Inputted from the ADC


def AudioSampler(): #Samples the last last 
    