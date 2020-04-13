class Animal:
  type = 'Animal' # class variable

  def __init__(self, name): # contructor
    self.name = name # instance variable

  def show_name(self): # normal method
    print('My name is', self.name)

class Dog(Animal):
  def __init__(self, name):
    super().__init__(name)

  def show_name(self):
    print('Dog name is', self.name)

class Cat(Animal):

  def __init__(self, name , age, status):
    super().__init__(name)
    self._age = age
    self.__status = status

  def show_name(self): # normal method
    print('Cat name is', self.name)

  def show_age(self): # normal method
    print('Cat age is', self._age)

  def is_alive(self): # normal method
    print(self.__status)

a = Animal('Bobby')
print(a.type) # => Animal
a.show_name() # => My name is Bobby

lupin = Dog('Lupin')
lupin.show_name() # => Dog name is Lupin

tom = Cat('Tom', 2, 'alive')
tom.show_age() # => Tom age is 1
tom.is_alive() # => alive
print(tom.__status) # => AttributeError
