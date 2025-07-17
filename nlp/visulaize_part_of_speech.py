import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')
doc = nlp("Apple is looking at buying a startup in the UK.")

# Visualize POS tags
displacy.render(doc, style='dep', jupyter=True)  # Use in Jupyter Notebook



#What you'll see:
# Words are shown with arrows connecting them, showing their relationships.

# POS tags (like NOUN, VERB) are shown above each word.

# It's an easy way to understand sentence structure and word roles visually.

# Let me know if you're running it in VS Code or another environment, I’ll adjust the method for that.