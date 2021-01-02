for i in range(0, 10):
	if i == 3:
		print("i skips 3")
		continue # goes to the next iteration/run of the list
	print(i)
	print("After the if statement")


for i in range(0, 10):
	if i == 3:
		print("i breaks at 3")
		break # stop/brake on 3
	print(i)

# for loop to add sum of weights
list_with_weight = [55, 36, 59, 129, 59]
total_weight = 0
for element in list_with_weight: 
	total_weight = total_weight + element
	print(total_weight)
	if total_weight < 200:
		print("elevator is full, last person who entered should get out.")
		break