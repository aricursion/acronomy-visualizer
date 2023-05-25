import json
import networkx as nx

def loadGraph(loc):
    f = open(loc)
    data = json.load(f)
    graph = nx.DiGraph()

    for elt in data:
        defn = ((data[elt])["values"])[0]
        defn = defn.split(" ")
        edges = map(lambda w : (elt, w), defn)
        graph.add_edges_from(edges)
    return graph