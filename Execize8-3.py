import codecs
def PopularWord(name):
  finput = codecs.open(name,'r','utf-8')
  lines = finput.readlines()
  wordic={}
  bestword=''
  bestcount=-1
  for line in lines:
    for word in line.split():
      if word not in wordic:
        wordic[word]=1
      else:
        wordic[word]=wordic[word]+1
  finput.close()   

  list=wordic.items()
  for wordtuple in list:
    if bestcount<wordtuple[1]:
      bestcount=wordtuple[1]
      bestword=wordtuple[0]
  print bestword,bestcount

def PopularChar(name):
  finput = codecs.open(name,'r','utf-8')
  content_str=finput.read()
  finput.close()
  chardic={}
  bestchar=''
  bcount=-1
  for chara in list(content_str):
      if chara not in chardic:
        chardic[chara]=1
      else:
        chardic[chara]=chardic[chara]+1
  
  del chardic[" "]
  del chardic["'"]
  del chardic[","]  

  clist=chardic.items()
  for chartuple in clist:
    if bcount<chartuple[1]:
      bcount=chartuple[1]
      bestchar=chartuple[0]
  print bestchar,bcount

filename='little_prince.txt'
print "word:"
PopularWord(filename)
print "chara:"
PopularChar(filename)
