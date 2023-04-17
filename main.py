############
### The main code for the microphone and GPIO interface
# TBD = To be Determined


##TODO:
##Properly map the analog input of the speaker to the full range of the ADC
##Using the now digital input, throw it into the AudioSampler

import RPi.GPIO as GPIO

###Set GPIOs slots below
VolIn = 24 #VOLume IN. Inputted from the ADC

class InfractionCounter(): #A class that keeps track of the Infractions.
    def __init__(self,number=0):
        self.number = number
        ##TODO fill in the rest of this with proper getters and setters


def AudioSampler(Audio): #Samples the audio and proceeds to integrate the last 2 seconds.
    buffer = 2000 #TBD
    result = 1.0
    samples = []
    while True:
        while buffer > 0:
            samples.append(Audio)
        samples.append(Audio)
        samples.pop(0)
        result = (sum(samples) / (len(samples)))
        if result > 2222: #TBD
            Infraction()
        else:
            pass
        
def Infraction(): #TODO, keeps a tally of the amount of infractions that has accumulated. 
        AlterCounter.number += 1
        if AlterCounter.number = 3:
            LEDIndicator()
        if AlterCounter.number = 5:
            NoiseMaker()
            
            
def LEDIndicator(): ##TODO: Trigger the LED. Maybe make it flash
    pass

def NoiseMaker(): ##TODO: Trigger the Noise Maker
    pass
        
        
AlertCounter = InfractionCounter() #Make the Counter Object
    
            
        
AudioSampler() # Start the program


##########Main Program
class Noise:
    def __init__(self, sound):
        self.sound = [0,1023]
    #getters and setters
    @property
    def sound(self):
        return self._sound
    @sound.setter
    def sound(self, value):
        self._sound = value
        
    def average(self):
        (self.sound)/AudioSampler(Audio)
while(True):
    counter = 0
    if Noise()>number:
        counter += 1
        if counter == 3:
            GPIO output
            counter == 0
    


