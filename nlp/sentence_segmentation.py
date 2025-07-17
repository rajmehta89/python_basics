import spacy 
from spacy.language import Language
nlp=spacy.load('en_core_web_sm')

doc=nlp(u'"management is doing teh right things; leadership is doing the right things."')

print(doc.text)

for sent in doc.sents:
    print(sent)
    print('\n')
    
#add a segmentatipon rule
#means all time we dont just have to segment the text based on the space and all sometime we actully need the customization to do that thins as well
# Custom segmentation rule: set new sentence start after a semicolon
@Language.component("set_custom_boundaries")
def set_custom_boundaries(doc):
    for token in doc[:-1]:
        if token.text == ";":
            doc[token.i + 1].is_sent_start = True
    return doc

#first check for the sentence which i based on our modifier or not and then we are actually modifying on that 
# Add the custom component before the parser
nlp.add_pipe("set_custom_boundaries", before="parser")

# Input text
doc = nlp(u'"Management is doing the right things; leadership is doing the right things."')

# Print all the sentences
for sent in doc.sents:
    print(sent)


#the default segentation is based in the '\n
#but i ave define the custom_segmnetation here as welll

#how the spacy is basiclaly split on by default so as we know here
# ✅ 1. Punctuation (like ., !, ?)
# These are strong hints for sentence endings.

# But spaCy does not blindly split on them — it uses context too.

# Examples:

# text
# Copy code
# Hello! How are you? I'm fine.
# Segments into 3 sentences:
# Hello!, How are you?, I'm fine.

# ✅ 2. Abbreviations
# spaCy checks if a dot is part of a known abbreviation, like Dr., Mr., Inc.

# It doesn't split after these unless the next word starts a real sentence.

# text
# Copy code
# I met Dr. Smith today. He is nice.
# ✅ Correctly splits after Smith, not after Dr.

# ✅ 3. Capital letters at the start of a token
# A word starting with a capital letter after a punctuation is a strong signal for a new sentence.

# text
# Copy code
# I saw a dog. It was barking.
# ✔ “It” starts with a capital → New sentence likely

# ✅ 4. Dependency parse context
# spaCy uses grammatical structure to decide if a sentence makes sense as a unit.

# Even without punctuation, it can detect sentence boundaries based on verb structure.

# text
# Copy code
# Let's go now then we can eat.
# → May still split into:

# Let's go now.

# Then we can eat.
# (because “then we can eat” is a valid clause)

# ✅ 5. Quotes and brackets
# spaCy handles sentence segmentation inside quotes/brackets too:

# text
# Copy code
# He said, "Let's go." Then he left.
# ✔ Two separate sentences

# ❌ What spaCy doesn’t use by default:
# It does not split sentences on:

# commas ,

# semicolons ; (unless grammar says it should)

# newlines (unless you set nlp.select_pipes() or customize)

# 💡 TL;DR:
# spaCy uses:

# Feature	Used for sentence end?
# . ! ?	✅ Yes (with grammar check)
# Abbreviations	❌ Not split
# Capital letters	✅ Help signal start
# Grammar rules	✅ Always checked
# " ' ()	✅ Properly handled
# , ; :	❌ Not split by default





