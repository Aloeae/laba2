def my_generate(start=0, stop=5, step=1):
  number = start
  while number <= stop:
    yield number
    number += start
    
ranger = my_generate(1,4)

for value in ranger:
  print(value)



==================== RESTART: C:/Users/tvoym/Downloads/ex.py ===================
1
2
3
4
