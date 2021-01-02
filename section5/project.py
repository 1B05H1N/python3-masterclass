# twitter bot

# Excursus: Random Numbers

# We can generate random numbers in Python with the randint() function. But to use this function, we first have to integrate the random module. :)

import random

# randint randomly returns integers from an interval that we have to tell the function. The two limits and all integers within the interval can be values of randint

# print(random.randint(0, 4))

# print(random.randint(0, 4))

# creating lists of terms for our tweets
# here we just copied some common terms from the tweets ;)

part1 = ["Putin,", "Hillary,", "Obama,", "Fake News,", "Mexico,", "Arnold Schwarzenegger,", "The Democrats,"]
part2 = ["no talent,", "on the way down,", "really poor numbers,", "nasty tone,", "looking like a fool,", "bad hombres,"]
part3 = ["got destroyed by my ratings.", "rigged the election.", "had a much smaller crowd.", "will pay for the wall."]
part4 = ["So sad", "Apologize", "So true", "Media won't report", "Big trouble", "Fantastic job", "Stay tuned"]
part5 = [", China virus", ", Kung Flu" , ", Antifa", ", Fake news media"]

# we can create lists from other lists
best_words = [part1, part2, part3, part4, part5]
# print(best_words)

# building the tweet generator

"""
for part in best_words:
	print(len(part))
	r = random.randint(0, len(part) -1)
	print(part)
	print(r)
"""

"""
for part in best_words:
	print(len(part))
	r = random.randint(0, len(part) -1)
	print(part[r])
"""

sentence = []

for part in best_words:
	r = random.randint(0, len(part) -1)
	sentence.append(part[r])

# print(sentence)
print(" ".join(sentence) + "!")

