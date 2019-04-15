import nltk
import os
import json
import re
import io
import sys
import time
from nltk.tag import StanfordNERTagger

jar = './stanford-ner/stanford-ner.jar'
model_fr = './stanford-ner/classifiers/trained-ner-model-french-ser.giz'

st = StanfordNERTagger(model_fr, jar, encoding='utf8')

def run_ner(text,user):
    # Tokenize: Split sentence into words
    tokenized_text = nltk.word_tokenize(text)
    # Run NER tagger on words
    classified_text = st.tag(tokenized_text)

    highlighted_text = highlight_tagged_text(classified_text)
    highlighted_text = highlighted_text.replace("|||d|||",
                                                """<li style="
                                                    background: #fff;
                                                    border-top: 1px solid #e6ecf0;
                                                    border-left: 1px solid #e6ecf0;
                                                    border-right: 1px solid #e6ecf0;
                                                    background-clip: padding-box;
                                                    list-style: none;"> 
                                                <blockquote style="
                                                    data-lang="fr">
                                                    <p lang="fr" dir="ltr">
                                                """)
    highlighted_text = highlighted_text.replace("|||f|||","""</blockquote></li>""")

    save_text_as_html_file(highlighted_text,user)

def run_ner2(text,user):
    # Tokenize: Split sentence into words
    tokenized_text = nltk.word_tokenize(text)
    # Run NER tagger on words
    classified_text = st.tag(tokenized_text)

    highlighted_text = highlight_tagged_text(classified_text)

    return highlighted_text


def highlight_tagged_text(tagged_text):
    html_returned = ""
    twitter_account=False
    span_begin = "<span title='{}' style='background-color:{}'>"
    span_end = "</span>"


    for word,tag in tagged_text:
        if twitter_account:
            twitter_account = False
            html_returned += "<strong>"  + word +  "</strong>"+" "
            continue

        if "PER" in tag:
            html_returned += span_begin.format("PERSONNE","#2fecff") + word + span_end+" "
        elif "LOC" in tag:
            html_returned += span_begin.format("LOCALISATION","#ff992f") + word + span_end+" "
        elif "ORG" in tag:
            html_returned += span_begin.format("ORGANISATION","#2fff5c") + word + span_end+" "
        elif word.startswith('@'):
            html_returned += "<strong>" + word + "</strong>"
            twitter_account = True
        else:
            html_returned += word+ " "

    return html_returned

def save_text_as_html_file(text, filename):
    with io.open(filename + '-ner.html', 'w', encoding='utf-8') as jfile:
        jfile.write(text)

def process(user, path):

    cadre = """
    |||d|||{}|||f|||
    """

    all_tweets =""
    for file in os.listdir(path) :
        with open(os.path.join(path, file), encoding='utf-8') as f:
            tweet = json.load(f)
            all_tweets += cadre.format(re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', tweet['text'], flags=re.MULTILINE))

    run_ner(all_tweets,user)

def process2(user, path):
    index=0
    all_tweets =""
    for file in os.listdir(path) :
        index+=1
        if index > 15:
            break
        with open(os.path.join(path, file), encoding='utf-8') as f:
            tweet = json.load(f)

            all_tweets += run_ner2(re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', tweet['text'], flags=re.MULTILINE),user)


    save_text_as_html_file(all_tweets,user)

def usage():
    print("Usage:")
    print("python {} <username>".format(sys.argv[0]))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    user = sys.argv[1]

    t0 = time.time()
    process(user, os.path.join(os.getcwd(),"samples","timeline","json"))
    t1 = time.time()

    print (str(t1-t0))