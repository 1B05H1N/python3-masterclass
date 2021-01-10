"""
Exercise Exceptions

Good luck with these exercises :)

When you have finished this exercise sheet, you can use the sample solution in text form (File: Exercise Exceptions (Sample Solution)).

The video sample solution (in the next lesson) is particularly detailed. If you have solved everything correctly, it is perfectly okay if you skip this lesson then.
"""
"""
Task

Your time in the math magician's online shop is coming to an end - you're ready for bigger tasks! But you should make sure that even less competent users of your code will not spoil the shop...

a.)

Write an exception that catches the error when someone tries to open the following file that does not exist in this directory! In this case, output the message "File not found". Also make sure to open the file with a suitable construct if it does exist in the future - without errors because the file was not closed correctly.
"""

try:
  file = open("do_not_open.txt", "r")
  print(file)
except FileNotFoundError:
  print("File not found") 

"""
b.)

See what type of error occurs when executing the following code. Catch the error with try except and output an appropriate error message!
"""

articles = ["Invisible Keyboard", "Holographic Display", "Magic Mirror"]

prices = {"Invisible Keyboard": 150, "Holographic Display": 1150}

def print_prices():
  for article in articles:
    print(prices[article])
try:
  print_prices()
except KeyError:
  print("key is missing")

"""
c.)

Finally, you create an error class that is called if d is an empty dictionary. Then an EmptyDictionaryError should occur with the hint that the dictionary d contains no element.
"""

d = {}

if len(d) == 0:
  raise EmptyDictionaryError("d contains no element")

class EmptyDictionaryError(Exception):
  pass

# well done :) 