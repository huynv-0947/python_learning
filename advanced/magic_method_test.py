class Student:

  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return "Studio with name is {}".format(self.name) # magic method

student = Student('Sherlock')

print(student) # Studio with name is Sherlock
print(repr(student)) # Studio with name is Sherlock
