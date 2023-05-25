import matplotlib.pyplot as plt
import json 

def genHist(loc):
    f = open(loc)
    data = json.load(f)
    values = []
    for elt in data:
        values.append((data[elt])["inDeg"])
    plt.hist(values, bins=5)
    # plt.xscale("log")
    plt.show()
    print(sum(values)/len(values))

genHist("json/cleanGraphDeg.json")
