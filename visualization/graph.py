import networkx as nx
import matplotlib.pyplot as plt
import json
import sys
import os
sys.path.append(os.path.abspath('util'))
from graphLoader import loadGraph


def makeGraph(loc):
    graph = loadGraph(loc)
    sizes = []
    for w in graph.nodes:
        sizes.append(50*graph.in_degree(w) + 10)
    #print(sizes)
    fig = plt.figure(1, figsize=(12, 12))
    
    font_colors = []
    for w in graph.nodes:
        if graph.in_degree(w) + graph.out_degree(w) > 5:
            font_colors.append("white")
        else:
            font_colors.append("black")
    nx.draw(graph, with_labels=True, node_size=sizes, font_size=24, font_colors=font_colors)
    fig.savefig('img/small_graph.png')

    # fig.show()
makeGraph("json/cleanGraphDeg.json")

def makeRecursiveAcronymGraph(loc):
    graph = loadGraph(loc)
    sizes = []
    for w in graph.nodes:
        sizes.append(50*graph.in_degree(w) + 10)
    print(sizes)
    print(len(sizes))
    fig = plt.figure(1, figsize=(10, 10))

    nx.draw(graph, with_labels=True, node_size=sizes, font_size=12, font_color="black")
    fig.savefig('img/recursive_acr_graph.png')

# makeRecursiveAcronymGraph("json/cleanGraphDeg.json")

