# ✅ What is scikit-learn?
# scikit-learn is a powerful open-source Python library used for machine learning and data analysis.
# It provides simple and efficient tools for building models, training them, and evaluating their performance.

# 📦 What It's For:
# Task	Purpose
# Classification	Spam detection, image recognition, etc.
# Regression	Predict prices, trends, etc.
# Clustering	Customer segmentation, grouping, etc.
# Dimensionality Reduction	PCA, feature compression
# Model Selection	Cross-validation, grid search
# Preprocessing	Scaling, encoding, missing value handling

# 🧰 Key Features:
# Easy syntax like model.fit() and model.predict()

# Integrates with NumPy, pandas, and matplotlib

# Algorithms included: SVM, Random Forest, Logistic Regression, KNN, etc.

# Includes tools for train-test split, pipelines, metrics, and more

#----------------------------------------------------------------------------------------------------------


#  NumPy (Numerical Python)
# NumPy is a Python library used for fast math with arrays and matrices.

# 🔹 What it does:
# Creates powerful arrays (faster than Python lists)

# Helps in mathematical operations (add, multiply, stats, etc.)

# Used heavily in machine learning, AI, and data science

#----------------------------------------------------------------------------------------------------------


# ✅ pandas (Panel Data)
# pandas is a Python library for handling and analyzing data in table form (like Excel).

# 🔹 What it does:
# Lets you create DataFrames (rows & columns like a spreadsheet)

# Easy to filter, sort, group, clean data

# Widely used in data analysis and preprocessing

#now here i have defined whta is the mean of the numpy and pandas and how we have to actually use that here .....

#------------------------------------------------------------------------------------------------------------





# Here is a simple diagram of a Confusion Matrix for binary classification (e.g., spam vs ham):

# lua
# Copy code
#                  Predicted
#                 Spam    Ham
#               +--------------+
#   Actual Spam |   TP   |  FN  |
#               +--------------+
#         Ham   |   FP   |  TN  |
#               +--------------+



#so here youcan se ethe confusion metrics and how it is basically works here 


#------------------------------------------------------------------------------------
import numpy as np
import pandas as pd

# Correct and full path to the file

# Use 'latin1' or 'ISO-8859-1' encoding to handle non-UTF-8 characters
df = pd.read_csv(r'E:\python_basics\ml\spam.csv',encoding='latin1', usecols=[0, 1],names=["label", "message"], skiprows=1)

print(df.head())
print(len(df))


df.dropna(subset=['message'],inplace=True)
# Convert label to 0/1
df["label"] = df["label"].map({"ham": 0, "spam": 1})

# print(df['V1'].unique())


from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

vectorizer=CountVectorizer()

#x feature data
X=vectorizer.fit_transform(df['message'])

print('x lable will this now here',X)

print(X.shape)

#y is our lable data here 
y=df['label']

X_train,X_test,y_train,y_test=train_test_split(X,y , test_size=0.3 , random_state=42)

# print(X_train.shape)

# print(X_test.shape)


from sklearn.linear_model import LogisticRegression

lr_model=LogisticRegression(solver='lbfgs')

lr_model.fit(X_train,y_train)



from sklearn import metrics

predictions=lr_model.predict(X_test)

print(predictions)

print(metrics.confusion_matrix(y_test,predictions))


df=pd.DataFrame(metrics.confusion_matrix(y_test,predictions),index=['ham','spam'], columns=['ham','spam'])

print(df)

print(metrics.classification_report(y_test,predictions))

print(metrics.accuracy_score(y_test,predictions))

