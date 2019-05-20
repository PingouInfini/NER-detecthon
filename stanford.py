import os
import json
import re
import sys
import time
from nltk.tag import StanfordNERTagger
import services.nltoolkit as nlt

jar = './stanford-ner/stanford-ner.jar'
model_fr = './stanford-ner/classifiers/trained-ner-model-french-ser.giz'

st = StanfordNERTagger(model_fr, jar, encoding='utf8')

def process(user, path, quick):
    all_tweets = ""
    all_entities = {}
    for file in os.listdir(path) :

        with open(os.path.join(path, file), encoding='utf-8') as f:
            tweet = json.load(f)

            # TODO voir pour récup tout le tweet si + de 144 caractères
            tweet_text = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', tweet['text'], flags=re.MULTILINE)

            if quick:
                all_tweets += tweet_text
            else:
                new_entities = nlt.run_ner(st, tweet_text, user)
                all_entities = merge_map(all_entities, new_entities)


    if quick:
        new_entities = nlt.run_ner(st, all_tweets, user)
        all_entities = merge_map(all_entities, new_entities)

    print (all_entities)

def merge_map(full_map, new_map):

    for key, values in new_map.items():
        for value in values:
            full_map.setdefault(key,[]).append(value)

    return full_map

def usage():
    print("Usage:")
    print("python {} <username>".format(sys.argv[0]))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    user = sys.argv[1]

    ### Deux modes de traitement :
    # 1) concatener le scontenus des tweets en 1 text qui sera NERisé
    # 2) passer chaque tweet à la NER (bcp plus lent
    mode = 1

    t0 = time.time()
    process(user, os.path.join(os.getcwd(),"samples","json"), (mode ==1))
    t1 = time.time()

    print (str(t1-t0))