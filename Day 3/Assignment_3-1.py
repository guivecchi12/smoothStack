import random
# Coding Exercise 7

#1. Write a Python program to find numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)
def findMultiple():
    for x in range(1500, 2700):
        if x % 7 == 0 and x % 5 == 0:
            print("Number found: ", x)

#2. Write a Python program to convert temperatures to and from celsius, fahrenheit.
def tempConverter(measurement, temp):
    if measurement == 'c':
        print(str(temp) + u"\N{DEGREE SIGN}C is " + str(round((temp * 9 / 5 + 32))) + " in Fahrenheit")
    elif measurement == 'f':
        print(str(temp) + u"\N{DEGREE SIGN}F is " + str(round((temp - 32) * 5 / 9)) + " in Celsius")
    else:
        print("Please enter either c or f for the measurement type")

#3. Write a Python program to guess a number between 1 to 9.
def guessGame():
    num = str(random.randrange(1,10))
    guess = input('Guess a number between 1 - 9: ')
      
    while num != guess:
        guess = input('Wrong! Guess again \nGuess a number between 1 - 9: ')
    
    print("Congratulations! You guessed correctly, your number was " + num)

#4. Write a Python Program to construct the following pattern, using a nested for loop.
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
def pattern():
    for x in range(1,6):
        print('*' * x)       
        if(x == 5):
            for y in range(4):
                print('*' * (4-y))
        

#6. Write a Python program that accepts a word from the user and reverse it.
def reverse():
    word = input("Enter a word to be reversed: ")
    rev = ''
    for i in word:
        rev = i + rev
    print (rev)

#7. Write a Python program to count the number of even and odd numbers from a series of numbers
def evenOdd(numList):
    even = 0
    odd = 0
    for x in numList:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1  
    print("Number of even numbers:", even)
    print("Number of odd numbers:", odd)

#8. Write a Python program that prints each item and its corresponding type from the following list. Sample List: datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0,-1), [5,12], {"class":'V, "section": 'A}]

def myType(datalist):
    for i in datalist:
        print(type(i))

myType([1452, 11.23, 1+2j, True, 'w3resource', (0,-1), [5,12], {"class":'V', "section": 'A'}])

#9. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
def continuePractice():
    for x in range(6):
        if x == 3 or x == 6:
            continue
        else:
            print(x)

continuePractice()