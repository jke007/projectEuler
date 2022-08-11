products = []

i = 0
while i < 1000:
    if i % 3 == 0 or i % 5 == 0:
        products.append(i)
    i+=1

print(sum(products))
