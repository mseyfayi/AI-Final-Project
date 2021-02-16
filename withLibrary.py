import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

data = pd.read_csv('train.csv')
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(data)

print(X_train_counts)