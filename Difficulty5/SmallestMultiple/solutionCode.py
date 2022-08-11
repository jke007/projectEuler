import math
num = 1
for i in range(1,21):
    num *= i // math.gcd(i, num)
print(num)

