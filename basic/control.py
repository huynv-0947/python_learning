# opeator
print(1 == 1) # True
print(1 != 1) # False
print(1 > 1) # False
print(1 < 1) # False
print(1 >= 1) # True
print(1 == 1 and 2 == 2) # True
print(1 < 1 or 2 == 2) # True

# if, elif, else
if 10 == 10:
  print('OK') # OK

a = 1; b = 1
if a > b:
  print('a > b')
elif a < b:
  print('a < b')
else:
  print('a = b')
# a < b

if 1 == 1:
  pass # not raise error

# while
i = 0
while i <= 5:
  if i%2 == 0:
    print(i)
    i += 1
  else:
    i += 1
    continue
else:
  print('i now is greater than 5')

# for
for x in "abc":
  print(x) # abc

for x in range(1, 5):
  if x%2 == 0:
    pass
  else:
    print(x)
# 1, 3
