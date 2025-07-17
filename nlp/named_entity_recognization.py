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

