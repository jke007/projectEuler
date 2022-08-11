largestPalindrome = 1

for i in range(999, 100, -1):
    for j in range(999,100, -1):
        prod = i*j 
        num = str(prod)
        palindrome = True
        for a in range(0, len(num)-1):
            if num[a] != num[-a-1]:
                palindrome = False

        if palindrome:
            if prod> int(largestPalindrome):
                largestPalindrome = num
            break


print(largestPalindrome)
