# || Gobal variables || 
# variables  that are created outside of a function (as in all of the examples in the previous pages ) are  known as global variables.
#  global variables can be used by everyone ,both inside of functions and outside.

# example
# create a variable outside  of a function, and use it inside the function 

x = "awesome"
def myfunc():
 print("python is " + x)
 myfunc()

# create a variable inside a function , with the same  name sa the global variable
 x = "awesome"
 def myfunc():
  x = " fantastic"
  print("python is " + x)
  myfunc()
  print("python is " + x)

#   the global keyword 
#  normanally , when  you createa variable inside a function , that  variable is local, and can only be  used inside that function  
# to create  a globle variable inside a function , you can use the globle keyword.
def myfunc():
 global x 
 x = "creatures"
myfunc()
print("python is "+ x)

# to change the value of a global variable inside a function , refer to the variable by using the global keyword

x = "awesome"
def myfunc():
 global x 
 x = "fantastic"
 myfunc()
print("python is " + x)