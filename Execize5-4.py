from nltk.corpus import wordnet as wn
def  Hypernyms(word):
  return [synset_hypernyms.name().split('.')[0]\
            for synset in wn.s
              for synset_hypernyms in synset.hypernyms()]

print(Hypernyms('girl'))
