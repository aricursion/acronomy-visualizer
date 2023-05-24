import parseSite as pS
import json
def getFullGraph():
    pass

def getGraphFromWord(word):
    stack = [word]
    graph = {}
    while stack != []:
        cur = stack.pop()
        defn = pS.getDefOfWord(cur)
        if cur not in graph:
            graph[cur] = defn
        newWords = list(filter(lambda w : w not in graph, defn))
        stack = stack + newWords
        print("stack size:", len(stack))
        graph_size = len(graph)
        print("size of graph:", graph_size)
        if (len(graph) % 100 == 0):
            with open("util/start_graphs/start_graph"+str(graph_size)+".json", 'w') as outfile:
                json.dump(graph, outfile)

    return graph

graph = getGraphFromWord("start")
with open("start_graph.json", "w+") as outfile:
    json.dump(graph, outfile)
