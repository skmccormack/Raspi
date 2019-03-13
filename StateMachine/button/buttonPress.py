class ButtonPress:
  def __init__(self, action):
    self.action = action
  def __str__(self): return self.action

# Static fields; an enumeration of instances:
ButtonPress.on = ButtonPress("On")
ButtonPress.off = ButtonPress("Off")
ButtonPress.sel = ButtonPress("Select")
ButtonPress.left = ButtonPress("Left")
ButtonPress.right = ButtonPress("Right")
ButtonPress.up = ButtonPress("Up")
ButtonPress.down = ButtonPress("Down")
