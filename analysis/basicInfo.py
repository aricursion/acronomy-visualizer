import sys 
import os
sys.path.append(os.path.abspath('util'))
from graphLoader import loadGraph

def basicInfo(loc):
    graph = loadGraph(loc)
    out = {}
    out["total edges"] = graph.number_of_edges()
    out["total vertices"] =  graph.number_of_nodes()
    out["average degree"] = 2 * graph.number_of_edges() / graph.number_of_nodes()
    return out
print(basicInfo("json/cleanGraphNoDeg.json"))