import spacy

nlp=spacy.load('en_core_web_sm')

def show_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            print(ent.text+' - '+ent.label_+' - '+str(spacy.explain(ent.label_)))
            
    else:
        print('no entities are found')
 


doc=nlp(u'Hi How are you?')
show_ents(doc)

doc=nlp(u'May I go to Washinton, DC next May to see the washington  Monumnet?')
show_ents(doc)

#we can find 

#ent.text--> teh original entity text
#ent.label-->the entity types hash value
#ent.label_->te entity type;s string  description
#ent.start->the token  span;s "start" index position in the doc
#ent.end-> the token span;s "stop" index position in the doc

doc=nlp(u'hello raj how are you ?')
show_ents(doc)

#now we can add named entity recognzation as much we want bt now the concern is how can we  add and then basiclaly analysis that laos here 


#what is span is basiclally so itis like 
#  What is Span in spaCy?
# In spaCy, a Span is a slice of a Doc object — a span of words (tokens) from the document.

# It’s used to represent a continuous sequence of tokens, for example:

# a named entity (New York City)

# a phrase (5 million dollars)

# or a custom-defined term (Gujarat)


import spacy
from spacy.tokens import Span
from spacy import displacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = "Apple is opening a new office in Gujarat, India worth 5 million dollars."

# Process the text
doc = nlp(text)

# ✅ Step 1: View existing entities
print("Original Entities:")
for ent in doc.ents:
    print(ent.text, ent.label_)

# ✅ Step 2: Add a custom entity manually
# Let's say we want to mark "Gujarat" as a custom entity type "REGION"
start = text.split().index("Gujarat")  # crude way to find position
start_char = text.index("Gujarat")
end_char = start_char + len("Gujarat")

# Create a new Span with label
new_ent = Span(doc, doc.char_span(start_char, end_char).start, doc.char_span(start_char, end_char).end, label="REGION")

# Add the new entity to the doc
doc.ents = list(doc.ents) + [new_ent]

# ✅ Step 3: Visualize the entities with displacy
print("\nAfter Adding Custom Entity:")
for ent in doc.ents:
    print(ent.text, ent.label_)

# Visualize in browser
displacy.serve(doc, style="ent")

