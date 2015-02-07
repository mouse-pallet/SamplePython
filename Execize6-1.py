def  RemoveDuplicates(list):
  newlist=[]
  for word in list:
     if word not in newlist:
        newlist.append(word)
  return newlist


words=['hi','hi','how','are','how','you?']
print(RemoveDuplicates(words)) 
