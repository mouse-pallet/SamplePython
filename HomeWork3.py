from nltk.corpus import wordnet as wn
synonyms=wn.synsets('play')
for synonym in synonyms:
  definiton=synonyms[6].name().split()
  print(definiton[0])
