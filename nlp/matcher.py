import spacy
nlp=spacy.load('en_core_web_sm')

from spacy.matcher import Matcher

matcher=Matcher(nlp.vocab)

#now we are matching the things here 


#solarpower
pattern1=[{'LOWER':'solarpower'}]

#solar-power
pattern2=[{'LOWER':'solar'},{'IS_PUNCT':True},{'LOWER':'power'}]

#solar power
pattern3=[{'LOWER':'solar'},{'LOWER':'power'}]


#Great! You're exploring spaCy's Matcher, and you're absolutely on the right track.

# Let’s break it all down simply so you understand what Matcher is, how it works, and why it’s useful in NLP.

# 🔍 What is Matcher in spaCy?
# The Matcher is a rule-based pattern matcher in spaCy.

# It lets you search for specific sequences of tokens (words) in text — based on:

# text

# part-of-speech

# punctuation

# lemma

# lowercase forms

# etc.

# 📌 Why use Matcher?
# You use it when you want to find custom patterns in text like:

# Specific phrases (like “solar power”, “data science”)

# Word combinations (like adjective + noun)

# Named expressions not covered by NER

# Custom search in legal/medical/technical texts


#so here you can see how the matcher is basiclaly used here what is teh concern ehind that to use  matcher 
#for sometimes domain specific knowledge and here

# Summary (Why Matcher is useful in NLP):
# Helps custom search in text using flexible rules

# Useful when NER doesn't cover your use case

# Perfect for domain-specific phrase detection

# Supports combining rules: POS, punctuation, lemma, etc. 


#here we are setting callback=None here 
matcher.add("SolarPower", [pattern1, pattern2, pattern3])

doc=nlp(u'The Solar Power industry continues to grow a solarpower increases. solar-power is amazing')

found_matches=matcher(doc)

print(found_matches)

#[(8656102463236116519, 1, 3), (8656102463236116519, 8, 9), (8656102463236116519, 11, 14)]
#here you can see teh id of the matcher and the start of the token and then en dof the token actually here this way itis working here out

#we can remove also the matcher here basically here 
#matcher.remove('SolarPower')
