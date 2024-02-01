from numpy import true_divide
import pandas as pd
import bs4
import webbrowser
import requests
from bs4 import BeautifulSoup
source_bolly = requests.get("https://www.imdb.com/list/ls009997493/")
source_bolly.raise_for_status()
soup_bolly = BeautifulSoup(source_bolly.content,'html.parser')
mova_bolly = soup_bolly.find('div',class_="pagecontent").find_all(class_="lister-item mode-detail")
movies_bolly=[]
for i in range(0,50):
     movies_bolly.append(mova_bolly[i])
# print(len(movies_bolly))
def get_data_of_movie(movie):
     trailer = movie.a.get('href')
    #trailer=tai.a.get('href')
     return trailer
print((get_data_of_movie(movies_bolly[0]))[0])