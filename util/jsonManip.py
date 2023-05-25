import json


def cleanData(loc):
    f = open(loc)
    data = json.load(f)
    newJson = {}
    for elt in data:
        actual_name = ((elt["name"].split(":"))[0]).strip()
        if actual_name not in newJson:
            newEltDict = {}
            newEltDict["values"] = [elt["value"]]
            newJson[actual_name] = newEltDict
        else:

            ((newJson[actual_name])["values"]).append(elt["value"])

    return newJson

with open("foo.json", "w+") as outfile:
    json.dump(cleanData("json/originalGraph.json"), outfile)

# This takes in a cleaned graph, and
# adds information about the in-degrees
# of each vertex
def inDegrees(loc, defnPriority=0):
    if defnPriority != 0:
        raise "I don't know what to do here"
    
    if defnPriority == 0:
        f = open(loc)
        data = json.load(f)
        inDegs = {}
        for elt in data:
            defn = ((data[elt])["values"])[0]
            for word in defn.split(" "):
                if word not in inDegs:
                    inDegs[word] = 1
                else:
                    inDegs[word] += 1

        for entry in data:
            if entry in inDegs:
                (data[entry])["inDeg"] = inDegs[entry]
            else:
                (data[entry])["inDeg"] = 0
        return data

with open("foo2.json", "w") as outfile:
    json.dump(inDegrees("foo.json"), outfile)