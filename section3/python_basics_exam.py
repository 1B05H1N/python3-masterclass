"""
Completion of Python Basics

Take your time to complete these tasks carefully. Good luck! :)

When you have finished this exercise sheet, you can use the sample solution in text form (File: Compare Python Fundamentals (sample solution))

The video sample solution (in the next lesson) is partially detailed. If you have solved everything correctly, it is perfectly okay if you skip this lesson then. 
"""

""""
 1.) An automated trick

a.) 
A mathemagician asks you to automate one of her tricks with a small program. The trick starts as follows: 

1. think of a number (variable number). 
2. multiply it by two. 
3. add 10 to the result.
4. divide the result by 2

Perform this calculation for the variable number and output the result. 

number = 6

# Write the calculation in the following line 
result = 0 

print(result)

0 

Suggestion: These exercises are about the Python code. 

So your task is to adjust the Python code above so that the calculation from the task is calculated correctly, and you can check whether the correct output then comes out with the "correct output" under this text. This is not about the result, but about the way / Python code ;) 

The notebook "Python Fundamentals (sample solution)" also contains the finished Python code - but I would recommend you try developing the Python code yourself first. 

Correct output (need not be colored):

11.0 
"""

number = 6

# Write the calculation in the following line
result = (((number * 2) + 10) / 2) # number variable is multiplied by 2, 10 is added and then the total is divided by 2

print(result) 


"""
b.)
When she sees this, the mathematician turns up her nose: The result is still displayed as a decimal number. 

Convert the result to an integer before you print it. 

# Output the result of the calculation here as an integer. 

Correct output (no need not to be colored):

11
"""

print(int(result)) # the variable is changed to an integer with the int() function 

"""
c.) 
The mathematician points out that magic tricks also depend on presentation. Now give an answer sentence of the form

"You chose 6, the magical result is 11!"

where the variable number is to be used for the number 6 and the result (variable result) for the number 11. 

Note:***In Python a print - command may go over several lines as follows. This could be handy, especially if you want to put many strings in a row:

print("Hello" +
		"World")

# Print the magic trick as a sentence

Correct output: 

	You have chosen 6, the magical result is 11!

"""

print("You have chosen 6, the magical result is " + str(int(result)) + "!") # concatenating the sentence with a converted string converted from an int 

"""
Task 2: Sawed e-mail addresses

The mathemagician is very happy with your work and asks you for help with her online shop. She only knows the mail addresses of her customers and you should create a simplified directory with their names based on the mail addresses.
a. ) Draw a name from a email address in the form name@service.com

If the email address is Max-Mustermann@gmail.com, you should output Max-Mustermann; if the mail address is KlaraKlarnamen@uni-berlin.de, you should output KlaraKlarnamen.

Note: Be sure to check the .split() method again. This allows you to saw / split an e-mail address at the @ symbol, for example.

email = "willy.wizard@magicalschool.com"

correct output: 

	willy.wizard
"""

email = "willy.wizard@magicalschool.com"

print(email.split("@")[0]) # evoke split function to remove everything after the "@" for the only value in the list 

"""
b.) Draw a name from an email address in the form info@name.com

Sometimes the names of a mail address are only after the @-sign. Also print the names for such cases; remove the ending .com or .de. You may assume that there is no period within the name. If the mail address is info@Max-Mustermann.com, you should output Max-Mustermann.

Note:*** It is okay if you need several .split() - functions for the calculation, or if you want to cache a result. You are also welcome to use the code from the a) subtask here.

mail = "info@helena-witch.com"

# Ouput the last part of the given email address here
"""

mail = "info@helena-witch.com"

# Ouput the last part of the given email address here

print(mail.split("@")[1].split(".")[0]) # splits value into 2 list items, splits everything after the period for the 2nd list item and then displays the 1st item

"""
c.) Calculate: How many customers are there in the online shop?

Currently, all customers (mail1, mail2, mail3) str present as separate variables. We would like to build a list from it now, so that we would have the possibility to add further customers to this list later.

Therefore transfer the customers mail1, mail2 and mail3 to the list clients and get the number of elements of the list clients printed using Python.

mail1 = "zarah.magic@magicberg.de"
mail2 = "info@trixie-trickser.com"
mail3 = "uwe_evil@darknet.de" 

clients = []

# Add mail1, mail2, mail3 to the clients list

print(clients)
[]

['zarah.magic@magicberg.de', 'info@trixie-trickser.com', 'uwe_evil@darknet.de']
"""

mail1 = "zarah.magic@magicberg.de"
mail2 = "info@trixie-trickser.com"
mail3 = "uwe_evil@darknet.de" 

clients = []

# Add mail1, mail2, mail3 to the clients list
clients.append(mail1)
clients.append(mail2)
clients.append(mail3)

print(clients)

# Enter here the number of elements in the clients list

print(len(clients))

"""
d.) Assemble an email address from strings

Suddenly the mathematician remembers that her most important online shop customer is still missing from the clients list. The information about him was sawn into two parts during a failed trick and since then lies around in the list ["stageMagic", "magic.com"].

Use Python to reconstruct the customer's e-mail address (there is no @ between "stage magician" and "magic.com") and print it so that the online shop customer service can inquire about his or her well-being.

magician = ["stageMagic", "magic.com"]

# add code here

Desired output:

stageMagic@magic.com
"""

magician = ["stageMagic", "magic.com"]

# add code here
print(magician[0] + "@" + magician[1]) # way I did it
print("@".join(magician)) # way they wanted me to do it

# Well done! :) 