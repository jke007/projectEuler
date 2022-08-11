evenFibonacci = []

a = 0
b = 1

while b < 4000000:
    tempa = b
    b = a+b
    a = tempa
    if b % 2 == 0:
        evenFibonacci.append(b)
    
print(sum(evenFibonacci))