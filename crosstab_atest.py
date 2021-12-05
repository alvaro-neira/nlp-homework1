import pandas as pd
import numpy as np

# foo = pd.Categorical(['a', 'b'], categories=['a', 'b', 'c'])
# bar = pd.Categorical(['d', 'e'], categories=['d', 'e', 'f'])
# confusion_matrix = pd.crosstab(foo, bar, dropna=False)
# print(confusion_matrix)

# test_label = np.array([True, True, True, True, True, False, True, False, True, True])
# test_pred = np.array([True, True, False, False, True, False, True, True, True, True])
# # test_pred = np.array([False, False, False, False, False, False, False, False, False, False])
# confusion_matrix = pd.crosstab(test_label, test_pred)
# print(confusion_matrix)
# print(f"diag={np.array(confusion_matrix).diagonal().sum()}")
# print(f"total={np.array(confusion_matrix).sum()}")
# tn = confusion_matrix[0][0]
# tp = confusion_matrix[1][1]
# fp = confusion_matrix[1][0]
# fn = confusion_matrix[0][1]
# print(f"tn={tn}")
# print(f"tp={tp}")
# print(f"fp={fp}")
# print(f"fn={fn}")

words=['hello','bye']
for idx, w in enumerate(words):
    print(f"{idx} {w}")

