#Python Sets

myset = {"a", "b", "c"}

##Set

thisset = {"apple", "banana", "cherry"}
print(thisset)

##Set Items

##Duplicates Not Allowed

#1)

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

##Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:

#2)

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

##Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:

#3)

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

#False and 0 is considered the same value:

#Get the Length of a Set

thisset = {"apple", "banana", "cherry"}

print(len(thisset))

##Set Items - Data Types

#1)

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#2)

set1 = {"abc", 34, True, 40, "male"}

##type():

##<class 'set'>

myset = {"apple", "banana", "cherry"}
print(type(myset))

#The set() Constructor

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)




#Python - Access Set Items

#1)

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#2)

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#3)

thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)



#Python - Add Set Items
##Add Items


thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

##Add Sets

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

##Add Any Iterable

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)





#Python - Remove Set Items

##remove() method:

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)


##discard() method:

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#pop() method

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

#clear() method empties the set:

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)




#Python - Loop Sets

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)




#Python - Join Sets

##Union

#1)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#2)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

##Join Multiple Sets

##union() method:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)


#2)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)

##Join a Set and a Tuple

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

#3)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

##Intersection

##intersection() method 

#1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

#operator method.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

##intersection_update() method 

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

#2)

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)

##Difference

##difference() method

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

##operator method

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)

##difference_update() method 

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)

##Symmetric Differences

##The symmetric_difference() method

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

##^ operator instead 

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)

##symmetric_difference_update() method 

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)
