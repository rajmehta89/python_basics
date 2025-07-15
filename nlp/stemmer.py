
import nltk

from nltk.stem.porter import PorterStemmer


#suffix rules for the stemmer here that will help us for the redine our words actully here 
p_stemmer=PorterStemmer()

words=['run' , 'runner' , 'ran' , 'runs' , 'easily' , 'fairly']

for word in words:
    print(word+'----->'+p_stemmer.stem(word))
    

print('\n')
from nltk.stem.snowball import SnowballStemmer
   
#now this snowballstemmer basically here works defferently for another task so stemmering will be deffrently here     
s_stemmer=SnowballStemmer(language='english')

for word in words:
    print(word+'-------->'+s_stemmer.stem(word))    

    