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