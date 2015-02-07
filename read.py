import codecs

print('#### Method 1 ####')
finput = codecs.open('sample.txt', 'r', 'utf-8')
for line in finput:
  print(line)
finput.close()

print('#### Method 2 ####')
finput = codecs.open('sample.txt', 'r', 'utf-8')
lines = finput.readlines()
for line in lines:
  print(line)
finput.close()

print('#### Method 3 ####')
finput = codecs.open('sample.txt', 'r', 'utf-8')
data = finput.read()
print(data)
finput.close()

