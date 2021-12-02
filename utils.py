def normalizer(text, remove_tildes = True): #normalizes a given string to lowercase and changes all vowels to their base form
    text = text.lower() #string lowering
    text = re.sub(r'[^A-Za-zñáéíóú]', ' ', text) #replaces every punctuation with a space
    if remove_tildes:
        text = re.sub('á', 'a', text) #replaces special vowels to their base forms
        text = re.sub('é', 'e', text)
        text = re.sub('í', 'i', text)
        text = re.sub('ó', 'o', text)
        text = re.sub('ú', 'u', text)
    return text


stopwords_normalized = map(normalizer,stopwords_aysen)
corpus_normalized = normalizer(corpus_aysen)
corpus_normalized_no_stopwords = ""
for word in corpus_normalized.split(" "):
  if (len(word) > 3) & (word not in stopwords_normalized): # aquí eliminamos las palabras con 3 caracteres o menos y los stopwords usando la lista consolidada de stopwords
    corpus_normalized_no_stopwords += word +  " "
