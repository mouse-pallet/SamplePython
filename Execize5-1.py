def FindWordPosition(lst,wrd):
 count=0
 for word in lst:
   if word == wrd:
     return count
   count += 1
 return 'None'
 
words=['hallo','konnichiwa','hello','hola']
print(FindWordPosition(words,'holaaa'))
print(FindWordPosition(words,'hola'))
