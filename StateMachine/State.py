class State:
  def run(self, input):
      assert 0, "run not implemented"
  def next(self, input):
      assert 0, "next not implemented"
  def runAll(self, inputs):
      for i in inputs:
          print(i)
          self.currentState = self.currentState.next(i)
          self.currentState.run()
