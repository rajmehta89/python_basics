from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

# Example text data and labels (replace with your data)
documents = [
    "Customer wants a refund.",
    "Happy with the service.",
    "Customer cancelled subscription.",
    "Signed up for a new product."
]
labels = [1, 0, 1, 0]  # 1: churn, 0: not churn

# Define a pipeline that first vectorizes, then classifies
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('svc', LinearSVC())
])

# Fit the pipeline on your training data
pipeline.fit(documents, labels)

# Predict on new, unseen data
new_docs = ["Asked for cancellation", "Very satisfied customer"]
predictions = pipeline.predict(new_docs)
print(predictions)  # Output: array of predicted classes ([1, 0])



#here is the pipeline and the workingof the pipeline here like how it is workign and all here 

