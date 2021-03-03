import spacy
import re
from nltk.stem import WordNetLemmatizer

sp = spacy.load('en_core_web_sm')
all_stopwords = sp.Defaults.stop_words

new_words = ["http", "www", "co", "u", "com", "t", "s", "m",
             "ve", "dy", "ll", 'n', 'r', 'b', "wa", "y", "don", "ha"]
for words in new_words:
    all_stopwords.add(words)

wordnet = WordNetLemmatizer()


def clean_text(text, stopwords=all_stopwords):
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower()
    text = text.split(' ')
    text = [wordnet.lemmatize(word) for word in text]
    text = [word for word in text if word not in stopwords]
    text = ' '.join(text)
    return text
