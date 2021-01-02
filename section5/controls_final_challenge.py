"""
Conclusion of control structures

Take the time to complete the tasks carefully. :-) Good luck!

When you have finished this exercise sheet, you can use the sample solution in text form (File: Closure Control Structures (Sample Solution)).

The video sample solution (in the next lesson) is particularly detailed. If you have solved everything correctly, it is perfectly okay if you skip this lesson then.
"""

"""
1st task: Continents
a.) Output all continents from the continents list one after the other.
"""

continents = ["Africa", "Antarctica", "Asia", "Australia and Oceania", "Europe", "North America", "South America"]

# Enter your code here

for continent in continents:
	print(continent)
	continue

"""
Africa
Antarctica
Asia
Australia and Oceania
Europe
North America
South America
"""

"""
b.) Output only the inhabited continents from the continents list.

Note:: Antarctica is uninhabited. So you can skip this continent at the output
"""
print(" ")

for continent in continents:
	if continent == "Antarctica":
		continue
	print(continent)

"""
c.) Output only the continents from the stuff list.

You can loop through the list stuff and then use the variable continents to check if an element of the list stuff also appears in the list continents.
"""

print(" ")

stuff = ["Asia", "Max", 101, "Monika", "China", "Zimbabwe", "Antarctica"]

for element in stuff: 
	if element in continents:
		print(element) 

"""
d.) How many continents are included in the list stuff?

Write a loop to count the number of continents in the stuff list and then output this value.
"""

print(" ")

count = 0 

for i in stuff: 
	if i in continents:
		if i in continents:
			count = count + 1
print(count)

print("Alternatively")

counts = []

for i in stuff:
	if i in continents:
		counts.append(i)

print(len(counts))

"""
2nd task: Discount campaign

Back to the mathemagician: She wants to start a discount campaign in her shop to boost her business. Of course, she has something to program for you again. You should simplify the calculation of the reduced prices with an if-elif-else structure.

Note the following:

Items costing between 0 and 20 thalers (inclusive) will be reduced by 20%; items costing between 20 (not inclusive) and 50 thalers (inclusive) will be reduced by 40%. All other items, i.e. items costing more than 50 thalers, will be reduced by 60%.
a.) Output the new discounted price for the price variable.
"""

print(" ")

price = 50

if price <= 20:
	price = price * 0.8
elif price <= 50:
	price = price * 0.6
else:
	price = price * 0.4

print(price)

"""
b.) Now calculate for each of the old prices from the prices list the appropriate reduced prices and save them in the new_prices list. Finally output this list.
"""

print(" ")

prices = [2, 50, 70, 30]
new_prices = []

for price in prices:
	if price <= 20:
		price = price * 0.8
	elif price <= 50:
		price = price * 0.6
	else:
		price = price * 0.4

	new_prices.append(price)

print(new_prices) 

"""
c.) Additional task (difficult!)

Now the mathematician presents you with trembling hands with the list chaos, in which new and old prizes are mixed! In the face of this ill-considered work, you clench your hands in front of your head, but it doesn't help: Only you can restore order here by bringing together everything you have already learned!

Scroll through the items in the chaos list. With a new price, simply drag the new value from the string and append it to the order list. With an old price, however, you get the old value, calculate the new price and add this value to the order list.

Finally, output the complete order list, which only contains new prices (and only numbers!).

Tip: With the in operator you can check if old or new appears in a list item (old" in "old price: 123") and decide if you want to make the discount or not.
"""

print(" ")

chaos =["old price: 40", "new price: 21", "old price: 29", "old price: 50", "new price: 101"]
order = []

# Enter your code here

for i in chaos:

	price = int((i.split(": ")[1]))

	if "old" in i:
		if price <= 20:
			price *= 0.8
		elif price <= 50:
			price *= 0.6
		else:
			price *= 0.4
	    
	order.append(price)

print(order)