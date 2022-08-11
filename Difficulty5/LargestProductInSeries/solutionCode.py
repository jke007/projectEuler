import math
file = 'Difficulty5/LargestProductInSeries/number.txt'

f = open(file, 'r')

digits = ''.join(str(f.read()).split())

maxProduct = 0

#first 13 digits to initiate process
nums = [7,3,1,6,7,1,7,6,5,3,1,3,3]

for i in range(13, 1000):
    if math.prod(nums) > maxProduct:
        maxProduct = math.prod(nums)
    
    nums.pop(0)
    nums.append(int(digits[i]))

print(maxProduct)
    

