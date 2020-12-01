## Example 0 ##
print('\n## Example 0 ##\n')

# scope = variable life expectancy
# the parts of a program where you can access a variable

def f():
  p = 2
  q = 3
  print(p+q)

def g():
  f()
  print(p) # this won't work, why?

# to make it visible to the caller, return it
def f2():
  p = 2
  q = 3
  print(p+q)
  return p

def g2():
  p = f2()
  print(p) # this will work now


## Example 1 ##
print('\n## Example 1 ##\n')

# pressure is a global variable
# defined outside any particular function
# visible everywhere
pressure = 103.9

def adjust(t):
  # t and temperature are local variables in adjust
  # defined in the function
  # not visible in the main program
  temperature = t * 1.43 / pressure
  return temperature


## Example 2 ##
print('\n## Example 2 ##\n')

# what about the visibility of limit and value variables?
limit = 100

def clip(value):
  return min(max(0.0, value), limit)

value = -22.5
print(clip(value))


## Example 3 ##
print('\n## Example 3 ##\n')

# # would this work, why?
# def inc_by(k):
# 	return x+k

# print(inc_by(10))
# x = 10


## Example 4 ##
print('\n## Example 4 ##\n')

# functions typically communicate with the outside environment
# via their parameters and return values

def change_variable(x):
	x = x+5
	return x

a = 5
a = change_variable(a)
print(a)


## Example 5 ##
print('\n## Example 5 ##\n')

# local changes are not visible outside the function scope
# unless they are returned

k = 5
def attempt_to_change_value_k(x):
	k = 10
	return x**2

x = 10
print(attempt_to_change_value_k(x))

# would k be printed as 5 or 10?
print(k)


## Example 6 ##
print('\n## Example 6 ##\n')

# there is an odering to the way Python searches for a variable
# different levels of namespaces

# LEGB rule:
# Local -> Enclosed -> Global -> Built-in

  # (L)ocal can be inside a function or class method, for example
  # (E)nclosed can be its enclosing function, e.g., if a function is wrapped inside another function
  # (G)lobal refers to the uppermost level of the executing script itself
  # (B)uilt-in are special names that Python reserves for itself

a_var = 'global'

def a_func():
  print(a_var, 'a_var inside a_func()')

a_func()
print(a_var, 'a_var outside a_func()')

#####

a_var = 'global'

def a_func():
  a_var = 'local'
  print(a_var, 'a_var inside a_func()')

a_func()
print(a_var, 'a_var outside a_func()')

#####

a_var = 'global'

def a_func():
  # to modify the global a_var
  # use the global keyword
  global a_var
  # re-assigning a new value to it 
  a_var = 'local'
  print(a_var, 'a_var inside a_func()')

print(a_var, 'a_var outside a_func()')
a_func()
print(a_var, 'a_var outside a_func()')

#####

a_var = 1

# def a_func():
#   # this will be a problem, why?
#   a_var = a_var + 1
#   print(a_var, 'a_var inside a_func()')

# print(a_var, 'a_var outside a_func()')
# a_func()

#####

a_var = 'global'

def outer():
  a_var = 'enclosed' 

  def inner():
    a_var = 'local'
    print(a_var)
  
  inner()

# which a_var will be printed?
outer()

#####

# NOT recommended but let's define our own len() function
def len(in_var):
  print('my len() function')
  l = 0
  for i in in_var:
    l += 1
  return l

def a_func(in_var):
  # which len() will be used: built-in or my len()?
  len_in_var = len(in_var)
  print('Input variable is of length', len_in_var)

a_func('Hello, World!')


## Example 7 ##
print('\n## Example 7 ##\n')

a = 'global'

def outer():
  def len(in_var):
    print('len() function in outer() function')
    l = 0
    for i in in_var:
      l += 1
    return l
  
  a = 'local'

  def inner(a):
    global len
    a += ' variable'
    print('a is', a, 'with len', len(a))

  inner(a)
  print('a is', a, 'with len', len(a))

outer()
print('a is', a, 'with len', len(a))


## Example 8 ##
print('\n## Example 8 ##\n')

def create_adder(x): 
  global tic 
  tic = x

  def adder():
    global tic
    tic = tic + x
    return tic

  return adder 
 
a = create_adder(1)
b = create_adder(2)

print(a())
print(a())
print(a())
print(a())
print(b())
print(a())
print(b())
print(b())
print(b())


## Example 9 ##
print('\n## Example 9 ##\n')

def quadruple(x):

  def double(x):
    return x+x

  print(double(double(x)))

quadruple(2)


## Example 10 ##
print('\n## Example 10 ##\n')

def quadruple(x):

  def double(y):
    return y+y

  print(double(double(x)))

quadruple(2)