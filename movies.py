from bs4 import BeautifulSoup

import requests
from time import sleep
from random import randint

Name = []
Release_year = []
imdb_rating = []
metascore = []
votes = []
genre=[]


for x in range(1, 1001, 50):
    if(x==1):
        page= requests.get("https://www.imdb.com/search/title/?title_type=feature&user_rating=7.5,&sort=num_votes,desc")
    else:
        page=requests.get("https://www.imdb.com/search/title/?title_type=feature&user_rating=7.5,&sort=num_votes,desc&start=" +str(x)+ "&ref_=adv_nxt")
    
    soup = BeautifulSoup(page.content, 'html.parser')
    sleep(randint(2,10))
    
    movies=soup.find_all('div', class_ = "lister-item mode-advanced")
    for c in movies:
        names=c.h3.a.text
        Name.append(names)
    
        year=c.h3.find('span', class_ = 'lister-item-year text-muted unbold').text
        Release_year.append(year)
    
        genres=c.find('span', class_ = 'genre').text.strip()
        genre.append(genres)
    
        imdb=float(c.strong.text)
        imdb_rating.append(imdb)
    
        vote=int(c.find('span', attrs = {'name':'nv'})['data-value'])
        votes.append(vote)
    
        if c.find('div', class_ = 'ratings-metascore') is not None:
            meta=int(c.find('span', class_ = 'metascore').text)
            metascore.append(meta)
        else:
            metascore.append("not specified") 
        
    

import pandas as pd
df=pd.DataFrame({
"Name" : Name,
"Release_year" :Release_year,
"imdb_rating" :imdb_rating,
"metascore" :metascore,
"votes" :votes,
"genre" :genre 
})
df.index+=1 
pd.set_option("display.max_rows", None, "display.max_columns", None)
df
