from nltk.corpus import wordnet as wn
synonyms = wn.synsets('play')
for synonym in synonyms:
  print(synonym.name().split('.')[0])

