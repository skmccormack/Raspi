# StateMachine/filters/filter_switch.py
# State Machine pattern using 'if' statements
# to determine the next state.
import string, sys
sys.path += ['../StateMachine', '../button']
from State import State
from StateMachine import StateMachine
from ButtonPress import ButtonPress

#Devices
class Devices:
  def __init__(self, value):
    self.value = value
clip = Devices(100)  #initial value
lpc = Devices(100)  #initial value
lpq = Devices(100)  #initial value
hpc = Devices(100)  #initial value
hpq = Devices(100)  #initial value
bpc = Devices(100)  #initial value
bpq = Devices(100)  #initial value
bsc = Devices(100)  #initial value
bsq = Devices(100)  #initial value

#Function to change pot value with vertical buttons
def ValueChangeV(value):
  if input == ButtonPress.up:
    value = value + inc
  if input == ButtonPress.down:
    value = value - inc
    
#Function to change pot value with horizontal buttons
def ValueChangeH(value):
  if input == ButtonPress.right:
    value = value + inc
  if input == ButtonPress.left:
    value = value - inc

# A different subclass for each state:
class Clipping(State):
  def run(self):
    clip.value = ValueChangeV(clip.value)
    data_out = {addr, 0b00, clip.value}    #NEEDS FIXING
    #turn on clipping device cs, set MOSI to data out, turn off cs
  def next(self, input):
    if input == ButtonPress.select:
      return Filters.lowpass
    return Filters.clipping

class LowPass(State):
  def run(self):
    lpq.value = ValueChangeV(lpq.value)
    data_out = {addr, 0b00, lpq.value}   #NEEDS FIXING
    #turn on lpq device cs, set MOSI to data out, turn off cs
    lpc.value = ValueChangeH(lpc.value)
    data_out = {addr, 0b00, lpc.value}   #NEEDS FIXING
    #turn on lpc device cs, set MOSI to data out, turn off cs
  def next(self, input):
    if input == ButtonPress.select:
      return Filters.highpass
    return Filters.lowpass

class HighPass(State):
  def run(self):
    hpq.value = ValueChangeV(hpq.value)
    data_out = {addr, 0b00, hpq.value}   #NEEDS FIXING
    #turn on hpq device cs, set MOSI to data out, turn off cs
    hpc.value = ValueChangeH(hpc.value)
    data_out = {addr, 0b00, hpc.value}   #NEEDS FIXING
    #turn on hpc device cs, set MOSI to data out, turn off cs
  def next(self, input):
    if input == ButtonPress.select:
      return Filters.bandpass
    return Filters.highpass
  
class BandPass(State):
  def run(self):
    bpq.value = ValueChangeV(bpq.value)
    data_out = {addr, 0b00, bpq.value}   #NEEDS FIXING
    #turn on bpq device cs, set MOSI to data out, turn off cs
    bpc.value = ValueChangeH(bpc.value)
    data_out = {addr, 0b00, bpc.value}   #NEEDS FIXING
    #turn on bpc device cs, set MOSI to data out, turn off cs
  def next(self, input):
    if input == ButtonPress.select:
      return Filters.bandstop
    return Filters.bandpass
  
class BandStop(State):
  def run(self):
    bsq.value = ValueChangeV(bsq.value)
    data_out = {addr, 0b00, bsq.value}   #NEEDS FIXING
    #turn on bsq device cs, set MOSI to data out, turn off cs
    hpc.value = ValueChangeH(bsc.value)
    data_out = {addr, 0b00, bsc.value}   #NEEDS FIXING
    #turn on bsc device cs, set MOSI to data out, turn off cs
  def next(self, input):
    if input == ButtonPress.select:
      return Filters.Clipping
    return Filters.bandstop
  
class Filters(StateMachine):
  def __init__(self):
    #Intial State
    StateMachine.__init__(self.Filters.clipping)
    
# Static variable initialization:
Filters.clipping = Clipping()
Filters.lowpass = LowPass()
Filters.highpass = HighPass()
Filters.bandstop = BandStop()
Filters.bandpass = BandPass()
    
