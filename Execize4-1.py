

def GetSynonyms(word):
  from nltk.corpus import wordnet as wn
  synonyms = wn.synsets(word)
  ans=[]
  for synonym in synonyms:
    ans.append(synonym.name().split('.')[0])
  return ans

print(GetSynonyms('play'))
