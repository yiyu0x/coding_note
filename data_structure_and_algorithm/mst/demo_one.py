import tkinter as tk
from graphviz import Digraph

def draw(dataBox):
	print("hi")
	dataBox = dataBox.split(',')
	dot = Digraph(comment='demo_one')
	sumOfnode = len(dataBox)

	# create node
	for i in range(len(dataBox)):
		dot.node(str(i),str(i))

	edgeVector = []
	# create edge
	for source,data in enumerate(dataBox):
		for destination,connect in enumerate(data):
			if connect == '1':
				edgeVector.append([source,destination])
				# print("source:",source,"destination:",destination)
				# dot.edge(str(source),str(destination))
	print(edgeVector)
	for source,destination in edgeVector:
		if [destination,source] in edgeVector:
			dot.edge(str(source),str(destination),dir='both')
			edgeVector.remove([destination,source])
		else:
			dot.edge(str(source),str(destination))

	dot.view()

def getText():
	inputData = textField.get()
	draw(inputData)

window = tk.Tk()
window.title('demo one')

textField = tk.Entry(window)
textField.pack()
button1 = tk.Button(window,text="draw",width=15,height=2,command=getText)
button1.pack()

window.mainloop()