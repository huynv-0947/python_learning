def decorator_function(pass_function):
  def wrapper():
    print("Wrapper is running...")
    if pass_function.__name__ == 'display':
      print("Display function are passed! Use it!")
    else:
      print("Do nothing!")

  return wrapper

@decorator_function
def display():
  pass

display()
# => Wrapper is running...
#    Display function are passed! Use it!
