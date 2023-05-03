############
### The main code for the microphone and GPIO interface

#As you can see, a lot of modules are required to get this thing running.
import RPi.GPIO as GPIO
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import time

#tell GPIO What mode to use
GPIO.setmode(GPIO.BCM)

# create the spi bus
spi = busio.SPI(clock=board.SCLK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.CE0)

# designate the GPIO output for the beeper device.
beeper = 13
GPIO.setup(beeper, GPIO.OUT)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)
chan2 = AnalogIn(mcp, MCP.P1)



#while True:
#    print (chan.value)                                                              



##########Main Program
#averages a number for every third second



class MainSystem(): #The infraction system works as an object to make it easier to access the variables. 

    infractions = 0
    lastsecond = []
    def __init__(self):
        pass



    def AudioSampler(self): #Samples the audio and proceeds to integrate the last second or so.
        return (sum(self.lastsecond)/len(self.lastsecond))

    def noiseMaker(): #Beeps a few times to warn of a high noise. 
        GPIO.output(beeper, GPIO.HIGH)
        time.sleep(0.25)
        GPIO.output(beeper, GPIO.LOW)
        time.sleep(0.25)

        GPIO.output(beeper, GPIO.HIGH)
        time.sleep(0.25)
        GPIO.output(beeper, GPIO.LOW)
        time.sleep(0.25)

        GPIO.output(beeper, GPIO.HIGH)
        time.sleep(0.25)
        GPIO.output(beeper, GPIO.LOW)
        time.sleep(0.25)




    def noiseMakerSuper(): #A more annoying version of the above function.
        GPIO.output(beeper, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(beeper, GPIO.LOW)



        
    def Infraction(self): #The function used to increment the Infractions and resets it as well. 
        self.infractions += 1
        if self.infractions == 3:
            self.noiseMaker() #
        if self.infractions == 5:
            self.noiseMakerSuper()
            self.infractions = 0
            
            

        
        
System = MainSystem() #Make the Counter Object
    
            
while True: #can be considered the 'main' part of the program

    #Every 'frame', add the recorded value to the list of recorded values.
    System.lastsecond.append(chan.value)
    
    if len(System.lastsecond) > 1000: #And then every 1000 'frames' find the average and compare to the threshold
        audioCheck = System.AudioSampler()
        print (audioCheck)
        if audioCheck > 5000:
            System.Infraction()
        System.lastsecond.clear()



    
    