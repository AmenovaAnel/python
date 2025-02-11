#1

import math  

deg = float(input("Input degree: "))  
rad = math.radians(deg)  
print(f"Output radian: {rad:.6f}")  


#2

h = float(input("Height: "))  
a = float(input("Base, first value: "))  
b = float(input("Base, second value: "))  

s = ((a + b) / 2) * h  
print(f"Expected Output: {s:.1f}")  


#3

import math  

n = int(input("Input number of sides: "))  
s = float(input("Input the length of a side: "))  

area = (n * s**2) / (4 * math.tan(math.pi / n))  
print(f"The area of the polygon is: {area:.1f}")  


#4

b = float(input("Length of base: "))  
h = float(input("Height of parallelogram: "))  

area = b * h  
print(f"Expected Output: {area:.1f}")  
