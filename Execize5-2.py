def reversed(lst):
 ans=[]
 for word in range(0,len(lst)):
   ans.append(lst.pop())
 return ans

words=['hallo','konnichiwa','hello','hola']
print(reversed(words))

