import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import BOTH, END, LEFT
from PIL import Image, ImageTk
import numpy as np
from random import choice
#----------------------------main window-----------------------------------#
gui = tk.Tk(className="Tittle")
gui.geometry("1280x700")
WIDTH, HEIGHT = 450, 350
G=nx.Graph()
#-----------------------------Functions for calculations-----------------------#
#Function for node in complete graphs
def total_de_aristas_grafos_completos(n):
	result = (n * (n - 1)) // 2
	return result
#Function Remove duplicates for count exactly edges and nodes
def remueve_duplicados(list_n):
    element_seen = set()
    for item in list_n:
        tup = tuple(item)
        if tup not in element_seen:
            element_seen.add(tup[::-1])
            yield item
#Function return edges
def recorre_list_n(list_n):
	element_g = ''
	for e in list_n:
		element_g = element_g + 'The node {} has grade: {} \n'.format(e[0], e[1])
	return element_g
#Function sumatory edges
def devuelve_grados(list_n):
	return sum([ele[1] for ele in list_n])
#----------------------------Function Event & Calculations-----------------------------#
def event():
  list_n_de_nodes = str(entry.get())
  try:
  	#--------------Evaluate string of graph-----------#
  	res = list(eval(list_n_de_nodes))
  	G.add_edges_from(res)
  	label_graph.configure(text = "Your graph is: " + entry.get())
  	#--------------Show images of graph-------------------------------------#
  	nx.draw(G,with_labels = True, edge_color='green', node_color='yellow')
  	grafo_imagen = plt.savefig("graph_c.png")
  	load = Image.open("graph_c.png").resize((WIDTH, HEIGHT))
  	render = ImageTk.PhotoImage(load)
  	img = tk.Label(gui, width = 450, height = 350, anchor="w")
  	img.config(image=render)
  	img.image = render
  	plt.clf()
  	title_sub = tk.Label(gui, text="GRAPH:", anchor="w")
  	title_sub.grid(row=7, column=0)
  	img.grid(row=8, column=0)
  	#--------------show subgraph images-----------------------------------#
  	random_node = choice(np.unique(res))
  	list_n_node_sub = [ n[1] for n in G.edges(random_node) ]
  	list_n_node_sub.append(random_node)
  	Gsub = nx.Graph(G.subgraph(list_n_node_sub))
  	nx.draw(Gsub,with_labels = True, edge_color='red', node_color='pink')
  	grafo_imagen_sub = plt.savefig("subgraph_c.png")
  	load_sub = Image.open("subgraph_c.png").resize((WIDTH, HEIGHT))
  	render_sub = ImageTk.PhotoImage(load_sub)
  	img2 = tk.Label(gui, width = 450, height = 350, anchor="w")
  	img2.config(image=render_sub)
  	img2.image = render_sub
  	plt.clf()
  	title_sub = tk.Label(gui, text="RANDOM SUBGRAPH", anchor="w")
  	title_sub.grid(row=7, column=1)
  	img2.grid(row=8, column=1)
  	#--------------Get Edges-----------------------------------#
  	vertex_to = np.unique(res)
  	label_vertex.configure(text = "Edge of the Graph: " + str(vertex_to))
  	#-------------Get Nodes-------------------------------------#
  	aristas = list(remueve_duplicados(res))
  	label_nodes_a.configure(text = "Nodes of the graph: " + str(len(aristas)))
  	#-------------Grades------------------------------------#
  	list_n_grados = G.degree()
  	label_grade_titl.configure(text = "GRADES OF EDGES: \n" + str(recorre_list_n(list_n_grados)) + "\n GRADE UNDER FORMULA Σgr(v) = 2 |A| IS: " + str(devuelve_grados(list_n_grados)) + "(2) = "+ str(devuelve_grados(list_n_grados)*2))
  except NameError:
  	label_graph.configure(text = "Error: Must be a format like ('x','y'),('w','z') ")
  return
  entry.delete(0,END)
#----------------------------Elements of GUI-----------------------------#
tk.Label(gui, anchor="e", text="INSTRUCTIONS: WRITE A GRAPH IN FORMAT ('x','y'),('z','w') \n. YOU CAN PUT NEW GRAPHS AND CHOOSE [SHOW CHARACTERISTICS] \n EVERY TIME YOU WANT.").grid(row=0, column=0)
#input
entry = tk.Entry(gui, width=90)
entry.bind("<Return>", event)
entry.grid(row=0, column=1)
#labels
label_graph = tk.Label(gui, anchor="w")
label_graph.grid(row=1, column=0)
label_vertex = tk.Label(gui, anchor="w")
label_vertex.grid(row=2, column=0)
label_nodes_a = tk.Label(gui, anchor="w")
label_nodes_a.grid(row=3, column=0)
label_grade_titl = tk.Label(gui, anchor="w")
label_grade_titl.grid(row=4, column=0)
#----------------Button of event-------------------------------------------#
B = tk.Button(gui, text ="Show characteristics of my Graph", command = event)
B.grid(row=9, column=0)
gui.mainloop()