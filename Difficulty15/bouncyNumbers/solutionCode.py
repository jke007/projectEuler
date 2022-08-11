

bouncy = []

flag = False

number = 1

while not flag:
    increasing = False
    decreasing = False

    num = str(number)
    for i in range(1, len(num)): 
        next = num[i]
        last = num[i-1]
        if int(next) > int(last): 
            increasing = True
        elif int(next) < int(last): 
            decreasing = True 
    if increasing and decreasing:
        bouncy.append(num)
    number+=1
    if float(len(bouncy)/int(num)) == 0.99:
        flag = True

    if number% 10000 ==0 :
        print(float(len(bouncy)/int(num)))
    

print(bouncy[-1])
         
