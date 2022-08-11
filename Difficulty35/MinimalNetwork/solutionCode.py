from datetime import timedelta
from itertools import chain
import time

starttime = time.time()

edges = []


matrix = 'Difficulty35/MinimalNetwork/matrix.txt'

matrixList = []

originalWeight = 0

f = open(matrix, 'r')
for line in f:
    lineContent = line.strip()
    row = lineContent.split(',')
    matrixList.append(row)

x = 1
for i in range(1, len(matrixList)):
    for j in range(0, x): 
        if matrixList[i][j] == '-': 
            continue
        originalWeight += int(matrixList[i][j])
    x+=1


names = ['THOMAS','JAMES','JACK','DANIEL','MATTHEW','RYAN','JOSHUA','LUKE','SAMUEL','JORDAN','ADAM',
'MICHAEL','ALEXANDER','CHRISTOPHER','BENJAMIN','JOSEPH','LIAM','JAKE','WILLIAM','ANDREW','GEORGE',
'LEWIS','OLIVER','DAVID','ROBERT','JAMIE','NATHAN','CONNOR','JONATHAN','HARRY','CALLUM',
'AARON','ASHLEY','BRADLEY','JACOB','KIERAN','SCOTT','SAM','JOHN','BEN']

class edge:
    def __init__(self, weight, vertex1, vertex2):
        self.weight = weight
        self.vertex1 = vertex1
        self.vertex2 = vertex2

b = 1
for i in range(1, len(matrixList)):
    for j in range(0, b): 
        if matrixList[i][j] == '-': 
            continue
        w = int(matrixList[i][j])
        edges.append(edge(w, names[i] , names[j]))
    b+=1

print("WorksUntilHere")

edges.sort(key=lambda x: x.weight)

edgesInTree = [edges[0]]

verteciesInTree = [['SCOTT' , 'LEWIS']]
totalVertecies = 0
totalEdges = 0
treeBindingEdges = []
for i in range(1, len(edges)):
    #if(len(verteciesInTree)) == 40 and len(edgesInTree) == 39: 
    if totalVertecies <=39:
        count =  0
        y = list(chain(*verteciesInTree))
        if edges[i].vertex1 in y and edges[i].vertex2 in y:
            continue
        for j in range(len(verteciesInTree)):
            count +=1
            if ((edges[i].vertex1 in verteciesInTree[j]) ^ (edges[i].vertex2 in verteciesInTree[j])):
                edgesInTree.append(edges[i])
                if edges[i].vertex1 in verteciesInTree[j]:
                    verteciesInTree[j].append(edges[i].vertex2)
                    totalVertecies = sum(len(e) for e in verteciesInTree)
                    break
                else:
                    verteciesInTree[j].append(edges[i].vertex1)
                    totalVertecies = sum(len(e) for e in verteciesInTree)
                    break
            else:
                if ((edges[i].vertex1 not in verteciesInTree[j]) and (edges[i].vertex2 not in verteciesInTree[j])) and count == len(verteciesInTree):
                    edgesInTree.append(edges[i])
                    verteciesInTree.append([edges[i].vertex1, edges[i].vertex2])        
                    totalVertecies = sum(len(e) for e in verteciesInTree)
                    break
        totalEdges = len(edgesInTree)
    if totalVertecies == 40:
        break

for i in range(0,len(edges)):    
    if totalEdges == 39:
        break
    if totalEdges < 39:
        flag = False
        for lk in range(0, len(verteciesInTree)):
            if edges[i].vertex1 in verteciesInTree[lk] and edges[i].vertex2 in verteciesInTree[lk]:
                flag = True
                break
        if flag:
            continue
        v1 = []
        v2 = []
        for v in range(0,len(verteciesInTree)): 
            if edges[i].vertex1 in verteciesInTree[v]:
                v1 = verteciesInTree[v]
                verteciesInTree[v] = []
                break
        for u in range(0, len(verteciesInTree)):
            if edges[i].vertex2 in verteciesInTree[u]:
                v2 = verteciesInTree[u]
                verteciesInTree[u] = []
                break
        newTree = v1 + v2
        verteciesInTree.append(newTree)
        treeBindingEdges.append(edges[i])
        
newWeight = 0 
for w in range(0, len(edgesInTree)):
    newWeight += edgesInTree[w].weight

for r in range(0, len(treeBindingEdges)):
    newWeight += treeBindingEdges[r].weight

endtime = time.time()

print(originalWeight - newWeight)
print(originalWeight)
print(newWeight)

