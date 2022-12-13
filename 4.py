def prime(x):
    if x == 1 and x%2 == 0:               ## 1 ve 2 için kontrol
        return False
    for i in range(3, int(x**0.5)+1, 2):  ## 3'ten itibaren sayının karekökü + 1 range'i aralığında bu sayıyı bölen bir sayı varsa sayı asal değildir.
        if x%i == 0: 
            return False
    return True                           # bu range'de bu sayıyı bölen bir i değeri yoksa sayı asaldır

counter = 1
i = 1
while (counter != 10001):
    i += 2
    if prime(i):
        counter+=1
print(i)