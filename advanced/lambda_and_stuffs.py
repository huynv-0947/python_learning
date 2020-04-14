import functools

# lambda function
count = lambda a, b: a + b

print(count(1, 2)) # => 3

# map(function, iterable)
nums = [1, 2, 3]
double = lambda x: x * x
map_nums = map(double, nums)

print(map_nums) # <map object at 0x7fe1073d9050>
print(next(map_nums)) # => 1, next is 4, 9

# filter(function, iterable)
nums = [1, 2, 3, 4, 5]
is_even = lambda x: x%2 == 0
filter_nums = filter(is_even, nums)

print(filter_nums) # <filter object at 0x7fe1073dd7d0>
print(next(filter_nums)) # => 2

# reduce(function, iterable)
nums = [1, 2, 3, 4]
add = lambda x, y: x + y
reduce_nums = functools.reduce(add, nums)

print(reduce_nums) # => 10
