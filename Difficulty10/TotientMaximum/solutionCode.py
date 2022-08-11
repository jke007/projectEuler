
##########################
#First approach (very naive):
##########################
#import math
#maxphi = 1
#for i in range(1000000, 0, -1):
#    relativePrimes = []
#    for j in range(int(i/2), 0,-1):
#        if math.gcd(i,j) == 1:
#            relativePrimes.append(j)
#    phi = i/len(relativePrimes)
#    if phi > maxphi: 
#        maxphi = phi
#        print(phi , i)
#    if len(relativePrimes) == 1:
#        print(i)
#        break
#
######################################################
#Second approach after reading about totient-function:
######################################################

#Let p be the product of the maximum n primes for which p doesnt exceed 1000000:

primes = [2,3,5,7,11,13,17,19,23,29,31]

val = 1
i = 0
while val <= 1000000: 
    val *= primes[i]
    i+=1
    print(val)