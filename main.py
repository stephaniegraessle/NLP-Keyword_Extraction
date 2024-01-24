import spacy
from nltk.tokenize import word_tokenize

en_model = spacy.load('en_core_web_sm') # load SpaCy English language model

stopwords = en_model.Defaults.stop_words

input_text = "This is some test text. I wonder which words this will remove."
text_tokens = word_tokenize(input_text)
tokens_without_stopwords = [word for word in text_tokens if not word in stopwords]

print(text_tokens)
print(tokens_without_stopwords)
