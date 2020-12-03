# A Python program to return multiple  
# values from a method using tuple 
  
# This function returns a tuple 
def fun(): 
  str = "hello"
  x = 20
  y = 1.0
  return str, x, y  # Return tuple
                    # we could also write (str, x, y) 
  
# code to test above method 
a, b, c = fun() # Assign returned tuple 
# (a, b, c) = fun() # this is also ok 
print(a) 
print(b) 
print(c)


# A Python program to return multiple  
# values from a method using list 
  
# This function returns a list 
def fun(): 
  str = "hello"
  x = 20   
  y = 1.0
  return [str, x, y]  
  
# code to test above method 
list = fun()  
print(list) 


# A Python program to return multiple  
# values from a method using dictionary 
  
# This function returns a dictionary 
def fun(): 
  d = dict();  
  d['str'] = "hello"
  d['x'] = 20
  d['y'] = 1.0
  return d 

# code to test above method 
d = fun()  
print(d) 