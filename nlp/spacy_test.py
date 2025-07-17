import spacy

# Load small English model
nlp = spacy.load('en_core_web_sm')

# Process the text
doc = nlp("Hello I am Raj Mehta")

# Iterate over tokens and print them
for token in doc:
    print(token.text)
