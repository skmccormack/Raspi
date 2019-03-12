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
      return Filters.LowPass
    return Filters.Clipping

class LowPass(State):
  def run(self):
    pot = ValueChange().pot.value
    data_out = {pot, addr, pot.value}
  def next(self, input):
    if input == 1:
      return Filters.HighPass
    return Filters.LowPass

class HighPass(State):
  def run(self):
    pot = ValueChange().pot.value
    data_out = {pot, addr, pot.value}
  def next(self, input):
    if input == 1:
      return Filters.BandPass
    return Filters.HighPass
  
class BandPass(State):
  def run(self):
    pot = ValueChange().pot.value
    data_out = {pot, addr, pot.value}
  def next(self, input):
    if input == 1:
      return Filters.BandStop
    return Filters.BandPass
  
class BandStop(State):
  def run(self):
    pot = ValueChange().pot.value
    data_out = {pot, addr, pot.value}
  def next(self, input):
    if input == 1:
      return Filters.Clipping
    return Filters.BandStop
  
class Filters(StateMachine):
  def __init__(self):
    #Intial State
    StateMachine.__init__(self.Filters.Clipping)
