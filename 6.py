sentence = input("Sentence: ")

#this will allow us to not accept any punctuations
filtered = ''.join(filter(lambda x: x not in '".,;!-', sentence))


words = [word for word in filtered.split() if word]

#average length of words:
avg_len = sum(map(len, words))/len(words)
print(avg_len)