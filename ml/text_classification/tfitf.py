from sklearn.feature_extraction.text import TfidfVectorizer

# Example: list of text documents (replace this with your actual text data)
documents = [
    "Customer called customer support for a refund.",
    "No service complaints from this customer.",
    "Customer requested to cancel their service.",
    "Customer upgraded to premium plan last month."
]

# Create the vectorizer instance
vectorizer = TfidfVectorizer()

# Fit and transform the documents into a TF-IDF matrix
tfidf_matrix = vectorizer.fit_transform(documents)

# To see what features (words) were extracted:
print(vectorizer.get_feature_names_out())

# To print the resulting matrix as an array:
print(tfidf_matrix.toarray())
