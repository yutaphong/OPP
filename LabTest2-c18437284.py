# Lab test 2
# Writer: C18437284
# Date: 12:12:19
# compile: onlinegdb

# write a python class to Represnt a 3D Vector
#   A) __add__ vector x+a, y+b, z+c 
#   B) __sub__ vector x-a, y-b, z-c
#   C) __mul__ vector x*n, y*n, z*n
#       n is an integer
#   D) magnitude Vector x^2+y^2+z^2

import math

class Vector:

	def __init__(self, x, y, z):
		self.x = float(x)
		self.y = float(y)
		self.z = float(z)
		
	def __init__(extra, a, b, c):
		extra.a = (a)
		extra.b = (b)
		extra.c = (c)

    # Represntation
	def __str__(self):
		return "({:f}, {:f}, {:f})".format(self.x,self.y,self.z)
		

	def __str__(extra):
		return "({:f}, {:f}, {:f})".format(extra.a,extra.b,extra.c)

	# Addition
	def __add__(self,extra):
		return Vector(self.x+extra.a, self.y+extra.b, self.z+extra.c)

	# Subtraction 
	def __neg__(self,extra):
		return Vector(self.x-extra.a, self.y-extra.b, self.z-extra.c)

	
	# Scalar Multiplication
	def __mul__(self, extra):
		return Vector(self.x * extra, self.y * extra, self.z * extra)

	def __rmul__(self, extra):
		return self.__mul__(extra)
		
    # magnitude of vector
	def magnitude(self):
		return math.sqrt((self.x*self.x)+(self.y*self.y)+(self.z*self.z))

# Calling
v1 = Vector(1, 2, 3)
v2 = Vector(5, 5, 5)

print ("Printing v1")
print ("v1 = ", v1)

print ("Printing v2")
print ("v2 = ", v2)

v3 = v1+v2
print ("Printing addition")
print("v1 + v2 = ", v3)

v4 = v1 - v2
print ("Printing subtraction")

print("v1 - v2 = ", v4)
print ("Printing dot product")

v5 = v1 * v2
print("v1 * v2 = ", v5)

print ("Printing integer multiplication")

v6 = v1 * 2.5
print("v1 * 2.5 = ", v6)

print("v1 magnitude is ", v1.magnitude())







