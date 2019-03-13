import RPi.GPIO as GPIO

#To set numbing system
GPIO.setmode(GPIO.BOARD)

#To get rid of warnings
#GPIO.setwarnings(False)

# Set the "SPI_NO_CS" flag to disable use of the chip select
#spi.no_cs = True

#Set up IOs
#Switch CSs
LPSw = GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW)   #Low Pass Bypass
HPSw = GPIO.setup(38, GPIO.OUT, initial=GPIO.LOW)   #High Pass Bypass
BPSw = GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW)   #Band Pass Bypass
BSSw = GPIO.setup(36, GPIO.OUT, initial=GPIO.LOW)   #Band Stop Bypass
ClipSw = GPIO.setup(35, GPIO.OUT, initial=GPIO.LOW)   #Clipping Bypass
#Digital Potentiometer CSs
LPc = GPIO.setup(33, GPIO.OUT, initial=GPIO.LOW)   #LP cutoff (dual)
LPq = GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW)   #LP q (single)
HPc = GPIO.setup(31, GPIO.OUT, initial=GPIO.LOW)   #HP cutoff (dual)
HPq = GPIO.setup(29, GPIO.OUT, initial=GPIO.LOW)   #HP q (single)
BPc = GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)   #BP cutoff (dual)
BPq = GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)   #BP q (single)
BSc = GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)   #BS cutoff (dual)
BSq = GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)   #BS q (single)
Clip = GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)   #Clipping (dual)



#Use this outside of while loop for restart pin assignments
#GPIO.cleanup()
