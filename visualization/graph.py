import networkx as nx
import matplotlib.pyplot as plt
import json

def makeGraph(loc):
    f = open(loc)
    data = json.load(f)
    graph = nx.DiGraph()

    for elt in data:
        defn = ((data[elt])["values"])[0]
        defn = defn.split(" ")
        edges = map(lambda w : (elt, w), defn)
        graph.add_edges_from(edges)
    
    sizes = []
    for w in graph.nodes:
        sizes.append(50*graph.in_degree(w) + 10)
    print(sizes)
    fig = plt.figure(1, figsize=(500, 500), dpi=60)

    nx.draw_spectral(graph, with_labels=True, node_size=sizes, font_size=24, font_color="white")
    fig.savefig('img/spectral_graph.png')

    # fig.show()
makeGraph("json/cleanGraphDeg.json")

def makeRecursiveAcronymGraph(loc):
    f = open(loc)
    data = json.load(f)
    graph = nx.DiGraph()

    for elt in data:
        defn = ((data[elt])["values"])[0]
        defn = defn.split(" ")
        edges = map(lambda w : (elt, w), defn)
        if elt in defn:
            graph.add_edges_from(edges)
    
    sizes = []
    for w in graph.nodes:
        sizes.append(50*graph.in_degree(w) + 10)
    print(sizes)
    print(len(sizes))
    fig = plt.figure(1, figsize=(10, 10))

    nx.draw(graph, with_labels=True, node_size=sizes, font_size=12, font_color="black")
    fig.savefig('img/recursive_acr_graph.png')

# makeRecursiveAcronymGraph("json/cleanGraphDeg.json")

