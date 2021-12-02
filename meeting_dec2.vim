* Why did you the filtering of stopwords?:

stop_words_union = set(list(nltk_stopwords) + list(spacy_stopwords))
stop_words_final = []
for word in stop_words_union:
  if word not in spacy_stopwords:
    stop_words_final.append(word)
  if word not in nltk_stopwords:
    stop_words_final.append(word)

* Change function names and variable names to "20% legibilidad de su entrega"
* rankin es ranking

