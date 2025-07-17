

#spacy have  something 305 english stop words inot therre list 

import spacy
nlp=spacy.load('en_core_web_sm')


print(nlp.Defaults.stop_words)
print(len(nlp.Defaults.stop_words))

#we can also add teh stop words into the defaults to use this actually...

#nlp.vocab['mystery'].is_stop-->it will gives us false here 


# now adding new stop_word

nlp.Defaults.stop_words.add('btw')

nlp.vocab['btw'].is_stop=True

print(len(nlp.Defaults.stop_words))

#we can alos remove an stop word from the vocabs and then we can  see which is actually usefull and allhere 
