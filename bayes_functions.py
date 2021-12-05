import pandas as pd
import re

import spacy
import nltk
import sklearn
import wordcloud
import matplotlib.pyplot as plt
import pandas as pd
import random
import numpy as np
import json
from sklearn.model_selection import train_test_split
train=[]
test=[]
def binary_naive_bayes(count_vectorizer, train_matrix, specialty):
  c_w_negative = np.asarray(train_matrix.todense()[train.PRESTA_EST != specialty, :].sum(0)).reshape(-1)
  c_w_positive = np.asarray(train_matrix.todense()[train.PRESTA_EST == specialty, :].sum(0)).reshape(-1)
  c_negative = (train.PRESTA_EST != specialty).sum()
  c_positive = (train.PRESTA_EST == specialty).sum()
  p_w_negative = (c_w_negative + 1) / c_negative # Probabilidad asociada a cada palabra en la clase negativa
  p_w_positive = (c_w_positive + 1) / c_positive
  r = np.log(p_w_positive / p_w_negative)
  term_doc_matrix_test = count_vectorizer.transform(test.SOSPECHA_DIAG)
  test_pred = term_doc_matrix_test.dot(r) > 0
  test_label = np.where(test.PRESTA_EST == specialty, True, False)
  confusion_matrix = pd.crosstab(test_label,test_pred)
  return (np.array(confusion_matrix).diagonal().sum() / np.array(confusion_matrix).sum())


def drop_unneded_columns(df):
  for name, values in df.iteritems():
    if name not in ['PRESTA_EST', 'SOSPECHA_DIAG']:
      df.drop(name, axis=1, inplace=True)

#SVD ~4 minutos
U, s, Vh = np.linalg.svd(x_D10K.toarray(), full_matrices=False)