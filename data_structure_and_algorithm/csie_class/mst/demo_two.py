import tkinter as tk
import graphviz

def draw(dataBox):
	dataBox = dataBox.split('\n')
	dataBox.remove(dataBox[-1]) # because '\n' split create a redundant space
	sumOfnode = len(dataBox)

	dot = graphviz.Graph(comment='demo_two')

	# create node
	for i in range(sumOfnode):
		dot.node(str(i),str(i))

	# create edge
	haveConnect = []
	for source,data in enumerate(dataBox):
		if data == '*':
			continue
		else:
			destinations = data.split()
			for destination in destinations:
				print("node",source,"to",destination)
				# if A,B have edge , B,A not connect again
				if str(source)+str(destination) not in haveConnect:
					dot.edge(str(source),str(destination))
					haveConnect.append(str(source)+str(destination))
					haveConnect.append(str(destination)+str(source))
		print()
				
	dot.view()
	# print(dot.source) 


def getText():
	inputData = textField.get(1.0,tk.END)
	draw(inputData)

window = tk.Tk()
window.title('demo two')

# textField = tk.Entry(window)
# textField.pack()
textField = tk.Text(window,height=20)
textField.pack()
button1 = tk.Button(window,text="draw",width=15,height=2,command=getText)
button1.pack()

window.mainloop()