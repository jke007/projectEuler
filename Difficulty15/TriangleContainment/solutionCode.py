
triangles = "Difficulty15/TriangleContainment/triangles.txt"

temp= []

f = open(triangles, 'r')
for line in f:
    lineContent = line.strip()
    row = lineContent.split(',')
    for i in range(0, len(row)):
        row[i] = int(row[i])
    temp.append(row)

triList = []

for i in range(0,len(temp)):
    triangle = [[temp[i][0], temp[i][1]],[temp[i][2], temp[i][3]],[temp[i][4], temp[i][5]]]
    triList.append(triangle)
    
counter = 0

def area(a,b,c):
    areal = abs((a[0] - c[0])*(b[1] -a[1]) - (a[0]-b[0])*(c[1]-a[1]))
    return areal

for triangle in triList:
    o = [0,0]
    a = triangle[0]
    b = triangle[1]
    c = triangle[2]
    bigTriangle = area(a,b,c)
    tri_1 = area(o,b,c)
    tri_2 = area(a,o,c)
    tri_3 = area(a,b,o)

    if bigTriangle == tri_1 + tri_2 + tri_3:
        counter += 1
    
print(counter)
        
