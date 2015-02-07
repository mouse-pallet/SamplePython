def PrintWordsFrequency(words):
  dic={}
  for word in words:
   if word in dic:
      dic[word]=dic[word]+1
   else:
      dic[word]=1
  for word in dic:
    print word,dic[word]  
  


words=['hi','hello','hi','hallo','hello','hi']
PrintWordsFrequency(words)
