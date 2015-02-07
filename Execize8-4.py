import codecs
def CountCharsWordsLines(name):
  finput = codecs.open(name,'r','utf-8')
  lines = finput.readlines()
  cline=0
  wordset=[]
  charset=[]
  for line in lines:
    cline+=1
    for word in line.split():
      wordset.append(word)
      for chara in list(word):
        charset.append(chara)
  print cline
  print len(wordset)
  print len(charset)
#   print "(%d,%d,%d)" %(len(charset),len(wordset),cline)

filename='little_prince.txt'
CountCharsWordsLines(filename)
