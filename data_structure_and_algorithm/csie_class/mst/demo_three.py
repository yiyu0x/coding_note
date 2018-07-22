import tkinter as tk
import graphviz
from tkinter import messagebox
import yiyu_prim

sortedOutput = ''

def print_graph(nodes,edges,MST):
	dot = graphviz.Graph(comment='three')
	# dot_MST = graphviz.Graph(comment='three')
	for i in nodes:
		dot.node(str(i),str(i))

	for i in edges:
		# print(i[0],i[1],i[2])
		if i in MST or (i[1],i[0],i[2]) in MST:
			dot.edge(i[0],i[1],str(i[2]),color='red')
		else:
			dot.edge(i[0],i[1],str(i[2]))
		# dot.edge('A','B','3')
	dot.view()

def draw(inputData1,inputData2,inputData3):
	# print(inputData1,inputData2,inputData3)
	nodes = list(inputData1)
	###debug
	# nodes = ['A','B','C','D','E','F','G']
	# inputData2 = 'AB 7,BC 8,CE 5,BE 7,BD 9,AD 5,DE 15,EG 9,EF 8,FG 11,DF 6'
	###
	dataBox = inputData2.split(',')
	edges = []
	for data in dataBox:
		part = data.split()
		edges.append((part[0][0],part[0][1],int(part[1])))

	MST = yiyu_prim.prim(nodes,edges)
	sortEdges = sorted(edges, key = lambda x : x[2])

	###sorting node string
	global sortedOutput
	sortedOutput = str(MST[0][1]) + '->' + str(MST[0][0])
	# print(sortedOutput)
	for i in range(1,len(MST)):
		sortedOutput += '->' + str(MST[i][1])
	print(sortedOutput)
	###

	
	#debug
	# print(sortEdges)
	# print("mst:",MST)
	# print()
	# print("edges:",edges)

	print_graph(nodes,edges,MST)

def getText():
	global sortedOutput
	inputData1 = textField1.get()
	inputData2 = textField2.get()
	inputData3 = textField3.get()
	# inputData4 = textField4.get()
	draw(inputData1,inputData2,inputData3)
	messagebox.showinfo("showinfo",sortedOutput)
	sortedOutput = ''

window = tk.Tk()
window.title('demo three')

textField1 = tk.Entry(window)
textField1.pack()
textField2 = tk.Entry(window)
textField2.pack()
textField3 = tk.Entry(window)
textField3.pack()
# textField4 = tk.Entry(window)
# textField4.pack()
button1 = tk.Button(window,text="draw",width=15,height=2,command=getText)
button1.pack()
# t = tk.Text(window,height=2)
# t.pack()
window.mainloop()