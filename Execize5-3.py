from nltk.corpus import wordnet as wn
 
# NLP exercise 1: Write a function that returns the hypernyms of a word.
 
def GetHypernyms(word):
  synsets = wn.synsets(word)
  hypernyms = []
  for synset in synsets:
    synset_hypernyms = synset.hypernyms()
    for synset_hypernym in synset_hypernyms:
      hypernym_lemma  = synset_hypernym.name().split('.')[0]
      hypernyms.append(hypernym_lemma)
  return hypernyms
 
hypernyms = GetHypernyms('girl')
print(hypernyms)

