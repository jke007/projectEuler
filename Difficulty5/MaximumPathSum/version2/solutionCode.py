triangle = "Difficulty5/MaximumPathSum/version2/triangle.txt"

with open(triangle) as f:
    lines = f.read()
lines = lines.strip().split('\n')
for i in range(0,len(lines)):
    lines[i] = lines[i].strip().split(' ')
    lines[i] = [int(x) for x in lines[i]]

for i in range(len(lines), 1, -1):
    for j in range(0, len(lines[i-1]) - 1):
        lines[i-2][j] += max(lines[i-1][j], lines[i-1][j+1])

print(lines[0][0])