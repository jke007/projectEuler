import math


num = int(600851475143)
primes = []
primefactors =[]
prod = 1
while prod < num/2:
    for i in range(3, int(num/2)):
        flag = False
        for a in range(2, i):
            if(i%a == 0):
                flag = True
                break
        if not flag:
            primes.append(i)
            if num % i == 0:
                primefactors.append(i)
        if math.prod(primefactors) == num:
            break
    break

print(max(primefactors))












            