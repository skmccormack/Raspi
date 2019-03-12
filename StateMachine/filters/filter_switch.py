# StateMachine/filters/filter_switch.py
# State Machine pattern using 'if' statements
# to determine the next state.
import string, sys
sys.path += ['../StateMachine', '../button']
from State import State
from StateMachine import StateMachine
from ButtonPress import ButtonPress
# A different subclass for each state:
class Clipping(State):
  def run(self):
    pot = ValueChange().pot.value
    data_out = {pot, addr, pot.value}
  def next(self, input):
    if input == 1:
      return Filters.lowpass
    return Filters.clipping

class LowPass(State):
  def run(self):
    pot = ValueChange().pot.value
    data_out = {pot, addr, pot.value}
  def next(self, input):
    if input == 1:
      return Filters.highpass
    return Filters.lowpass

class HighPass(State):
  def run(self):
    pot = ValueChange().pot.value
    data_out = {pot, addr, pot.value}
  def next(self, input):
    if input == 1:
      return Filters.bandpass
    return Filters.highpass
  
class BandPass(State):
  def run(self):
    pot = ValueChange().pot.value
    data_out = {pot, addr, pot.value}
  def next(self, input):
    if input == 1:
      return Filters.bandstop
    return Filters.bandpass
  
class BandStop(State):
  def run(self):
    pot = ValueChange().pot.value
    data_out = {pot, addr, pot.value}
  def next(self, input):
    if input == 1:
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
    
