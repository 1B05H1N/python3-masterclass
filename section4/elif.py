# elif is the short form of else if

currency = "euro"

if currency == "usd":
	print("US-Dollar")
else:
	if currency == "yen":
		print("Japanese yen")
	else:
		if currency == "euro":
			print("euro")
		else:
			if currency == "baht":
				print("thai baht")

currency = "euro"

if currency == "usd":
	print("US-Dollar")
elif currency == "yen":
	print("Japanese yen")
elif currency == "euro2":
	print("euro2")
elif currency == "baht":
	print("thai baht")

if currency == "euro":
	print("euro2")
