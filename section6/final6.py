
"""
Challenge Paper - Functions

It's time for another exercise sheet! This exercise sheet is about functions, etc. :)

You can find this exercise sheet in the course materials you downloaded in the first section. It is located in the folder "06 - Functions", the file is called "Final exercise functions".

Have fun with the tasks :)

Final exercise about functions

Take your time to complete the tasks carefully. :-) Good luck!

When you have finished this exercise sheet, you can use the sample solution in text form (File: Compare Final exercise functions (sample solution)).

The video sample solution (in the next lesson) is particularly detailed. If you have solved everything correctly, it is perfectly okay if you skip this lesson then.
"""

"""
 functional online shop

The math magician wants to convert her online shop to functions. So there's a lot of work waiting for you.

a.) Write a function that calculates the total price of the products in the shopping cart!

Complete the function list_sum(), to which a list with the prices is passed as a parameter. The function should then output the sum of the numbers from the list.
"""

cart_prices = [20, 3.5, 6.49, 8.99, 9.99, 14.98]

def list_sum(list): # defining function with list argument 
    sum = 0 # creating placeholder variable
    for i in list: # iterate through list and add each list value, for every single item add the next in the list until done
    	sum = sum + i

    print(sum)
    
list_sum(cart_prices)


print("\n")

"""
b.) Write a function that creates a price table for an item!

Now the math magician wants a function to which she can pass an item name and the sales price. From this, the function has to print a list of the sum of one, two, three,... up to ten units prices. Each element in the list should look like this: "Number x articles: Price".

You're just wondering about the math magician's demands for short time.
"""

def prices_list(name, price):
    # this is where your code goes. replace the next line with your code.
    l = [] # create empty list
    for i in range(1,11): # go through range 1-10 -- 11 is not iterated
    	l.append(str(i) + " x " + name + ": " + str(price * i)) 
    return l

print(prices_list("Cookie", 0.79))


"""
c.) Write a function that fills the lists with the articles!

From now on, a function should also put the goods on the virtual shelves, i.e. put them in the first, still empty position in the shelf list. The article should be passed to the function add_shelf() as parameter. The function then updates the shelf list, and the new article was placed in the first empty shelf.
"""

shelf = ["Magic Mirror", "empty", "Cookie", "Book with Magic Tricks", "empty"]

def add_shelf(article):
    for i in range(0, len(shelf)):
    	if shelf[i] == "empty":
    		shelf[i] = article
    		break

add_shelf("Rubik's Cube")
add_shelf("Skate board")
print(shelf)

