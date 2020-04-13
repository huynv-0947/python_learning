import pdb
pdb.set_trace() # stop execution program

# run with debug: python -m pdb.tool.py
# some commands:
# - l: list source code and current debug position
# - ll: list all source code
# - n: execution until the next line
# - r: continue execution until the current function returns
arr = [1, 2, 'a', 'b']
arr_int = []
arr_str = []

for i in arr:
  if type(i) == int:
    arr_int.append(i)
  elif type(i) == str:
    arr_str.append(i)

print(arr_int)
print(arr_str)
