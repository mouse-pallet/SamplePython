import codecs

def CreatDic(filename):
  finput=codecs.open(filename,'r','utf-8')
  dict={}
  for line in finput:
    word= line.split()
    dict[word[0]]=word[1]
  #print dict
  return dict

def Translate(en_file,dic_file,spa_file):

  dic_dic=CreatDic(dic_file)
  finput=codecs.open(en_file,'r','utf-8')
  #content_str = finput.read()
  #en_list=content_str.split("\n")
  sp_list=[]
  for line in finput:
    for word in line.split():
      sp_list.append(dic_dic[word])
    text=' '.join(sp_list)+"\n"

  print text
  foutput=codecs.open(spa_file,'w','utf-8')
  foutput.write(text)

  

english_filename='english_text.txt'
dictionary_filename='dictionary_en-es.txt'
spanish_filename='spanish_text.txt'
Translate(english_filename,dictionary_filename,spanish_filename)
      
  


