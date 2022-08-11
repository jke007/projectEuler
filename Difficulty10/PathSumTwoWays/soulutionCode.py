

matrix =[]

f =  open('Difficulty10/PathSumTwoWays/matrix.txt', 'r')
for line in f:
    lineContent  = line.strip()
    row = lineContent.split(',')
    for i in range(0, len(row)):
        row[i] = int(row[i])
    matrix.append(row)


length = len(matrix) -1

for i in range(length, -1, -1):
    for j in range(length, -1, -1):
        if i < length and j < length:
            matrix[i][j] += min(matrix[i+1][j] , matrix[i][j+1])
        elif i < length: 
            matrix[i][j] += matrix[i+1][j]
        elif j < length:
            matrix[i][j] += matrix[i][j+1]

print(matrix[0][0])
