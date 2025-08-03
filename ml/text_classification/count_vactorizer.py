from sklearn.feature_extraction.text import CountVectorizer

# Sample documents
documents = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?"
]

# Create an instance of CountVectorizer
vectorizer = CountVectorizer()

# Fit the vectorizer to the documents and transform the documents into a matrix
X = vectorizer.fit_transform(documents)

# Get the feature names (the words)
print(vectorizer.get_feature_names_out())

# Print the resulting document-term matrix (word counts)
print(X.toarray())


#te deffrence betwen the count vactorizer and TfidfVectorizer here is the deffrence betwenn that here 
# How is CountVectorizer different from TfidfVectorizer?
# CountVectorizer: Just counts words ("bag of words")—no importance adjustment, all words treated equally.

# TfidfVectorizer: Considers not just frequency, but how important a word is (words that appear in many documents get lower scores, to focus on unique/important words).

