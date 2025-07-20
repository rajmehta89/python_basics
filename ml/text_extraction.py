#countvactorization basiclaly do to count every unique word into the documnet like what are they and what are the catual count of tat messages here 
#the ocumnet will known as the Document Term Matrix (DTM)
#we can know like how are the unique words and what are there count frequencies and all that very easily..add()

# ✅ Count Vectorization (CountVectorizer) — Simple Definition
# CountVectorization is a technique to convert text (words/sentences) into numbers so that machine learning algorithms can work with it.

# 💡 How It Works:
# It:

# Splits text into words (called "tokens"),

# Counts how many times each word appears,

# Creates a numerical vector (1 row per document, 1 column per word).

# 📦 From scikit-learn:
# python
# Copy code
# from sklearn.feature_extraction.text import CountVectorizer

# corpus = ["I love NLP", "NLP is fun", "I love learning"]
# vectorizer = CountVectorizer()
# X = vectorizer.fit_transform(corpus)
# 🧾 Example Step-by-Step:
# Corpus:

# python
# Copy code
# ["I love NLP", "NLP is fun", "I love learning"]
# 🔤 Vocabulary (all unique words):

# css
# Copy code
# ['fun', 'learning', 'love', 'nlp', 'is', 'i']
# 🧮 Count Matrix:

# kotlin
# Copy code
#                  fun  learning  love  nlp  is  i
# "I love NLP"       0        0     1    1   0   1
# "NLP is fun"       1        0     0    1   1   0
# "I love learning"  0        1     1    0   0   1
# Each row = 1 sentence
# Each column = 1 word from the vocabulary
# Each number = how many times the word appears in the sentence

# ✅ Output Type:
# X is a sparse matrix (efficient storage), you can convert to array:

# python
# Copy code
# X.toarray()
# 🔁 Summary:
# What it does	Example
# Converts text to numbers	"I love NLP" → [0, 0, 1, 1, 0, 1]
# Basis	Word frequency (bag of words)
# Used in	Text classification, spam detection, etc


#term-matrix document.....

# ✅ Why use TF-IDF instead of CountVectorizer?
# CountVectorizer only tells you how frequently a word appears.

# TF-IDF tells you how important a word is in a document, by reducing the weight of common words like “the”, “is”, “and”.

# 💡 TF-IDF = Term Frequency × Inverse Document Frequency
# Let’s break this down:

# 1. TF (Term Frequency)
# How often a word appears in a document.

# Formula:

# javascript
# Copy code
# TF = (Number of times word appears in document) / (Total words in document)
# 🧠 Example:
# If the word "NLP" appears 3 times in a 100-word document:
# → TF = 3 / 100 = 0.03

# 2. IDF (Inverse Document Frequency)
# Tells how rare or common a word is across all documents.

