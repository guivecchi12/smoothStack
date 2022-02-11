import math

def main():
# Coding Excercise 2:

    # 1. Numbers: Example code to add two numbers 50 + 50 and 100 - 10 and print it
        num1 = 50 + 50
        num2 = 100 - 10
        print(num1, num2)

    # 2. Python does not have a +* operation so 30+*6 returns an error

    # 3. Print "Hello World" on the console output. Print output "Hello World : 10" Make sure capitalization and spacing matches.
        print("Hello World")
        print("Hello World :", 10)

    # 4. Mathematical calculation excercise:
        def monthlyPayments(p, r, l):
            monthly = (p * (r/12) / 100) / (1 - (1 / (1 + (r/12)/100)**l)) 
            return math.ceil(monthly)

        print(monthlyPayments(800000, 6, 103))
main()