import nltk

def run_ner(st, text, user):
    # Tokenize: Split sentence into words
    tokenized_text = nltk.word_tokenize(text)
    # Run NER tagger on words
    classified_text = st.tag(tokenized_text)

    entities = extract_entities(classified_text)
    return entities

def extract_entities(tagged_text):
    entities = dict()
    for word,tag in tagged_text:
        if "PER" in tag:
            entities.setdefault(tag,[]).append(word)
        elif "LOC" in tag:
            entities.setdefault(tag,[]).append(word)
        elif "ORG" in tag:
            entities.setdefault(tag,[]).append(word)
        elif word.startswith('@'):
            #TODO A considérer comme un compte twitter?
            pass
        else:
            pass
    return entities