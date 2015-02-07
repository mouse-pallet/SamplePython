from collections import defaultdict

words=['hello','hi','hello','hi','hello']
dictionary= defaultdict(int)
for word in words:
  dictionary[word]+=1
print(dictionary)
