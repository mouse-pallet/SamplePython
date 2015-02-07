answer = []
# synonyms = [Synset('play'),Synset('bid'),Synset('free_rain'),...]
from nltk.corpus import wordnet as wn
def GetLongSynonyms(word_string):
synonyms = wn.synsets(word_string)
answers = []
for synonym in synonyms:
 synonym_clean = synonym.name().split(’.’)[0]
if ’_’ in synonym_clean:
answers.append(synonym_clean)
return answers

