import pandas as pd
from datetime import datetime
import altair as alt
import streamlit as st
# import matplotlib.pyplot as plt
# from bs4 import BeautifulSoup
# #from nltk.stem.snowball import FrenchStemmer
# import re
# from nltk.corpus import stopwords
# # Download the punkt tokenizer for sentence splitting
# import nltk.data
# # Import the built-in logging module and configure it so that Word2Vec creates nice output messages
# import logging
# import time
# import itertools

# import numpy as np
# from pandas.plotting import register_matplotlib_converters


# def text_to_float(x):
#     if  isinstance(x, str):
#         x=x.lower()
# #         if x=='nan' or x=='none' or x=='None':
# #             return(0.0)
#         if 'k' in x:
#             return(float(x[:len(x)-1])*1000)
#         else:
#             return(float(x))
#     else:
#         return(0.0)
    

# def text_to_floatm(x):
#     if isinstance(x, float):
#         return(x)
#     if  isinstance(x, str) and 'k' in x:
#         x=x.lower()
#         return(float(x[:len(x)-2].replace(',','.'))*1000)
#     if ',' in x:
#         return(float(x[:len(x)-3]))
#     else:
#         return(0.0)

# #prend un mot et un tweet, renvoie 1 si le mot est dans le tweet 0 sinon
# def word_in(mot,x):
#     if mot in x:
#         return(1)
#     else:
#         return(0)
    





    
    
# def lasq_date(x):
    
#     y=x[:10]
#     d=x[11:len(x)-5]
#     dd=y+' '+d
#     return(datetime.strptime(dd, '%Y-%m-%d %H:%M:%S'))
        

# def lasq_heure(x):
    
    
#     d=x[11:len(x)-5]

#     return(datetime.strptime(d, '%H:%M:%S'))
        




# alpha = 44.26 #coefficient de normalisation

# covid = pd.read_csv('covid.csv', sep= ';', usecols=['date','vac_statut','nb_PCR+','nb_PCR+_sympt','HC','SC'])

macron=pd.read_csv('Df_mac.csv.csv')
zemour=pd.read_csv('Df_zem.csv.csv')
mel=pd.read_csv('Df_mel.csv.csv')
# macron2 = pd.read_csv('Macronn2.csv',usecols=['Timestamp','Embedded_text','Comments', 'Likes', 'Retweets'])

# zemmour1 = pd.read_csv('Zemmourall1.csv',usecols=['Timestamp','Embedded_text','Comments', 'Likes', 'Retweets'])
# zemmour2 = pd.read_csv('Zemmourall2.csv',usecols=['Timestamp','Embedded_text','Comments', 'Likes', 'Retweets'])



# zemmour=pd.concat([zemmour1,zemmour2])
# macron  =pd.concat([macron1, macron2])
# zemmour = zemmour.drop_duplicates(['Timestamp'])
# macron = macron.drop_duplicates(['Timestamp'])

# listd=[1113,1316,1622]
# df=pd.read_csv('Mel_0911.csv')
# for k in range(1,len(listd)):
#     dt=pd.read_csv(f"Mel_{listd[k]}.csv")
#     df=pd.concat([df, dt])

# mell=df.drop_duplicates()

# mell=mell.fillna(0.0)
# zemmour = zemmour.fillna(0.0)

# macron = macron.fillna(0.0)

# zemmour['Likes'] = zemmour['Likes'].apply(lambda x : text_to_float(x) )
# zemmour['Comments'] = zemmour['Comments'].apply(lambda x : text_to_float(x) )
# zemmour['Retweets'] = zemmour['Retweets'].apply(lambda x : text_to_float(x) )
# zemmour['date'] = zemmour['Timestamp'].apply( lambda x : lasq_date(x) )
# zemmour['heure'] = zemmour['Timestamp'].apply( lambda x : lasq_heure(x) )

# macron['Likes'] = macron['Likes'].apply(lambda x : text_to_float(x) )
# macron['Comments'] = macron['Comments'].apply(lambda x : text_to_float(x) )
# macron['Retweets'] = macron['Retweets'].apply(lambda x : text_to_float(x) )
# macron['date'] = macron['Timestamp'].apply( lambda x : lasq_date(x) )
# macron['heure'] = macron['Timestamp'].apply( lambda x : lasq_heure(x) )

# mell['Likes'] = mell['Likes'].apply(lambda x : text_to_floatm(x) )
# mell['Comments'] = mell['Comments'].apply(lambda x : text_to_floatm(x) )
# mell['Retweets'] = mell['Retweets'].apply(lambda x : text_to_floatm(x) )
# mell['date'] = mell['Timestamp'].apply( lambda x : lasq_date(x) )
# mell['heure'] = mell['Timestamp'].apply( lambda x : lasq_heure(x) )


# DataZ = zemmour[['date','Timestamp','Likes','Comments','Retweets']]
# DataM = macron[['date','Timestamp','Likes','Comments','Retweets']]
# DataMel = mell[['date','Timestamp','Likes','Comments','Retweets']]


# DataZ['SMA_L3']=DataZ.iloc[:,2].rolling(window=50).mean()
# DataZ['SMA_C3']=DataZ.iloc[:,3].rolling(window=50).mean()
# DataZ['SMA_R3']=DataZ.iloc[:,4].rolling(window=50).mean()

# DataM['SMA_L3']=DataM.iloc[:,2].rolling(window=50).mean()
# DataM['SMA_C3']=DataM.iloc[:,3].rolling(window=50).mean()
# DataM['SMA_R3']=DataM.iloc[:,4].rolling(window=50).mean()

# DataMel['SMA_L3']=DataMel.iloc[:,2].rolling(window=50).mean()
# DataMel['SMA_C3']=DataMel.iloc[:,3].rolling(window=50).mean()
# DataMel['SMA_R3']=DataMel.iloc[:,4].rolling(window=50).mean()

mDf=pd.read_csv('occurM.csv')
diccc=mDf.set_index('Unnamed: 0').T.to_dict('list')

DataMtronc1=macron[macron['date']>'2019-11-01 21:53:43']
E=['SMA_R3','SMA_C3','SMA_L3']

# base = alt.Chart(DataMtronc1)

# line1 = base.mark_line().encode(
#     x='date',
#     y=E[0],
#     #color='symbol'
# )
# line2 = base.mark_line(color="#FFAA00").encode(
#     x='date',
#     y=E[1],
# )


st.title('Comparateur de tweets de politiciens')

# st.line_chart(DataZ['SMA_L3'])
# st.line_chart(DataM['SMA_R3'])

#st.altair_chart(line1+line2, use_container_width=True)

# option = st.sidebar.checkbox('test ?') 

# st.write(option)


pol1 = st.radio(
     "quel est le premier  politicien que vouz choisisez? (bleu) ",
     ('Zmmour', 'Macron', 'Mellonchon'))

pol2 = st.radio(
     "quel est le deuxieme  politicien que vouz choisisez? (rouge) ",
     ('Zmmour', 'Macron', 'Mellonchon'))

var = st.radio(
     "quel est la  variable que vous souhaitez visualiser ",
     ('re-tweets', 'commentaires', 'likes'))

# var2 = st.radio(
#      "quel est la deuxieme  variable que vous souhaitez visualise",
#      ('re-tweets', 'commentaires', 'likes'))


# d = st.date_input(
#      "When's your birthday",
#      datetime.date(2019, 7, 6))
# st.write('Your birthday is:', d)

d1 = st.date_input(
     "La date du début")
format= '%Y-%m-%d %H:%M:%S'

dd1=d1.strftime('%Y-%m-%d %H:%M:%S')

  
d2 = st.date_input(
     "La date de fin")

dd2=d2.strftime('%Y-%m-%d %H:%M:%S')
  
pols= ['Zmmour', 'Macron', 'Mellonchon']

class Candidat(str):

    def __init__(self,str):

        if str is 'Zmmour':

            self.data = zemour[dd1<zemour['date']]
            self.data=self.data[self.data['date']<dd2]

        if str is 'Macron':
            self.data=macron[dd1<macron['date']]
            self.data=self.data[self.data['date']<dd2]
        
        if str is 'Mellonchon':
            self.data=mel[dd1<mel['date']]
            self.data=self.data[self.data['date']<dd2]
    


Abstractpol1=Candidat(pol1) 
Abstractpol2=Candidat(pol2) 

base1 = alt.Chart(Abstractpol1.data)
base2=alt.Chart(Abstractpol2.data)

if var=='re-tweets':
    line11 = base1.mark_line().encode(
        x='date',
        y=E[0],)
    line12 = base2.mark_line(color='red').encode(
        x='date',
        y=E[0],)

if var=='commentaires':
    line11 = base1.mark_line().encode(
        x='date',
        y=E[1],)
    line12 = base2.mark_line(color='red').encode(
        x='date',
        y=E[1],)

if var=='likes':
    line11 = base1.mark_line().encode(
        x='date',
        y=E[2],)
    line12 = base2.mark_line(color='red').encode(
        x='date',
        y=E[2],)
    


st.altair_chart(line11+line12, use_container_width=True)


option = st.sidebar.checkbox('quel mot?')

st.write('Your birthday is:', d)

# ID={pol1:{
# df
# },
# pol2:{

# }}
