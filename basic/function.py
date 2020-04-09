# define
def say_hi():
  print('Hello Python')

say_hi() # Hello Python

# arguments
def your_name(first_name, last_name):
  print('{} {}'.format(first_name, last_name))

your_name('Sherlock', 'Holmes') # Sherlock Holmes
# your_name('sherlock') => error

# arbitrary argument
def do_math(*number): # tuple
  total = 0
  for n in number:
    total += n

  return total

print(do_math(1, 2, 3)) # 6

# recursion
def recursion(n):
  if n > 1:
    return n + recursion(n-1)
  else:
    return n

print(recursion(3)) # 6
