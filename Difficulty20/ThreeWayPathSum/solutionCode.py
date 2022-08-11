import csv 
matrixfile = 'Difficulty20/ThreeWayPathSum/matrix.csv'

def matrixPathSum(file):

    matrix = []

    with open(file, newline='\n') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            temp = []
            for i in range(0, len(row)): 
                temp.append(int(row[i]))
            matrix.append(temp)

    value = [matrix[y][-1] for y in range(len(matrix))]


    for i in range(len(matrix)-2, -1, -1):
        value[0] += matrix[0][i]
        for j in range(1,len(matrix)):
            value[j] = min(value[j], value[j-1]) + matrix[j][i]
        for k in range(len(matrix)-2, -1,-1):
            value[k] = min(value[k], value[k+1] + matrix[k][i])
    print(min(value))


matrixPathSum(matrixfile)