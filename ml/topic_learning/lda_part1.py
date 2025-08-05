import pandas as pd

# Make sure this path matches your actual file location
npr = pd.read_csv(r'E:\python_basics\ml\spam.csv',encoding='latin1', usecols=[0, 1],names=["label", "message"], skiprows=1)

print(npr.head())


from  sklearn.feature_extraction.text import CountVectorizer

cv=CountVectorizer(max_df=0.95, min_df=2,stop_words='english')

dtm=cv.fit_transform(npr['message'])
 
print(dtm)
 
from  sklearn.decomposition import LatentDirichletAllocation

LDA=LatentDirichletAllocation(n_components=7 , random_state=42)

LDA.fit(dtm)


#grab the voabulary of words

print(len(cv.get_feature_names_out()))

#the type of the word here is

print(cv.get_feature_names_out())


#grab the topics

len(LDA.components_)



LDA (Latent Dirichlet Allocation) is a powerful topic modeling algorithm used in Natural Language Processing (NLP). It helps discover the hidden topics in a large collection of text documents.

# 🔍 What is LDA, in simple words?
# Think of LDA as a way to automatically organize a bunch of documents (like emails, news, reviews, etc.) by identifying topics that occur in them.

# It does not need labels or training — it’s an unsupervised learning method.

# 💡 Analogy:
# Imagine you are given thousands of books written in different genres — but without any genre label.
# LDA will analyze the words in the books and group them by topics — like sports, politics, science, romance, etc., based on word patterns.

# 🔧 How LDA works (simplified):
# Each document is assumed to be a mix of topics.

# Each topic is a mix of words.

# LDA tries to:

# Find out which topics each document talks about.

# Find out which words belong to which topics.

# 📊 Example:
# If you run LDA on a bunch of SMS messages:

# Topic 1 → {win, prize, cash, free, claim}

# Topic 2 → {love, hey, good, meet, night}

# Topic 3 → {urgent, reply, call, now, mobile}

# So you can say:

# Messages in Topic 1 are probably spam.

# Messages in Topic 2 are probably personal.

# Messages in Topic 3 are urgent communications.

# 📦 In your code:
# python
# Copy code
# LDA = LatentDirichletAllocation(n_components=7, random_state=42)
# LDA.fit(dtm)
# n_components=7 → You want LDA to find 7 topics from your messages.

# dtm is the document-term matrix created using CountVectorizer.

# ✅ LDA is useful for:
# Organizing and summarizing large text data

# Discovering hidden themes

# Recommender systems

# Customer review analysis

# Spam detection


# 🔍 What is dtm in this code?
# python
# Copy code
# dtm = cv.fit_transform(npr['message'])
# Here, dtm stands for Document-Term Matrix.

# 📦 Think of it like this:
# You have a bunch of messages (SMS texts, in your case).
# Each message is a document made of words.

# The CountVectorizer breaks every message into individual words and counts how many times each word appears.

# 📊 The result (dtm) looks like a big table:
# Message #	Word1	Word2	Word3	...
# msg 1	1	0	2	...
# msg 2	0	3	0	...
# ...	...	...	...	...

# Rows → each message (document)

# Columns → each word (term)

# Value → how many times that word appears in that message

# 🎯 Why do we need it?
# Because LDA (Latent Dirichlet Allocation) can’t read plain text —
# It needs numbers that show which words are in which messages and how many times.

# The DTM is like feeding the LDA a numeric summary of the text.

# 📘 Final Analogy:
# If your messages are books, the DTM is like a library catalog showing which words appear in which book and how often.

# And LDA uses that catalog to figure out what topics those books might be about.


# 🔶 What is the actual use of Non-negative Matrix Factorization (NMF)?
# Non-negative Matrix Factorization (NMF) is used to discover hidden patterns or topics in large collections of text or data.

# 🎯 Real-World Simple Example:
# Imagine you have a bunch of news articles. Each article talks about some topics like:

# Sports

# Politics

# Technology

# Health

# But you don’t know in advance which articles are about what.

# 🧠 What NMF does:
# You turn all the articles into a matrix using CountVectorizer or TfidfVectorizer.

# Rows = documents (articles)

# Columns = words

# Values = how many times each word appears in each document

# This is your Document-Term Matrix (DTM).

# NMF breaks this matrix into two smaller matrices:

# One tells you which words belong to which topic.

# The other tells you which documents belong to which topic.

# And the cool part:
# ✅ All values are non-negative (no negatives), which makes it easier to interpret.

# 💡 Think of it like this:
# If you bake a cake (original data), NMF is like breaking it down to find out how much flour, sugar, and butter went into it (topics/components).

# ✅ So why use NMF?
# To automatically discover topics in text (topic modeling)

# For recommendation systems (like Netflix recommending based on genres)

# For dimensionality reduction (reducing complexity while keeping meaning)


# ✅ Definition (Simple):
# Non-negative Matrix Factorization (NMF) is a technique that breaks a big matrix into two smaller ones — using only positive numbers — to find hidden patterns or topics in data.

# 🧠 Why "non-negative"?
# Because in real life, we don’t have negative counts for things like:

# Word frequencies

# Product ratings

# Time spent
# So, NMF sticks to only positive values, making it easier to understand.

# 🔍 What is NMF used for?
# 📰 Topic Modeling: Finding hidden topics in a bunch of documents or articles

# 📺 Recommender Systems: Suggesting products, movies, etc.

# 🧬 Bioinformatics: Finding patterns in gene expressions

# 📊 Dimensionality Reduction: Simplifying big data into important parts

# 📦 How it works (Very Simply):
# Let’s say we have a document-term matrix like this:

# word1	word2	word3
# Doc A	2	3	0
# Doc B	0	1	4

# ➡️ NMF breaks this into:

# A Document-Topic matrix: (e.g., Doc A = 70% Topic 1, 30% Topic 2)

# A Topic-Word matrix: (e.g., Topic 1 = mostly word1 and word2)

# 🎯 Simple Example:
# Imagine you have 100 movie plots and you want to find the types of movies (like Action, Comedy, Drama) without reading them.

# NMF can:

# Find the hidden topics (Action, Comedy, etc.)

# Tell you which words are common in each topic

# Show you which movie belongs to which topic

# ✍️ Final Definition to Remember:
# NMF is a machine learning technique that finds parts-based, easy-to-understand structure in your data — especially useful when your data has only positive values, like word counts or views.


