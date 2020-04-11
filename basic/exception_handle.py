try:
  print(100/0)
except ArithmeticError:
  print("ArithmeticError occured!")
else:
  print("Execute when no exception")
finally:
  print("Always execute this block")

# => ArithmeticError occured!
#    Always execute this block

class CustomError(RuntimeError):
  def __init__(self, args):
    self.args = args

try:
  raise CustomError("Pass argument")
except CustomError as e:
  print(e.args) # tuple
