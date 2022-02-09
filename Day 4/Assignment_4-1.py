#Coding Exercise 8:

#1. Create a function func() which prints a text ‘Hello World’
from asyncio.windows_events import NULL


def func():
    print('Hello World')

#2. Create a function which func1(name)  which takes a value name and prints the output “Hi My name is Google’
def func1(name):
    print('Hi My name is ' + name)

#3. Define a function func3(x,y,z) that takes three arguments x,y,z where z is true it will return x and when z is false it should return y . func3(‘hello’goodbye’,false)
def func3(x,y,z):
    if z:
        return x
    else:
        return y

func3('hello', 'goodbye', False)

#4. Define a function func4(x,y) which returns the product of both the values.
def func4(x,y):
    return x + y

#5. Define a function called as is_even that takes one argument , which returns true when even values is passed and false if it is not.
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

#6. Define a function that takes two arguments, and returns true if the first value is greater than the second value and returns false if it is less than or equal to the second.
def is_greater(x,y):
    return x > y

#7. Define a function which takes arbitrary number of arguments and returns the sum of the arguments.
def sum_args(*args):
    sums = 0
    for arg in args:
        sums += arg 
    return sums

#8. Define a function which takes arbitrary number of arguments and returns a list containing only the arguments that are even.
def even_args(*args):
    even = []
    for arg in args:
        if arg % 2 == 0:
            even.append(arg)
    return even

#9. Define a function that takes a string and returns a matching string where every even letter is uppercase and every odd letter is lowercase 
def string_manipulation(word):
    word = str(word)
    my_string = ''
    for index, i in enumerate(word):
        if index % 2 == 0:
            my_string += i.upper()
        else:
            my_string += i.lower()

    return my_string

#10. Write a function which gives lesser than a given number if both the numbers are even, but returns greater if one or both or odd.
def lesser(x, y):
    if x % 2 == 0 and y % 2 == 0:
        return 'lesser'
    else:
        return 'greater'

#11. Write a function which takes  two-strings and returns true if both the strings start with the same letter.
def same_start(a, b):
    return a[0].lower() == b[0].lower()

#12. Given a value,return a value which is twice as far as other side of 7
def twice_from_seven(val):
    return abs((val - 7) * 2)

print(twice_from_seven(5))

#13. A function that capitalizes first and fourth character of a word in a string.
def cap_first_and_fourth(word):
    my_string = ''
    for index, l in enumerate(word):
        if index == 0 or index == 3:
           my_string += l.upper()
        else:
            my_string += l
    return my_string

