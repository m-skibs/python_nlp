import nltk
import spacy
import random

from nltk.corpus import wordnet as wn

sp = spacy.load('en_core_web_sm')
text = sp("place your input text here")

text_clean = []
for word in text:
    if word.is_stop == False:
        text_clean.append(word)

allsyns = []
defs = []
for word in text_clean:
    for ss in wn.synsets(str(word)):
        for l in ss.lemma_names():
            allsyns.append(l)
        defs.append(ss.definition()) #can likely do this only for the first few words

allsyns_cap = []
#capitalize to prep for input word removal
for word in allsyns:
    allsyns_cap.append(str(word).upper())

#remove words from input
for word in text_clean:
    wordstr = str(word).upper()
    if wordstr in allsyns_cap:
        while wordstr in allsyns_cap:
            allsyns_cap.remove(wordstr)

syns = []
#create a list with no duplicates
for word in set(allsyns_cap):
    syns.append(str(word))

#get our final ten
ten_words = []
if len(syns) == 10 or len(syns) == 10:
    #easiest scenario
    ten_words = syns

elif len(syns) > 10:
    #select 10 random syns to avoid only showing syns of first word(s)
    ten_words = random.sample(syns, 10)

elif 1 <= len(syns) < 10:
    def_words = []
    for defn in defs:
        #first tokenize the definition
        defn_tokens = sp(defn)
        for word in defn_tokens:
            if word.is_stop == False:
                def_words.append(word)

    #process words in definition
    def_syns_raw = []
    def_syns = []

    for word in def_words:
        for ss in wn.synsets(str(word)):
            for l in ss.lemma_names():
                def_syns_raw.append(str(l).upper()) #add as uppercase 

    #add words from the original processed synset
    for word in syns:
        def_syns_raw.append(word)

    #remove duplicates
    for word in set(def_syns_raw):
        def_syns.append(str(word))

    #re-check for original input words
    for word in def_syns:
        wordstr = str(word).upper()
    if wordstr in syns:
        while wordstr in syns:
            def_syns.remove(wordstr)
    ten_words = random.sample(def_syns, 10)

if len(ten_words) == 0:
    print("word(s) not recognized or stop word(s)")
else:
    print(ten_words)