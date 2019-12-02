def add(a, b):
    return a + b


def subtract(a, b):
    if b== 0:
      raise ValueError('Cant devide by zero')
    else:
     return a/b

print(add(2, 2))
