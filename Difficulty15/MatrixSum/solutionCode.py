import csv
from munkres import Munkres


file = 'Difficulty15/MatrixSum/matrix.csv'

origMatrix =[]

with open(file, newline = '\n') as matrixcsv:
    reader = csv.reader(matrixcsv, delimiter=' ')
    for row in reader:
        origMatrix.append(row)


maxInMatrix = 0 

for row in origMatrix: 
    for element in row: 
        if int(element) > maxInMatrix: 
            maxInMatrix = int(element)
matrix = []

for row in origMatrix:
    newRow = []
    for number in row:
        newNumber = maxInMatrix - int(number)
        newRow.append(newNumber)
    matrix.append(newRow)

m = Munkres()

nodes = m.compute(matrix)
vals = []

for x, y in nodes:
    vals.append(int(origMatrix[x][y]))

print(sum(vals))



