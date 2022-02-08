# Coding Exercise 4

#1. Create a list with one number, one word and one float value. Display the output of the list
lst = [1, 'word', 2.3]
print(lst)

#2. I have a nested list [1,1[1,2]], how to grab the value of 2 from the list.
lst = [1,1,[1,2]]
print(lst[2][1])

#3. lst=['a','b','c'] what is the result of lst[1:]
    #Answer: ['b','c']

#4. Create a dictionary with weekdays an keys and week index numbers as values. Assign dictionary to a variable
week = {
    'Monday': 1,
    'Tuesday': 2,
    'Wednesday': 3,
    'Thursday': 4,
    'Friday': 5,
    'Saturday': 6,
    'Sunday': 7
}

#5. D={'k1':[1,2,3]} what is the output of d[k1][1]
#   Answer: You would get an error, you need to change k1 to a string ('k1') if you made that change you would then get 2

#6. Create a list [1,[2,3]] into a tuple
lst = [1,[2,3]]
tpl = tuple(lst)

#7. With a single set function can you turn the word 'Mississippi' to distinct character word.
mySet = set('Mississippi')

#8. Can you add X tot he above created set
mySet.add('X')

#9. Output of set([1,1,2,3])
    # Answer: {1,2,3}

# Question 1:
#   Find a all numbers between 2000 and 3200 (both included) that are divisible by 7 but not multiple of 5
answer = ()
for x in range(2000, 3201):
    if x % 7 == 0:
        if x % 5 != 0:
            answer += (x,)

# Question 2:
#   Write a program that can compute the factorial of a given numbers
#   The results should be printed in a comma-seperated sequence on a single line

def factorial():
    n = int(input("Find the factorial of: "))
    fact = 1
    for x in range(1, n+1):
        fact *= x
    print(fact)


# Question 3:
#   Create a function that takes 1 argument and creates a dictionary. Key's = 1 - n, Values = keys squared
def createDict():
    n = int(input("Choose the range of the dictionary "))
    dictionary = {}
    for x in range(1, n+1):
        dictionary[x] = x**2
    print(dictionary)

# Question 4:
#   Create a function that takes comma-separated numbers and returns those numbers in a list and a tuple
def lstAndTpl():
    n = input("Enter a list of comma-separated numbers ")
    lst = n.split(',')
    tpl = tuple(lst)
    print(lst)
    print(tpl)

# Question 5
#   Define a class with two methods:
#       getString: to get a string from console input
#       printString: to print the string in upper case

class MyString:
    def __init__(self):
        self.string = ''
    def getString(self):
        self.string = input("Add your string: ")
    def printString(self):
        print(self.string)

string = MyString()
string.getString()
string.printString()