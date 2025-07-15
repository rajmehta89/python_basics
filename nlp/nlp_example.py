import spacy

# Load small English model
nlp = spacy.load('en_core_web_sm')

# Process the text
doc = nlp("Tesla is Looking at buying U.S. startup for $6 million")

# Iterate over tokens and print them
for token in doc:
    print(token.text, token.pos_, token.dep_)
    
print(nlp.pipeline)

print(nlp.pipe_names)
print('\n')
doc2=nlp(u"tesla is'nt looking       into startups anymore.")

for token in doc2:
    print(token.text, token.pos_, token.dep_)
    
print(doc2[0].pos_)
print('\n')
doc3=nlp(u'here here ere jere . efhrkfjrelf khfef egrkfr egrfirf. gfkege nekf r. ekfef.bekfef')

for sentence in doc3.sents:
    print(sentence)
    
print(doc3[5].is_sent_start)    
print('\n')
doc5=nlp(u'A 5km NYC cab ride costs $10.30 here')

for t in doc5:
    print(t)
    
#we can also find the named entities here for the  single string 
print('\n')
doc6=nlp(u'Apple to build a Hong Kong factory for $6 million')

for entities in doc6.ents:
    print(entities)
    print(entities.label_)
    print(str(spacy.explain(entities.label_)))
    print('\n')
    
#it will provide noun_chunks as well

from spacy import displacy

doc8=nlp(u'Apple is going to build a U.K. Factory fo $6 million')

# This will open the visualization in your web browser
# displacy.serve(doc8, style='dep', options={'distance': 110})

#this way we can also see entity related data as well 
# displacy.serve(doc8,style='ent',options={'distance':110})


#now  we are using stemmers here 

