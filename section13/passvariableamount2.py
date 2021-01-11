def f(**args):
	print(args)


f(key="value", key2="value2") 

def g(key, param2):
	print(key)
	print(param2)

d = {"key": "I am the key", "param2":"I am a parameter"}

g(key=d["key"], param2=d["param2"])
g(**d)

import matplotlib.pyplot as plt

def create_plot(**plot_params):
	plt.plot([1,2,3],[5,6,5], **plot_params)
	plt.show()

create_plot(color="r", linewidth=7, linestyle="dashed")