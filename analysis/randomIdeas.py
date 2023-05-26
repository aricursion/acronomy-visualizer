import json
import networkx as nx
import sys
from tqdm import tqdm
sys.path.append("..") 

# from util.graphLoader import loadGraph
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

def minWordsNeeded(loc, excludeOneDefn = False):
    f = open(loc)
    data = json.load(f)
    graph = nx.DiGraph()
    # opposite graph defns go to source word
    for elt in data:
        defn = ((data[elt])["values"])[0]
        defn = defn.split(" ")
        edges = map(lambda w : (w, elt), defn)
        graph.add_edges_from(edges)

    graph_copy = graph.copy()

    if excludeOneDefn:
        for node in graph:
            if graph.out_degree(node) <= 2:
                graph_copy.remove_node(node)

    newGraph = nx.condensation(graph_copy)


    count = 0
    for node in newGraph:
        if newGraph.in_degree(node) == 0:
            count += 1
    return count

#print(minWordsNeeded("json/cleanGraphNoDeg.json", excludeOneDefn=True))

def numRecursiveAcronyms(loc):
    f = open(loc)
    data = json.load(f)
    graph = nx.DiGraph()
    # opposite graph defns go to source word
    for elt in data:
        defn = ((data[elt])["values"])[0]
        defn = defn.split(" ")
        edges = map(lambda w : (elt, w), defn)
        if elt in defn:
            print(elt)
        graph.add_edges_from(edges)
    
    num_cyc = 0
    short_rec = 0
    uniqueWords = set()
    uniqueWordsNum = 0
    longestCycle = 0
    previousAccs = []
    f = open("recAccUnique10.txt", "w+")

    def compareAcc(accr):
        for acc in previousAccs:
            count = 0
            for word in accr:
                if word in acc:
                    count += 1
            if count > 2:
                return False
        return True
    
    for cyc in nx.simple_cycles(graph, length_bound=10):
        for w in cyc:
            if w not in uniqueWords:
                uniqueWords.add(w)
                uniqueWordsNum += 1
        if compareAcc(cyc):
            previousAccs.append(cyc)
            print('new unique')
            print(len(previousAccs))
            f.write(" ".join(cyc) + "\n\n")
    return (uniqueWordsNum)
        

print(numRecursiveAcronyms("json/cleanGraphNoDeg.json"))

