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
