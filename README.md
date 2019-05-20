## Prerequis
1. Installation des libs nécessaires

       pip install -r requirements.txt

2. Installation
 
       python
       >>> import nltk
       >>> nltk.download()
     
    * La popup "NLTK Downloader" s'ouvre après qq sec, sélectionner "all", puis DOWNLOAD
    * Une fois toutes les collections récupérées, fermer la fenêtre, et passer à la prochaine étape [exit() dans le terminal pour quitter]
    * /!\ /!\ /!\ add "NLTK_DATA", varEnv qui cible le répertoire du download /!\ /!\ /!\

3. Mise en place du dictionnaire 

- unzip
-     "[...]/stanford-ner/classifiers/trained-ner-model-french-ser.zip"
- and move file to get
-     "[...]/stanford-ner/classifiers/trained-ner-model-french-ser.giz"



	
	
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
    
    