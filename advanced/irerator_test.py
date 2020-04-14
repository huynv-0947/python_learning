nums = [1, 2, 3]

# normal loop
for num in nums:
  print(num)

print('__iter__' in dir(nums)) # => True

# for loop do under the hood is call iter magic method on object
# => return a iterator, so that object can iterable

# list is iterable, not is iterator
# iterator is object can remember where it in in the iteration, have next() method

nums_iterator = iter(nums)

print(nums_iterator) # <list_iterator object at 0x7f61d49ede90>
print('__next__' in dir(nums_iterator)) # => True
print(next(nums_iterator)) # or nums_iterator.__next__()
# => 1
print(next(nums_iterator)) # => 2
print(next(nums_iterator)) # => 3
print(next(nums_iterator)) # => raise StopIterationException
