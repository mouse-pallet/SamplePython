import codecs 
finput = codecs.open('little_prince.txt','r','utf-8')
content_str=finput.read()
a=set(content_str.split())
print(a)
finput.close() 
