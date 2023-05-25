import json
import networkx as nx
import sys
# sys.path.append("..") 

#from util.graphLoader import loadGraph
def sCC(loc):
    f = open(loc)
    data = json.load(f)
    graph = nx.DiGraph()

    for elt in data:
        defn = ((data[elt])["values"])[0]
        defn = defn.split(" ")
        edges = map(lambda w : (elt, w), defn)
        graph.add_edges_from(edges)

    return nx.number_strongly_connected_components(graph)

def minWordsNeeded(loc):
    f = open(loc)
    data = json.load(f)
    graph = nx.DiGraph()

    for elt in data:
        defn = ((data[elt])["values"])[0]
        defn = defn.split(" ")
        edges = map(lambda w : (elt, w), defn)
        graph.add_edges_from(edges)

    sccs = nx.strongly_connected_components(graph)

    newGraph = nx.DiGraph()
    numSCC = 0
    for rep in sccs:
        numSCC += 1
        print(rep)
        rep = (list(rep))[0]
        if rep not in data:
            newGraph.add_node(rep)
        else:
            defn = ((data[rep])["values"])[0]
            defn = defn.split(" ")
            defn = list(filter(lambda w : {w} in sccs, defn))
            edges = map(lambda w : (rep, w), defn)
            newGraph.add_edges_from(edges)
    count = 0
    for node in newGraph:
        if newGraph.in_degree(node) == 0:
            count += 1
    print("numScc: ", nx.number_strongly_connected_components(graph))
    return count


print(minWordsNeeded("json/cleanGraphNoDeg.json"))

