def GetLongSynonyms(word):
  from nltk.corpus import wordnet as wn
  synonyms = wn.synsets(word)
  ans=[]
  for synonym in synonyms:
    if not synonym.name().split('.')[0].find('_') == -1:
       ans.append(synonym.name().split('.')[0])
  return ans


print(GetLongSynonyms('play'))
