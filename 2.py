
#initial variables
a, b = 1, 1
toplam = 0

#when a is smaller than 4 million, if a is even; add it to total
while a <= 4000000:
    if a % 2 == 0:
        toplam += a
    a, b = b, a+b  #Fibonacci

print(toplam)