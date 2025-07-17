import spacy

nlp=spacy.load('en_core_web_sm')

doc1=nlp(u"i am a runner running in a race beacuse i love to run  since i ran today")


#Lemmatization means:

# Changing a word to its correct base form (dictionary form).

# This base word is called a "lemma."

# 📌 Why do we need it?
# Words like:

# "running", "ran", "runs"
# all mean the same base action — "run"

# When machines read text, they should treat them as the same word.
# That’s what lemmatization helps with.

# 📊 Examples
# Word	Lemma	Explanation
# running	run	Present participle → base verb
# went	go	Past tense → base verb
# cars	car	Plural → singular noun
# better	good	Comparative → base adjective
# studies	study	Verb with “-ies” → base verb


#so lemmatization basiclaly means to form a word into its base form any how here 

#all indiviuals like run, ranning , runner has pointing to the same hashcode here 
#so by this way we can actually lemmtization the given words here


def show_lemmas(text):
    for token in text:
        print(f'{token.text:{12}} {token.pos_:{6}} {token.lemma:<{12}}  {token.lemma_}')
        
for token in doc1:
    print(token.text,'\t',token.pos_,'\t',token.lemma,'\t',token.lemma_)
    

print('\n')
doc2=nlp(u'i saw ten mice today!!!')

show_lemmas(doc2)