
import nltk

from nltk.stem.porter import PorterStemmer

#🧾 Summary
# Feature	NLTK	spaCy
# Speed	❌ Slower	✅ Faster
# Ease of Use	❌ More code, verbose	✅ Clean, Pythonic
# Pre-trained Models	❌ Few or external	✅ Many, built-in
# Learning & Research	✅ Good	❌ Limited
# Industrial Use	❌ Not ideal	✅ Optimized


#💡 Summary
# Goal	Use NLTK	Use spaCy
# Understand word meanings	✅ Yes	❌ No
# Get synonyms/definitions/examples	✅ Yes	❌ No
# Fast processing & NER/POS/Syntax	❌ Okay	✅ Yes
# Word sense disambiguation	✅ Yes	❌ No

# 🧠 Final Answer:
# If your goal is to understand the exact meaning of words, get definitions, or explore different word senses (like "bank" = riverbank or money bank), NLTK is the better choice.


#What is spaCy? (In Simple Words)
# spaCy is a powerful library made for machines to understand human language.

# It helps your program do things like:

# Break a sentence into words ✅

# Find which word is a noun, verb, etc. ✅

# Find names of people, places, dates, companies in text ✅

# Understand sentence structure (who did what to whom) ✅

# Find relationships between words (e.g., subject, object) ✅

# Be very fast and accurate ✅

# Works best in real-world apps, like chatbots, search engines, etc. ✅

# 📌 Example
# python
# Copy code
# import spacy
# nlp = spacy.load("en_core_web_sm")

# text = "Barack Obama was born in Hawaii."
# doc = nlp(text)

# for ent in doc.ents:
#     print(ent.text, ent.label_)
# Output:

# nginx
# Copy code
# Barack Obama PERSON
# Hawaii GPE
# 🔹 So spaCy can recognize real-world things like people, locations, organizations — this is called Named Entity Recognition (NER).

# 🎯 So, what is spaCy actually for?
# spaCy is good for	Why it matters
# Fast and efficient text processing	Needed in real apps like search/chatbots
# Finding word types (POS tagging)	Helps computers understand grammar
# Named Entity Recognition (NER)	Extract useful info like names/places
# Dependency Parsing (who does what)	Understand relationships in a sentence
# Industrial NLP use	Works great in production environments

# 🧠 Simple Analogy
# If NLTK is like a textbook with grammar rules and vocabulary,

# Then spaCy is like a Google Assistant — fast, smart, practical, and used in real applications.



#🔧 Real Use Case
# Say you're building a chatbot:

# Use spaCy to understand the intent, extract names, places

# Use NLTK to look up meanings or synonyms of words in the query

# You get the best of both worlds!


#suffix rules for the stemmer here that will help us for the redine our words actully here 
p_stemmer=PorterStemmer()

words=['run' , 'runner' , 'ran' , 'runs' , 'easily' , 'fairly']

for word in words:
    print(word+'----->'+p_stemmer.stem(word))
    

print('\n')
from nltk.stem.snowball import SnowballStemmer
   
#now this snowballstemmer basically here works defferently for another task so stemmering will be deffrently here     
s_stemmer=SnowballStemmer(language='english')

for word in words:
    print(word+'-------->'+s_stemmer.stem(word))    


#here is the other way to do this things here 
print('\n')
wordss=['genrerous','generation','generously','genrate']

for word in wordss:
    print(word+'   ---->  '+s_stemmer.stem(word))
    
    
 
