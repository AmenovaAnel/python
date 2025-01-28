#PYTHON BOOLEANS

##booleans values

print(19 > 18)
print(19 == 18)
print(19 < 18)

##messages

a = 2025
b = 1025

if b > a:
  print("b is older than a")
else:
  print("b is not older than a")

##evaluate values and variables

x = "Bye"
y = 19

print(bool(x))
print(bool(y))

##true values

bool("idk")
bool(500)
bool(["carrot", "onion", "potato"])

##false values

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

##another false value

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

##another true value

#1) 

def myFunction() :
  return True

print(myFunction())

#2)

def myFunction() :
  return True

if myFunction():
  print("uh huh")
else:
  print("nuh uh")

#3)

x = 1000
print(isinstance(x, int))




#PYTHON OPERATOES

print(12 + 9)

##operator Precedence

#1)

print((12 + 9) - (34 - 89))

#2)

print(100 + 5 * 3)

#3)

print(345 + 456546 - 5465467 + 349594)




#PYTHON LISTS

thislist = ["socks", "jeans", "shoes"]
print(thislist)

##duplicates

thislist = ["hat", "hat", "hat", "dress", "jeans"]
print(thislist)

##list Length

thislist = ["socks", "t-shirt", "blouse"]
print(len(thislist))

##data Types

#1)

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#2)

list1 = ["abc", 34, True, 40, "male"]

##type()

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

##list constructor

thislist = list(("apple", "banana", "cherry")) 
print(thislist)

##access list

thislist = ["carrot", "potato", "onion","tomato","pumpkin"]
print(thislist[4])

##negative indexing

thislist = ["carrot", "potato", "onion","tomato","pumpkin"]
print(thislist[-2])

##range of indexes

thislist = ["carrot", "potato", "onion","tomato","pumpkin"]
print(thislist[2:4])

##leaving one

#1)

thislist = ["carrot", "potato", "onion","tomato","pumpkin"]
print(thislist[:4])

#2)

thislist = ["carrot", "potato", "onion","tomato","pumpkin"]
print(thislist[2:])

##range of Negative Indexes

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

##check of items

thislist = ["carrot", "potato", "onion","tomato","pumpkin"]
if "carrot" in thislist:
    print("дай боже сил закрыть этот предмет")

##change items in list

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

##Change a Range of Item Values

#1)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#2)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#3)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

##insert items

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

##append(add)items

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

##insert(add)items

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

##extend(add)items

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

##add anything

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

##remove items 

#1)

thislist = ["good grades", "sleep", "health"]
thislist.remove("good grades")
print(thislist)

#2)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

##remove with pop()

#1)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#2)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#remove with del

#1)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#2)

thislist = ["apple", "banana", "cherry"]
del thislist

##remove with clear()

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

##loop lists

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

##loop through index

thislist = ["dad", "girl", "boy"]
for i in range(len(thislist)):
  print(thislist[i])

##loop with while

thislist = ["one", "two", "three"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

##loop with comprehension

thislist = ["cupcake", "cake", "bread"]
[print(x) for x in thislist]

##join lists

#1)

list1 = ["a", "u", "f"]
list2 = [2, 2, 7]

list3 = list1 + list2
print(list3)

#2)

list1 = ["a", "u" , "f"]
list2 = [2, 2, 87]

for x in list2:
  list1.append(x)

print(list1)

#3)

list1 = ["god", "save" , "me"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

##copy lists

#1)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


#2)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#3)

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

##sort lists

##Sort List Alphanumerically

#1)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#2)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

##Sort Descending

#1)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#2)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

##Customize Sort Function

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

##Case Insensitive Sort

#1)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#2)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

##Reverse Order

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

##List Comprehension

#1)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


#2)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#Condition

#1)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if x != "apple"]

print(newlist)

#2)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits]

print(newlist)

##Iterable

#1)

newlist = [x for x in range(10)]

print(newlist)

newlist = [x for x in range(10) if x < 5]

print(newlist)

##Expression

#1)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)

#2)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = ['hello' for x in fruits]

print(newlist)

#3)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)




#PYTHON FOR LOOPS

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

##Looping Through a String

for x in "banana":
  print(x)

##The break Statement

#1)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#2)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

##The continue Statement

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

##The range() Function

#1)

for x in range(6):
  print(x)

#2)

for x in range(2, 6):
  print(x)

#3)

for x in range(2, 30, 3):
  print(x)

##Else in For Loop

#1)

for x in range(6):
  print(x)
else:
  print("Finally finished!")

#2)

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

##Nested Loops

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

##The pass Statement

for x in [0, 1, 2]:
  pass




#Python While Loops

i = 1
while i < 6:
  print(i)
  i += 1

##The break Statement

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

##The continue Statement

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

##The else Statement

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")




#Python If ... Else

##If statement:

a = 33
b = 200
if b > a:
  print("b is greater than a")

##If statement, without indentation (will raise an error):

a = 33
b = 200
if b > a:
 print("b is greater than a") # you will get an error


##Elif

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

##Else

#1)

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#2)

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

##Short Hand If

a = 200
b = 33

if a > b: print("a is greater than b")

##Short Hand If ... Else

#1)

a = 2
b = 330
print("A") if a > b else print("B")

#2)

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

##And

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

##Or

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

##Not

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

##Nested If

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

##The pass Statement

a = 33
b = 200

if b > a:
  pass


















