def hesap(x):
	toplam = sum(i for i in range(x) if (i % 3 == 0 or i % 5 == 0))
	return toplam
print(f'1 ile 1000 arası 3e veya 5e bolunebilen sayilarin toplami: {hesap(1000)}')