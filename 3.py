#to check if a number is palindrome by using str(n)
def isPalindrome(n):
    return str(n) == str(n)[::-1]

palindromeList=[]

#append the number on the empty list if
for i in range(100,1000):
    for j in range(100,1000):
        result = i*j
        if isPalindrome(result):
            palindromeList.append(result)

#find the max num in the list as a result of multiplying 2 3-digit numbers
print(max(palindromeList))