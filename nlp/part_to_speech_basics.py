#let's explore part to speech folder here

import spacy
import spacy.attrs

nlp=spacy.load('en_core_web_sm')

doc=nlp(u'the quick brown fox jumpe dover the lazy dog\'s back')

print(doc.text)

print(doc[4].tag_)
print(doc[4].pos_)

for token in doc:
    print(f"{token.text:{10}} {token.pos_:{10}} {token.tag_:{10}} {spacy.explain(token.tag_)}")
       
#spacy will excatly know the sentence is basically having into the past or future means tense actually whatever it is here

print('\n')
doc2=nlp(u"i read books on NLP")

word=doc2[1]
token=word
print(f"{token.text:{10}} {token.pos_:{10}} {token.tag_:{10}} {spacy.explain(token.tag_)}")
      
doc3=nlp(u"i read a book on NLP")

word1=doc3[1]
token=word1
          
print(f"{token.text:{10}} {token.pos_:{10}} {token.tag_:{10}} {spacy.explain(token.tag_)}")
                         
#it is basiclaly counting like how many pos_counts and all are there actuallly doc=nlp()

doc=nlp(u'the quick brown fox jumped over the lazy dog\'sback.')
pos_counts=doc.count_by(spacy.attrs.POS)

print(pos_counts)

print(doc.vocab[84].text)
print(doc[2].pos)

print('\n')
for k,v in sorted(pos_counts.items()):
    print(f'{k} , {doc.vocab[k].text:{5}}  {v}')