import nltk

nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid==SentimentIntensityAnalyzer()

s='this is a good movie'

sid.polarity_scores(s)

#there are four terms here
#negatives
#neutrals here
#positives here
#compiund here

#to read the csv we areactually using the pandas here basically for thet now
 