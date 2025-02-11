#1

def squares(N):
    for i in range(N):
        yield i ** 2

N = int(input("Enter a number N: "))  

for num in squares(N):
    print(num)


#2

def even(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a number n: "))  
print(",".join(map(str, even(n))))


#3

def div_3_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter a number n: "))  

for num in div_3_4(n):
    print(num)


#4

def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2

a = int(input("Enter the start number (a): "))  
b = int(input("Enter the end number (b): "))  

for sq in squares(a, b):
    print(sq)


#5

def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Enter a number n: "))  

for num in countdown(n):
    print(num)
