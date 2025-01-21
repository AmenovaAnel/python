#PYTHON SYNTAX

#Ex1

print("Hello World")

#Ex2

if 5 > 2:
 print("YES")



#PYTHON VARIABLES

 x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#casting, to specify

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0 

#double quotes

x = "John"
# is the same as
x = 'John'

#This will create two variables:

a = 4
A = "Sally" #A will not overwrite a

#python variables: names

#legal variables names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)


#illegal variables names
# 2myvar = "John"  
# my-var = "John"  
# my var = "John" 

#Multi Words Variable Names

#Camel Case
#Each word, except the first, starts with a capital letter:

myVariableName = "John"
#Pascal Case
#Each word starts with a capital letter:

#MyVariableName = "John"
#Snake Case
#Each word is separated by an underscore character:

#my_variable_name = "John"

#Python Variables - Assign Multiple Values

#Many Values to Multiple Variables

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


#One Value to Multiple Variables

x = y = z = "Orange"
print(x)
print(y)
print(z)
#Unpack a Collection

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Python - Output Variables

x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#output multiple variables:

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#mathematical operator:

x = 5
y = 10
print(x + y)
#an error:

x = 5
y = "John"
print(x + y)

#best way to output it

x = 5
y = "John"
print(x, y)

#Python - Global Variables

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#local

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


#The global Keyword

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# if you want to change a global variable inside a function.

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)



#PYTHON COMMENTS

#Ex1

#This is a comment

#Ex2

#This is a comment
#written in
#more than just one line
print("Hello, World!")

#Ex3

"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")



#PYTHON DATA TYPES

#Ex1

x = 5
print(type(x))

int

#Ex2

x = "Hello World"
print(type(x))

str


#Ex3

x = 20.5
print(type(x))

float


#Ex4

x = ["apple", "banana", "cherry"]
print(type(x))

list

#Ex5

x = ("apple", "banana", "cherry")
print(type(x))

tuple

#Ex6

x = {"name" : "John", "age" : 36}
print(type(x))

dict

#Ex7

x = True
print(type(x))

bool



#PYTHON NUMBERS

#Ex1

x = 5
x = float(x)

#Ex2

x = 5.5
x = int(x)

#Ex3

x = 5
x = complex(x)



#PYTHON CASTING

#EX1

#Integers:

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

#ex2

#Floats:

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

#ex3

#Strings:

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'


#PYTHON STRINGS

#Escape Character

#an error 

# - txt = "We are the so-called "Vikings" from the north.

#The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."



#String Concatenation

a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

#Python - Format - Strings

#we cannot combine strings and numbers like this:

age = 36
txt = "My name is John, I am " + age
print(txt)


#F-Strings

age = 36
txt = f"My name is John, I am {age}"
print(txt)

#Placeholders and Modifiers

price = 59
txt = f"The price is {price} dollars"
print(txt)

#include a modifier 

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
#include math operations:

txt = f"The price is {20 * 59} dollars"
print(txt)

#Python - Modify Strings


#Upper Case

a = "Hello, World!"
print(a.upper())

#Lower Case

a = "Hello, World!"
print(a.lower())

#Remove Whitespace

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#Replace String

a = "Hello, World!"
print(a.replace("H", "J"))

#Split String

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#Python - Slicing Strings

#Slicing

b = "Hello, World!"
print(b[2:5])
#Note: The first character has index 0.

#Slice From the Start

b = "Hello, World!"
print(b[:5])

#Slice To the End

b = "Hello, World!"
print(b[2:])

#Negative Indexing

b = "Hello, World!"
print(b[-5:-2])


#Strings

print("Hello")
print('Hello')

#Quotes Inside Quotes

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#Assign String to a Variable

a = "Hello"
print(a)

#Multiline Strings

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Or three single quotes:

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)



#Strings are Arrays

a = "Hello, World!"
print(a[1])

#Looping Through a String

for x in "banana":
  print(x)

#String Length

a = "Hello, World!"
print(len(a))

#Check String

txt = "The best things in life are free!"
print("free" in txt)

#Use it in an if statement:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#Check if NOT

txt = "The best things in life are free!"
print("expensive" not in txt)

#Use it in an if statement:

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
