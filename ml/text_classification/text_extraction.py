import numpy as np
import pandas as  pd

# Make sure this path matches your actual file location
df = pd.read_csv(r'E:\python_basics\ml\spam.csv',encoding='latin1', usecols=[0, 1],names=["label", "message"], skiprows=1)

print(df.head())
print(len(df))

print(df.isnull().sum())

print(df['label'].value_counts)

from sklearn.model_selection import train_test_split

X=df['message']

y=df['label']

X_train,X_test,y_train,y_split=train_test_split(X,y,test_size=o.33,random_state=42)


from sklearn.feature_extraction.text from CountVectorizer

count_vect=CountVectorizer()

#FIT VECTORRIZER TO THE DATA(buil a vocablary)
#Transform THE ORIGINAL TEXTMESSAGE--->VECTOR

count_vect.fit(X_train)



