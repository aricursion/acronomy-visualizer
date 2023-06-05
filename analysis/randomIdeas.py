import json
import networkx as nx
import sys
import os

sys.path.append(os.path.abspath('util'))
from graphLoader import loadGraph

def sCC(loc):
    graph = loadGraph(loc)
    
    for cc in nx.connected_components(graph.to_undirected()):
        if len(cc) < 100:
            print(cc)
    return nx.number_strongly_connected_components(graph)

print(sCC("json/cleanGraphNoDeg.json"))

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

def numGenRecursiveAcronyms(loc):
    graph = loadGraph(loc)
    f = open(loc)
    data = json.load(f)
    uniqueWords = set()
    uniqueWordsNum = 0
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
    
    def extrapolate(cyc):
        defn = [cyc[0]]
        print(cyc[0])
        # print(cyc)
        def concatenate_lists(list1, list2, element):
            indices = []
            for idx, elt in enumerate(list1):
                if elt == element:
                    indices.append(idx)
            if indices != []:
                for idx in indices:
                    list1 = list1[:idx] + list2 + list1[idx+1:]
                return list1
            else:
                return list1

        for word in cyc:
                defn = concatenate_lists(defn, (((data[word])["values"])[0]).split(" "), word)

        defn = concatenate_lists(defn, ["[...]"], cyc[0])

        return " ".join(defn)

        
    for cyc in nx.simple_cycles(graph, length_bound=10):
        for w in cyc:
            if w not in uniqueWords:
                uniqueWords.add(w)
                uniqueWordsNum += 1
        if compareAcc(cyc):
            previousAccs.append(cyc)
            # print('new unique')
            # print(len(previousAccs))  
            extrap = extrapolate(cyc)
            f.write('"' + " ".join(cyc) + '" stands for:' + "\n")
            f.write(extrap + "\n\n")

        
    return (uniqueWordsNum)
        

print(numGenRecursiveAcronyms("json/cleanGraphNoDeg.json"))

