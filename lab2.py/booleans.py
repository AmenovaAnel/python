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