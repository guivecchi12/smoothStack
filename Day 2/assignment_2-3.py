# Coding Exercise 6:
#   Make a list of at least 4 people
#   Write an if test that prints a message about the room being crowded, if there are more than 3 people in your list
#   Modify your list so that there are only two people in it. Use on of the methods for removing people from the list, dont just redefine the list.
#   Run your if test again. There should be no output this time, because there are less than 3 people in the list.
#   Bonus: Store your if test in a function called something like crowd_test

def crowd_test1(lst):
    if len(lst) > 3:
        while len(lst) > 2:
            lst.pop()
        print(lst)

# Save your program from Three is a Crowd under a new name.
# Add an else statement to your if tests. If the else statement is run, have it print a message that the room is not very crowded

def crowd_test2(lst):
    if len(lst) > 3:
        while len(lst) > 2:
            lst.pop()
        print(lst)
    else:
        print('Room is not very crowded')

# Six is a mob
#   Save your program from Three is a Crowd - Part 2 under a new name.
#   Add some names to your list, so that there are at least six people in the list
#   Modify your tests so that
#       If there are more than 5 people, a message is printed about there being a mob in the room
#       If there are 3-5 people, a message is printed about the room being crowded.
#       If there are 1 or 2 people, a message is printed about the room not being crowded.
#       If there are no people in the room, a message is printed about the room being empty

def crowd_test(lst):
    if len(lst) > 5:
        print('There is a mob in the room')
    elif len(lst) >= 3:
        print('Room is being crowded')
    elif len(lst) > 0:
        print('Room is not crowded') 
    else:
        print('Room is empty')

lst = ['a', 'b', 'c', 'd', 'e', 'f']
crowd_test(lst)
