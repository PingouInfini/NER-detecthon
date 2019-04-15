## Prerequis

unzip
- "stanford-ner/classifiers/trained-ner-model-french-ser.zip"

and move file to get\
- "stanford-ner/classifiers/trained-ner-model-french-ser.giz"

	
===

Tuto:
	
- https://blog.sicara.com/train-ner-model-with-nltk-stanford-tagger-english-french-german-6d90573a9486

Download lib:

- https://nlp.stanford.edu/software/CRF-NER.html#Download

Corpus from newspaper (FR, DE, NL)

- https://github.com/EuropeanaNewspapers/ner-corpora



## Train you own model

Check "tuto" -> ~15-20 min to prepare it

    java -cp "stanford-ner.jar" -mx4g edu.stanford.nlp.ie.crf.CRFClassifier -prop train/prop.txt
    
    