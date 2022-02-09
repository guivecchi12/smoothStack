# Coding Exercise 9:

# 1. Imagine an accounting routine used in a book shop. It works on a list with sublists, which look like this: 
#   
#   Order Number	Book Title and Author	            Quantity	Price per Item
#   34587	        Learning Python, Mark Lutz	            4	        40.95
#   98762	        Programming Python, Mark Lutz	        5	        56.80
#   77226	        Head First Python, Paul Barry	        3	        32.95
#   88112	        Einführung in Python3, Bernd Klein	    3	        24.99
orders = [[34587, 'Learning Python, Mark Lutz', 4, 40.95],[98762, 'Programming Python, Mark Lutz', 5, 56.80],
[77226, 'Head First Python, Paul Barry', 3,32.95], [88112, 'Einführung in Python3, Bernd Klein', 3, 24.99]]

# 2. Write a Python program, which returns a list with 2-tuples. Each tuple consists of a the order number, the product of the price per items and the quantity. The product should be increased by 10,- € if the value of the order is smaller than 100,00 €. Write a Python program using lambda and map.
def toTuple(order_list):
    order = lambda quantity, price: round(quantity * price, 2)
    order_total = order(order_list[2], order_list[3])

    if  order_total < 100:
        order_total += 10

    return (order_list[0], order_total)

my_list = list(map(toTuple, orders))
# print(my_list)

# 3. 3.	The same bookshop, but this time we work on a different list. The sublists of our lists look like this: 
# [ordernumber, (article number, quantity, price per unit), ... (article number, quantity, price per unit) ] 
# Write a program which returns a list of two tuples with (order number, total amount of order).
orders = [[123, ('article 1', 3, 4.50), ('article 2', 4, 50.5)], [124, ('article 1', 5, 4.50), ('article 2', 7, 14.50)] ]

def bookshop(order_list):
    total = 0
    for i in order_list:
        if type(i) == tuple:
            total += (i[1] * i[2])

    return (order_list[0], total)

my_list = list(map(bookshop, orders))
print(my_list)