from nltk.corpus import wordnet as wn
synonyms = wn.synsets('play')
for synonym in synonyms:
  definition=synonym.definition()
  if len(definition)<15:    
    print(definition.upper())
  else:
    print(definition.title())

