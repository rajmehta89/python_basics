import pandas as pd

# Make sure this path matches your actual file location
npr = pd.read_csv(r'E:\python_basics\ml\spam.csv',encoding='latin1', usecols=[0, 1],names=["label", "message"], skiprows=1)

print(npr.head())

from sklearn.feature_extraction.text import TfidfTransformer

tfidf=TfidfTransformer(max_df=0.95, min_df=2 , stop_words='english')

dtm=tfidf.fit_transform(npr['messages'])


from  sklearn.decomposition import NMF
nmf_model=NMF(n_components=7 , random_state=42)

nmf_model.fit(dtm)


tfidf.get_feature_names()[2300]


for index,topic in enumerate(nmf_model.components_):
    
#so after we find all the ropics and inside the word for that particular tpice then we can doo this here ..add()

topic_results=nmf_model.transform(dtm)

topic_results.argmax(axis=1)


npr['Topic']=topic_results.argmax(axis=1)

mytopic_dit={0: 'health', 1:'election' , 2:"legis" , 3: ' poli' , 4:'election' , 5:'music', 6:'edu'}

npr['Topic Label']=npr['Topic'].map(mytopic_dict)
   
npr.head()

    