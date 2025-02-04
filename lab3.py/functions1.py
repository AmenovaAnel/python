#1

def grams_to_ounces(grams):
    return 28.3495231 * grams

print(grams_to_ounces(5))


#2

def Fahrenheit_to_centigrade(F):
    return (5 / 9) * (F - 32)

print(Fahrenheit_to_centigrade(65))


#3

def solve(numheads, numlegs):
    for chickens in range(numheads + 1):  
        rabbits = numheads - chickens  
        if (chickens * 2 + rabbits * 4) == numlegs:  
            return chickens, rabbits  

chickens, rabbits = solve(35, 94)
print("Курицы:", chickens)
print("Кролики:", rabbits)


#4

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers


#5

import itertools

def string_permutations():
    user_input = input("Enter a string: ")
    permutations = itertools.permutations(user_input)
    for perm in permutations:
        print(''.join(perm))


#6

def reverse_words():
    user_input = input("Enter a sentence: ")
    words = user_input.split()  
    reversed_words = words[::-1]  
    return ' '.join(reversed_words)  


#7

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

#8

def spy_game(nums):
    code = [0, 0, 7]
    index = 0
    for num in nums:
        if num == code[index]:
            index += 1
        if index == len(code):  # We found the full sequence
            return True
    return False


#9

import math

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3


#10

def unique_elements(lst):
    unique_lst = []
    for element in lst:
        if element not in unique_lst:
            unique_lst.append(element)
    return unique_lst

#11

def is_palindrome(s):
    s = s.replace(" ", "").lower() 
    return s == s[::-1]

#12

def histogram(lst):
    for num in lst:
        print('*' * num)

#13

import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    number_to_guess = random.randint(1, 20)
    
    attempts = 0
    guessed = False
    
    while not guessed:
        print("Take a guess.")
        guess = int(input())
        attempts += 1
        
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            guessed = True
    
    print(f"Good job, {name}! You guessed my number in {attempts} guesses!")