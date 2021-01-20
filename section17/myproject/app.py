from flask import Flask, render_template, request
app = Flask(__name__)

class Item():
	def __init__(self, name, amount):
		self.name = name
		self.amount = amount

@app.route("/")
def hello():
	#items = [
    #	Item("Apple", 5),
    #	Item("Computer", 1),
    #	Item("Pear", 4)

    items = [
    	{"name":"Apple", "amount": 5},
    	{"name":"Computer", "amount": 1},
    	{"name":"Pear", "amount": 4}
    ]
    
    #for item in items:
    #	item["amount"] = item["amount"] * 2

    person = ("John", "Doe")

    output = render_template("start.html", person=person, items=items)
    return output

@app.route("/test")
def test():
	args = request.args
	name = args.get("name")
	age1 = args.get("age")
	return render_template("test.html", name=name, age=age1)

@app.route("/currency")
def currency():
	currency1 = request.args.get("currency1", "USD")
	currency2 = request.args.get("currency2", "Euro")
	rate = float(request.args.get("rate", 0.87))

	table1 = []
	for x in range(1,50):
		table1.append((x, round(x*rate,2)))

	table2 = []
	for x in range(1,50):
		table2.append((x, round(x/rate,2)))

	return render_template("currency.html", currency1=currency1, currency2=currency2, rate=rate, table1=table1, table2=table2)