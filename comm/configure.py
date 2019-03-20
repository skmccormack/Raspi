import RPi.GPIO as GPIO
import time
import spidev

#To set numbing system
GPIO.setmode(GPIO.BOARD)

#To get rid of warnings
#GPIO.setwarnings(False)

# Set the "SPI_NO_CS" flag to disable use of the chip select
#spi.no_cs = True

#Set up IOs
#Switch CSs
LPSw = 40
GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW)   #Low Pass Bypass
HPSw = 38
GPIO.setup(38, GPIO.OUT, initial=GPIO.LOW)   #High Pass Bypass
BPSw = 37
GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW)   #Band Pass Bypass
BSSw = 36
GPIO.setup(36, GPIO.OUT, initial=GPIO.LOW)   #Band Stop Bypass
ClipSw = 35
GPIO.setup(35, GPIO.OUT, initial=GPIO.LOW)   #Clipping Bypass
#Digital Potentiometer CSs
LPc = 33
GPIO.setup(33, GPIO.OUT, initial=GPIO.LOW)   #LP cutoff (dual)
LPq = 32
GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW)   #LP q (single)
HPc = 31
GPIO.setup(31, GPIO.OUT, initial=GPIO.LOW)   #HP cutoff (dual)
HPq = 29
GPIO.setup(29, GPIO.OUT, initial=GPIO.LOW)   #HP q (single)
BPc = 18
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)   #BP cutoff (dual)
BPq = 16
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)   #BP q (single)
BSc = 15
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)   #BS cutoff (dual)
BSq = 12
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)   #BS q (single)
Clip = 13
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)   #Clipping (dual)

def comtodual(pot, value):
  GPIO.output(pot, 1)
  time.sleep(0.00000006)
  wiper0writeAddr = 0x00;
  wiper1writeAddr = 0x10;
  spi.xfer([wiper0writeAddr, value])
  GPIO.output(pot, 0)
  GPIO.output(pot, 1)
  time.sleep(0.00000006)
  spi.xfer([wiper1writeAddr, value])
  GPIO.output(pot, 0)
  
def comtosing(pot, value):
  GPIO.output(pot, 1)
  time.sleep(0.00000006)
  wiperwriteAddr = 0x00;
  spi.xfer([wiperwriteAddr, value])
  
def comtosw(pot, value):
  GPIO.output(pot, 1)
  time.sleep()
  #MOSI line command
  GPIO.output(pot, 0)
