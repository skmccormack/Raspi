# StateMachine/filters/filter_switch.py
# State Machine pattern using 'if' statements
# to determine the next state.
import string, sys #needs edit
sys.path += ['../StateMachine', '../button', '../comm']
from StateMachine import State
from StateMachine import StateMachine
from button import buttonPress
from comm import configure

#Devices
class Devices:
  def __init__(self, value, switch):
    self.value = value
    self.switch = switch
clip = Devices(50000, 1)  #initial value
lpc = Devices(50000, 1)  #initial value - Ignoring switch val for cutoff freq
lpq = Devices(50000, 1)  #initial value
hpc = Devices(50000, 1)  #initial value - Ignoring switch val for cutoff freq
hpq = Devices(50000, 1)  #initial value
bpc = Devices(50000, 1)  #initial value - Ignoring switch val for cutoff freq
bpq = Devices(50000, 1)  #initial value
bsc = Devices(50000, 1)  #initial value - Ignoring switch val for cutoff freq
bsq = Devices(50000, 1)  #initial value

# A different subclass for each state:
class Clipping(State):
  def run(self, input):
    if clip.switch:
      if input == ButtonPress.up:
        clip.value = increment(clip.value, 1)         #Have if statement for max value, write to pot in function, take 1 as dual, return new value
      if input == ButtonPress.down:
        clip.value = decrement(clip.value, 1)         #Have if statement for min value, write to pot in function, take 1 as dual, return new value
    if input == ButtonPress.on:
      clip.switch = 1
      comtosw(ClipSw, clip.switch)
    if input == ButtonPress.off:
      clip.switch = 0
      comtosw(ClipSw, clip.switch)
  def next(self, input):
    if input == ButtonPress.sel:
      return Filters.lowpass
    return Filters.clipping

class LowPass(State):
  def run(self, input):
    if lpq.switch == 1:
      if input == ButtonPress.up:
        lpq.value = increment(lpq.value, 1)         #Have if statement for max value, write to pot in function, take 1 as dual, return new value
      if input == ButtonPress.down:
        lpq.value = decrement(lpq.value, 1)         #Have if statement for min value, write to pot in function, take 1 as dual, return new value
      if input == ButtonPress.right:
        lpc.value = increment(lpc.value, 0)         #Have if statement for max value, write to pot in function, take 0 as singular, return new value
      if input == ButtonPress.left:
        lpc.value = decrement(lpc.value, 0)         #Have if statement for min value, write to pot in function, take 0 as singular, return new value
    if input == ButtonPress.on:
      lpq.switch = 1
      comtosw(LPSw, lpq.switch)
    if input == ButtonPress.off:
      lpq.switch = 0
      comtosw(LPSw, lpq.switch)
  def next(self, input):
    if input == ButtonPress.sel:
      return Filters.highpass
    return Filters.lowpass

class HighPass(State):
  def run(self, input):
    if hpq.switch == 1:
      if input == ButtonPress.up:
        hpq.value = increment(hpq.value, 1)         #Have if statement for max value, write to pot in function, take 1 as dual, return new value
      if input == ButtonPress.down:
        hpq.value = decrement(hpq.value, 1)         #Have if statement for min value, write to pot in function, take 1 as dual, return new value
      if input == ButtonPress.right:
        hpc.value = increment(hpc.value, 0)         #Have if statement for max value, write to pot in function, take 0 as singular, return new value
      if input == ButtonPress.left:
        hpc.value = decrement(hpc.value, 0)         #Have if statement for min value, write to pot in function, take 0 as singular, return new value
    if input == ButtonPress.on:
      hpq.switch = 1
      comtosw(HPSw, hpq.switch)
    if input == ButtonPress.off:
      hpq.switch = 0
      comtosw(HPSw, hpq.switch)
  def next(self, input):
    if input == ButtonPress.sel:
      return Filters.bandpass
    return Filters.highpass
  
class BandPass(State):
  def run(self, input):
    if bpq.switch == 1:
      if input == ButtonPress.up:
        bpq.value = increment(bpq.value, 1)         #Have if statement for max value, write to pot in function, take 1 as dual, return new value
      if input == ButtonPress.down:
        bpq.value = decrement(bpq.value, 1)         #Have if statement for min value, write to pot in function, take 1 as dual, return new value
      if input == ButtonPress.right:
        bpc.value = increment(bpc.value, 0)         #Have if statement for max value, write to pot in function, take 0 as singular, return new value
      if input == ButtonPress.left:
        bpc.value = decrement(bpc.value, 0)         #Have if statement for min value, write to pot in function, take 0 as singular, return new value
    if input == ButtonPress.on:
      bpq.switch = 1
      comtosw(BPSw, bpq.switch)
    if input == ButtonPress.off:
      bpq.switch = 0
      comtosw(BPSw, bpq.switch)
  def next(self, input):
    if input == ButtonPress.sel:
      return Filters.bandstop
    return Filters.bandpass
  
class BandStop(State):
  def run(self, input):
    if bsq.switch == 1:
      if input == ButtonPress.up:
        bsq.value = increment(bsq.value, 1)         #Have if statement for max value, write to pot in function, take 1 as dual, return new value
      if input == ButtonPress.down:
        bsq.value = decrement(bsq.value, 1)         #Have if statement for min value, write to pot in function, take 1 as dual, return new value
      if input == ButtonPress.right:
        bsc.value = increment(bsc.value, 0)         #Have if statement for max value, write to pot in function, take 0 as singular, return new value
      if input == ButtonPress.left:
        bsc.value = decrement(bsc.value, 0)         #Have if statement for min value, write to pot in function, take 0 as singular, return new value
    if input == ButtonPress.on:
      bsq.switch = 1
      comtosw(BSSw, bsq.switch)
    if input == ButtonPress.off:
      bsq.switch = 0
      comtosw(BSSw, bsq.switch)
  def next(self, input):
    if input == ButtonPress.sel:
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
    
buttonspressed = map(string.strip, open("textfile").readlines())
buttonsPressed = map(ButtonPress, buttonspressed)
Filters().runAll(buttonsPressed)
