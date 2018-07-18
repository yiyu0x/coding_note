import tkinter as tk
import graphviz
import yiyu_kruskal
from bubble import bubbleSort
from tkinter import messagebox

sortedOutput = ''
def print_graph(graph,dot,MST):
	for i in graph['vertices']:
		dot.node(str(i),str(i))
	for i in graph['edges']:
		if i in MST['edges'] or (i[0],i[2],i[1]) in MST['edges']:
			dot.edge(str(i[1]),str(i[2]),str(i[0]),color="red")
		else:
			dot.edge(str(i[1]),str(i[2]),str(i[0]))
	dot.view()

def draw(inputData1,inputData2,inputData3,inputData4):
	##initialize#####################################################################
	dot = graphviz.Graph(comment='three')
	dot_MST = graphviz.Graph(comment='three')
	###input data###################################################################
	inputVetices = inputData2
	dataBox = inputData4.split(',')
	################################################################################
	###create graph#################################################################
	graph = {}
	boxList = []
	graph['vertices'] = list(inputVetices)
	# collect edges and weight
	boxTuple = ()
	for detail in dataBox:
		tmp = detail.split()
		boxTuple = (int(tmp[1]),tmp[0][0],tmp[0][1])
		boxList.append(boxTuple)
	graph['edges'] = set(boxList)

	###creaate graph_MST############################################################
	graph_MST = graph.copy()
	tmp_graph = graph.copy()
	# create reverse box for graph_MST to calulate MST
	reverseBox = []
	for i in graph_MST['edges']:
		reverseBox.append(i)
		reverseBox.append((i[0],i[2],i[1]))
	reverseBox = set(reverseBox)
	tmp_graph['edges'] = reverseBox
	graph_MST['edges'] = yiyu_kruskal.kruskal(tmp_graph)
	for i in graph_MST['edges']:
		if (i[0],i[2],i[1]) in graph_MST['edges']:
			graph_MST['edges'].remove(i)
	###debug##############################################
	print("graph",graph['edges'])
	print("graphMST",graph_MST['edges'])
	print("\n\n")
	######################################################
	#sorting string
	global sortedOutput

	# sortedNode = sorted(graph_MST['edges'])
	sortedNode = bubbleSort(graph_MST)
	
	sortedOutput = ''
	for i in sortedNode:
		sortedOutput += str(i[1])+str(i[2])+'->'
	sortedOutput = sortedOutput[:-2]
	sortedOutput += ' '
	print(sortedOutput)
	######################################################
	print_graph(graph,dot,graph_MST)
	# dot.view()
	# dot_MST.view()
	######################################################

def getText():
	global sortedOutput
	inputData1 = textField1.get()
	inputData2 = textField2.get()
	inputData3 = textField3.get()
	inputData4 = textField4.get()
	draw(inputData1,inputData2,inputData3,inputData4)
	messagebox.showinfo("showinfo",sortedOutput)
	sortedOutput = ''
window = tk.Tk()
window.title('demo four')

textField1 = tk.Entry(window)
textField1.pack()
textField2 = tk.Entry(window)
textField2.pack()
textField3 = tk.Entry(window)
textField3.pack()
textField4 = tk.Entry(window)
textField4.pack()
button1 = tk.Button(window,text="draw",width=15,height=2,command=getText)
button1.pack()
# t = tk.Text(window,height=2)
# t.pack()
window.mainloop()













"""
graph = {
'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
'edges': set([
(7, 'A', 'B'),
(5, 'A', 'D'),
(7, 'B', 'A'),
(8, 'B', 'C'),
(9, 'B', 'D'),
(7, 'B', 'E'),
(8, 'C', 'B'),
(5, 'C', 'E'),
(5, 'D', 'A'),
(9, 'D', 'B'),
(7, 'D', 'E'),
(6, 'D', 'F'),
(7, 'E', 'B'),
(5, 'E', 'C'),
(15, 'E', 'D'),
(8, 'E', 'F'),
(9, 'E', 'G'),
(6, 'F', 'D'),
(8, 'F', 'E'),
(11, 'F', 'G'),
(9, 'G', 'E'),
(11, 'G', 'F'),
])
}

"""