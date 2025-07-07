def addition (x, y):
  try:
    return x + y
  except ValueError: 
    return "ValueError('This operation is not supported for given input parameters')"
 
def subtraction (x, y):
  try:
    return x - y
  except ValueError: 
    return "ValueError('This operation is not supported for given input parameters')"
 
def multiplication (x, y):
  try:
    return x * y
  except ValueError: 
    return "ValueError('This operation is not supported for given input parameters')"
 
def division (x, y):
    if y == 0:
     raise ValueError('This operation is not supported for given input parameters')
    else:
      return x / y
 
def modulo (x, y):
  if x >= y and y > 0:
    return x % y
  else:
    raise ValueError('This operation is not supported for given input parameters')
 
def secondPower (x):
  try:
    return x * x
  except ValueError: 
    return "ValueError('This operation is not supported for given input parameters')"
 
def power (x, y):
    if y >= 0:
      return float(x ** y)
    else:
      raise ValueError('This operation is not supported for given input parameters')
 
def secondRadix (x):
    if x > 0:
      return x ** (0.5)
    else:
      raise ValueError('This operation is not supported for given input parameters')
 
def magic (x, y, z, k):
  if y + z != 0:
    l = x + k
    m = y + z
    n = ((l / m) + 1)
    return n
  else:
    raise ValueError('This operation is not supported for given input parameters')
 
def control (a, x, y, z, k):
  if a == "ADDITION":
    return addition(x, y)
  elif a == "SUBTRACTION":
    return subtraction(x, y)
  elif a == "MULTIPLICATION":
    return multiplication(x, y)
  elif a == "DIVISION":
    return division(x, y)
  elif a == "MOD":
    return modulo(x, y)
  elif a == "POWER":
    return power(x, y)
  elif a == "SECONDRADIX":
    return secondRadix(x)
  elif a == "MAGIC":
    return magic(x, y, z, k)
  else:
    raise ValueError('This operation is not supported for given input parameters')