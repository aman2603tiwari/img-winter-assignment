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
     name = movie.find("h3",class_="lister-item-header").a.text
     year = movie.find("span",class_="lister-item-year text-muted unbold").text.strip('()')
     rating =movie.find('span','ipl-rating-star__rating').text
     desc = movie.find('p',class_='').text
     runtime= movie.find('span',class_='runtime').text
     genre = movie.find('span',class_='genre').text
     img = movie.img.get('loadlate')
    #  trailer = movie.a.get('href')
    #trailer=tai.a.get('href')
     return name,year,rating,desc,runtime,genre,img


genre_list_bolly=["Crime","Drama","Biography","History","Sport","Romance","Mystery","Family","Fantasy","Adventure"]
genre_list_bollys={}
for genre in genre_list_bolly:
    genre_list_bollys[f'genre_list_bolly_{genre}']=[]
    for movie in movies_bolly:
      if ((get_data_of_movie(movie))[5]).find(f'{genre}')!=-1:
        genre_list_bollys[f'genre_list_bolly_{genre}'].append(get_data_of_movie(movie)[0])
# print(genre_list_bollys)    


rank_list_bolly=["7-7.5","7.5-8","8-8.5","8.5-9","9-9.5","9.5-10"]
rank_list_bollys={}
for rank in rank_list_bolly:
    rank_list_bollys[f'rank_list_bolly_{rank}']=[]
for movie in movies_bolly:
    if float(((get_data_of_movie(movie)))[2])>=7 and float(((get_data_of_movie(movie))[2]))<7.5 :
         rank_list_bollys[f'rank_list_bolly_7-7.5'].append(get_data_of_movie(movie)[0])
    elif float(((get_data_of_movie(movie)))[2])>=7.5 and float(((get_data_of_movie(movie))[2]))<8 :
         rank_list_bollys[f'rank_list_bolly_7.5-8'].append(get_data_of_movie(movie)[0])
    elif float(((get_data_of_movie(movie)))[2])>=8 and float(((get_data_of_movie(movie))[2]))<8.5 :
         rank_list_bollys[f'rank_list_bolly_8-8.5'].append(get_data_of_movie(movie)[0])
    elif float(((get_data_of_movie(movie)))[2])>=8.5 and float(((get_data_of_movie(movie))[2]))<9 :
         rank_list_bollys[f'rank_list_bolly_8.5-9'].append(get_data_of_movie(movie)[0])
    elif float(((get_data_of_movie(movie)))[2])>=9 and float(((get_data_of_movie(movie))[2]))<9.5 :
         rank_list_bollys[f'rank_list_bolly_9-9.5'].append(get_data_of_movie(movie)[0])
    elif float(((get_data_of_movie(movie)))[2])>=9.5 and float(((get_data_of_movie(movie))[2]))<10 :
         rank_list_bollys[f'rank_list_bolly_9.5-10'].append(get_data_of_movie(movie)[0])
# print(rank_list_bollys)  
for i in range(0,50):
    html_bolly =f"""<html lang=\"en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{(get_data_of_movie(movies_bolly[i]))[0]}</title>
    <link rel="stylesheet" href="style3.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

</head>
<body>
    <div class="container">
        <div class="movie-poster" >
            <img class ="poster-image" src ="{(get_data_of_movie(movies_bolly[i]))[6]}">
        </div>
        <div class="movie-info">
            <div class="movie-title">
                <h2><strong>{(get_data_of_movie(movies_bolly[i]))[0]} </strong>({(get_data_of_movie(movies_bolly[i]))[1]})<h2>
            </div>
            <div class="details">
                <h3><i class="fa-regular fa-star-half-stroke"></i>  <span>{(get_data_of_movie(movies_bolly[i]))[2]}</span> </h3>
                <h4><i class="fa-regular fa-clock"></i> <span>{(get_data_of_movie(movies_bolly[i]))[4]}</span></h4>
            </div>
            <div class="overview">
                <h3>Overview</h3>
                <p class="featured-desc">{(get_data_of_movie(movies_bolly[i]))[3]}</p>
            </div>
            <div class="genre">
                <strong>{(get_data_of_movie(movies_bolly[i]))[5]}</strong>
            </div>
            <div class="languages">
                <span>Languages Available</span>
                <ul>
                    <li>Hindi</li>
                    <li>Tamil</li>
                    <li>Telugu</li>
                    <li>Bengali</li>
                </ul>
                <div class="trailer">
                    <button class="featured-button"><a href="">WATCH TRAILER!</a></button>
                </div>
            </div>
            
        </body>
        </html>"""
    with open(f"{get_data_of_movie(movies_bolly[i])[0]}.html","w")as html_file_bolly:
      html_file_bolly.write(html_bolly)













from numpy import true_divide
import pandas as pd
import bs4
import webbrowser
import requests
from bs4 import BeautifulSoup
source_holly = requests.get("https://www.imdb.com/list/ls055592025/")
source_holly.raise_for_status()
soup_holly = BeautifulSoup(source_holly.content,'html.parser')
mova_holly = soup_holly.find('div',class_="pagecontent").find_all(class_="lister-item mode-detail")
movies_holly=[]
for i in range(0,50):
     movies_holly.append(mova_holly[i])
# print(len(movies_holly))
def get_data_of_movie(movie):
     name = movie.find("h3",class_="lister-item-header").a.text
     year = movie.find("span",class_="lister-item-year text-muted unbold").text.strip('()')
     rating =movie.find('span','ipl-rating-star__rating').text
     desc = movie.find('p',class_='').text
     runtime= movie.find('span',class_='runtime').text
     genre = movie.find('span',class_='genre').text
     img = movie.img.get('loadlate')
     return name,year,rating,desc,runtime,genre,img
# print((get_data_of_movie(mova_holly[0]))[7])
genre_list_holly=["Crime","Drama","Biography","History","Sport","Romance","Mystery","Family","Fantasy","Adventure"]
genre_list_hollys={}
for genre in genre_list_holly:
    genre_list_hollys[f'genre_list_holly_{genre}']=[]
    for movie in movies_holly:
      if ((get_data_of_movie(movie))[5]).find(f'{genre}')!=-1:
        genre_list_hollys[f'genre_list_holly_{genre}'].append(get_data_of_movie(movie)[0])
# print(genre_list_hollys)    
        
rank_list_holly=["7-7.5","7.5-8","8-8.5","8.5-9","9-9.5","9.5-10"]
rank_list_hollys={}
for rank in rank_list_holly:
    rank_list_hollys[f'rank_list_holly_{rank}']=[]
for movie in movies_holly:
    if float(((get_data_of_movie(movie)))[2])>=7 and float(((get_data_of_movie(movie))[2]))<7.5 :
         rank_list_hollys[f'rank_list_holly_7-7.5'].append(get_data_of_movie(movie)[0])
    elif float(((get_data_of_movie(movie)))[2])>=7.5 and float(((get_data_of_movie(movie))[2]))<8 :
         rank_list_hollys[f'rank_list_holly_7.5-8'].append(get_data_of_movie(movie)[0])
    elif float(((get_data_of_movie(movie)))[2])>=8 and float(((get_data_of_movie(movie))[2]))<8.5 :
         rank_list_hollys[f'rank_list_holly_8-8.5'].append(get_data_of_movie(movie)[0])
    elif float(((get_data_of_movie(movie)))[2])>=8.5 and float(((get_data_of_movie(movie))[2]))<9 :
         rank_list_hollys[f'rank_list_holly_8.5-9'].append(get_data_of_movie(movie)[0])
    elif float(((get_data_of_movie(movie)))[2])>=9 and float(((get_data_of_movie(movie))[2]))<9.5 :
         rank_list_hollys[f'rank_list_holly_9-9.5'].append(get_data_of_movie(movie)[0])
    elif float(((get_data_of_movie(movie)))[2])>=9.5 and float(((get_data_of_movie(movie))[2]))<10 :
         rank_list_hollys[f'rank_list_holly_9.5-10'].append(get_data_of_movie(movie)[0])
# print(rank_list_hollys)  
for i in range(0,50):
    html_holly =f"""<html lang=\"en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{(get_data_of_movie(movies_holly[i]))[0]}</title>
    <link rel="stylesheet" href="style3.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

</head>
<body>
    <div class="container">
        <div class="movie-poster" >
            <img class ="poster-image" src ="{(get_data_of_movie(movies_holly[i]))[6]}">
        </div>
        <div class="movie-info">
            <div class="movie-title">
                <h2><strong>{(get_data_of_movie(movies_holly[i]))[0]} </strong>({(get_data_of_movie(movies_holly[i]))[1]})<h2>
            </div>
            <div class="details">
                <h3><i class="fa-regular fa-star-half-stroke"></i>  <span>{(get_data_of_movie(movies_holly[i]))[2]}</span> </h3>
                <h4><i class="fa-regular fa-clock"></i> <span>{(get_data_of_movie(movies_holly[i]))[4]}</span></h4>
            </div>
            <div class="overview">
                <h3>Overview</h3>
                <p class="featured-desc">{(get_data_of_movie(movies_holly[i]))[3]}</p>
            </div>
            <div class="genre">
                <strong>{(get_data_of_movie(movies_holly[i]))[5]}</strong>
            </div>
            <div class="languages">
                <span>Languages Available</span>
                <ul>
                    <li>Hindi</li>
                    <li>Tamil</li>
                    <li>Telugu</li>
                    <li>Bengali</li>
                </ul>
                <div class="trailer">
                    <button class="featured-button"><a href="">WATCH TRAILER!</a></button>
                </div>
            </div>
            
        </body>
        </html>"""
    with open(f"{get_data_of_movie(movies_holly[i])[0]}.html","w")as html_file_holly:
      html_file_holly.write(html_holly)



















from numpy import true_divide
import pandas as pd
import bs4
import webbrowser
import requests
from bs4 import BeautifulSoup
source_series = requests.get("https://www.imdb.com/list/ls057886464/")
source_series.raise_for_status()
soup_series = BeautifulSoup(source_series.content,'html.parser')
mova_series = soup_series.find('div',class_="pagecontent").find_all(class_="lister-item mode-detail")
movies_series=[]
for i in range(0,50):
     movies_series.append(mova_series[i])
# print(len(movies_series))
def get_data_of_movie(movie):
     name = movie.find("h3",class_="lister-item-header").a.text
     year = movie.find("span",class_="lister-item-year text-muted unbold").text.strip('()')
     rating =movie.find('span','ipl-rating-star__rating').text
     desc = movie.find('p',class_='').text
     runtime= movie.find('span',class_='runtime').text
     genre = movie.find('span',class_='genre').text
     img = movie.img.get('loadlate')
    #  trailer = movie.a.get('href')
    #trailer=tai.a.get('href')
     return name,year,rating,desc,runtime,genre,img
genre_list_series=["Crime","Drama","Biography","History","Sport","Romance","Mystery","Family","Fantasy","Adventure"]
genre_list_seriess={}
for genre in genre_list_series:
    genre_list_seriess[f'genre_list_series_{genre}']=[]
    for movie in movies_series:
      if ((get_data_of_movie(movie))[5]).find(f'{genre}')!=-1:
        genre_list_seriess[f'genre_list_series_{genre}'].append(get_data_of_movie(movie)[0])
# print(genre_list_seriess)    


rank_list_series=["7-7.5","7.5-8","8-8.5","8.5-9","9-9.5","9.5-10"]
rank_list_seriess={}
for rank in rank_list_series:
    rank_list_seriess[f'rank_list_series_{rank}']=[]
for movie in movies_series:
    if float(((get_data_of_movie(movie)))[2])>=7 and float(((get_data_of_movie(movie))[2]))<7.5 :
         rank_list_seriess[f'rank_list_series_7-7.5'].append(get_data_of_movie(movie)[0])
    elif float(((get_data_of_movie(movie)))[2])>=7.5 and float(((get_data_of_movie(movie))[2]))<8 :
         rank_list_seriess[f'rank_list_series_7.5-8'].append(get_data_of_movie(movie)[0])
    elif float(((get_data_of_movie(movie)))[2])>=8 and float(((get_data_of_movie(movie))[2]))<8.5 :
         rank_list_seriess[f'rank_list_series_8-8.5'].append(get_data_of_movie(movie)[0])
    elif float(((get_data_of_movie(movie)))[2])>=8.5 and float(((get_data_of_movie(movie))[2]))<9 :
         rank_list_seriess[f'rank_list_series_8.5-9'].append(get_data_of_movie(movie)[0])
    elif float(((get_data_of_movie(movie)))[2])>=9 and float(((get_data_of_movie(movie))[2]))<9.5 :
         rank_list_seriess[f'rank_list_series_9-9.5'].append(get_data_of_movie(movie)[0])
    elif float(((get_data_of_movie(movie)))[2])>=9.5 and float(((get_data_of_movie(movie))[2]))<10 :
         rank_list_seriess[f'rank_list_series_9.5-10'].append(get_data_of_movie(movie)[0])
# print(rank_list_seriess)  
for i in range(0,50):
    html_series =f"""<html lang=\"en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{(get_data_of_movie(movies_series[i]))[0]}</title>
    <link rel="stylesheet" href="style3.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

</head>
<body>
    <div class="container">
        <div class="movie-poster" >
            <img class ="poster-image" src ="{(get_data_of_movie(movies_series[i]))[6]}">
        </div>
        <div class="movie-info">
            <div class="movie-title">
                <h2><strong>{(get_data_of_movie(movies_series[i]))[0]} </strong>({(get_data_of_movie(movies_series[i]))[1]})<h2>
            </div>
            <div class="details">
                <h3><i class="fa-regular fa-star-half-stroke"></i>  <span>{(get_data_of_movie(movies_series[i]))[2]}</span> </h3>
                <h4><i class="fa-regular fa-clock"></i> <span>{(get_data_of_movie(movies_series[i]))[4]}</span></h4>
            </div>
            <div class="overview">
                <h3>Overview</h3>
                <p class="featured-desc">{(get_data_of_movie(movies_series[i]))[3]}</p>
            </div>
            <div class="genre">
                <strong>{(get_data_of_movie(movies_series[i]))[5]}</strong>
            </div>
            <div class="languages">
                <span>Languages Available</span>
                <ul>
                    <li>Hindi</li>
                    <li>Tamil</li>
                    <li>Telugu</li>
                    <li>Bengali</li>
                </ul>
                <div class="trailer">
                    <button class="featured-button"><a href="">WATCH TRAILER!</a></button>
                </div>
            </div>
            
        </body>
        </html>"""
    with open(f"{get_data_of_movie(movies_series[i])[0]}.html","w")as html_file_series:
      html_file_series.write(html_series)



   








list_movies_bolly=[]
for i in range(0,50):
    list_movies_bolly.append(f""" <div class="movie-list-item">
                            <img class="movie-list-item-img" src="{(get_data_of_movie(movies_bolly[i]))[6]}" alt="">
                            <span class="movie-list-item-title">{(get_data_of_movie(movies_bolly[i]))[0]}</span>
                            <p class="movie-list-item-desc">{(get_data_of_movie(movies_bolly[i]))[3]}</p>
                            <button class="movie-list-item-button"><a href="{get_data_of_movie(movies_bolly[i])[0]}.html">VIEW</a></button>
                        </div>""")

# print(list_movies_bolly)
movie_container_bolly=""
for movie in list_movies_bolly:
     movie_container_bolly=movie_container_bolly+movie
# print(movie_container_bolly)


list_movies_holly=[]
for i in range(0,50):
    list_movies_holly.append(f""" <div class="movie-list-item">
                            <img class="movie-list-item-img" src="{(get_data_of_movie(movies_holly[i]))[6]}" alt="">
                            <span class="movie-list-item-title">{(get_data_of_movie(movies_holly[i]))[0]}</span>
                            <p class="movie-list-item-desc">{(get_data_of_movie(movies_holly[i]))[3]}</p>
                            <button class="movie-list-item-button"><a href="{get_data_of_movie(movies_holly[i])[0]}.html">VIEW</a></button>
                        </div>""")

# print(list_movies_holly)
movie_container_holly=""
for movie in list_movies_holly:
     movie_container_holly=movie_container_holly+movie
# print(movie_container_holly)



list_movies_series=[]
for i in range(0,50):
    list_movies_series.append(f""" <div class="movie-list-item">
                            <img class="movie-list-item-img" src="{(get_data_of_movie(movies_series[i]))[6]}" alt="">
                            <span class="movie-list-item-title">{(get_data_of_movie(movies_series[i]))[0]}</span>
                            <p class="movie-list-item-desc">{(get_data_of_movie(movies_series[i]))[3]}</p>
                            <button class="movie-list-item-button"><a href="{get_data_of_movie(movies_series[i])[0]}.html">VIEW</a></button>
                        </div>""")

# print(list_movies_series)
movie_container_series=""
for movie in list_movies_series:
     movie_container_series=movie_container_series+movie
# print(movie_container_series)


list_searchbar=[]
for i in range(0,50):
    list_searchbar.append(f"""
        <li class="searchlist-item"><a href="{get_data_of_movie(movies_bolly[i])[0]}.html">{(get_data_of_movie(movies_bolly[i]))[0]}</a></li>""" )
    
for i in range(0,50):
    list_searchbar.append(f"""
        <li class="searchlist-item"><a href="{get_data_of_movie(movies_holly[i])[0]}.html">{(get_data_of_movie(movies_holly[i]))[0]}</a></li>""" )
    
for i in range(0,50):
    list_searchbar.append(f"""
        <li class="searchlist-item"><a href="{get_data_of_movie(movies_series[i])[0]}.html">{(get_data_of_movie(movies_series[i]))[0]}</a></li>""" )

# print(list_searchbar)
list_searchbar_string=""
for movie in list_searchbar:
     list_searchbar_string=list_searchbar_string+movie
# print(list_searchbar_string)












data=f"""
<html lang="en" >
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="styles2.css">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,400;1,100;1,300;1,400;1,500&family=Sen:wght@400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <link rel="shortcut icon" href="img/profile.jpg" type="image/x-icon">
    <!-- <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"> -->
    <!-- <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"> -->
    <title>Movie Websitee</title>
</head>
<body>
    <div class="loader-wrapper">
        <span class="loader">WELCOME TO CINEFLY</span>
    </div>
    <div class="navbar">
        <div class="navbar-container">
            <div class="logo-container"><h1 class="logo"><strong>CINEFLY</strong></h1></div>
            <div class="menu-container">
                <div class="select">
                    <label for="question"><strong>Menu</strong></label>
                    <select name="question" id="question" placeholder="Select">
                        <option value="q1">Home</option>
                        <!-- <option value="q2">Movies</option> -->
                        <option value="q3"><button onclick="signIn()">Login</button></option>
                        <!-- <option value="q4">Popular</option> -->
                        <option value="q4"><button onclick= "func()" ><i class="left-menu-icon fa-solid fa-magnifying-glass"></i>search</button></option>
                        
                    </select>
                </div>
                <ul class="menu-list">
                    <li class="menu-list-item active">Home</li>
                    <!-- <li class="menu-list-item">Movies</li> -->
                    <li class="menu-list-item"><button onclick="signIn()">Login</button></li>
                    <!-- <li class="menu-list-item">Popular</li> -->
                    <li class="menu-list-item"><button onclick= "func()" ><i class="left-menu-icon fa-solid fa-magnifying-glass"></i></button></li>
                </ul>
                                <div class="dropdown">
                    <button class="btn btn-default dropdown-toggle" type="button" data-toggle="dropdown">Filters
                    <span class="caret"></span></button>
                    <ul class="dropdown-menu">

                        <li class="dropdown-submenu">
                            <a class="test" tabindex="-1" href="#">Genre<span class="caret"></span></a>
                            <ul class="dropdown-menu">
                                <li class="dropdown-submenu">
                                    <a class="test" href="#">Crime<span class="caret"></span></a>
                                    <ul class="dropdown-menu">
                                        <li><a href="moviepage.html">Movie 1</a></li>
                                        <li><a href="#">Movie 2</a></li>
                                    </ul>
                                </li>

                                <li class="dropdown-submenu">
                                    <a class="test" href="#">Thriller<span class="caret"></span></a>
                                    <ul class="dropdown-menu">
                                        <li><a href="#">Movie 1</a></li>
                                        <li><a href="#">Movie 2</a></li>
                                    </ul>
                                </li>

                                <li class="dropdown-submenu">
                                    <a class="test" href="#">Romance<span class="caret"></span></a>
                                    <ul class="dropdown-menu">
                                        <li><a href=" Casablanca.html"> Casablanca</a></li>
                                        <li><a href="Gone with the Wind.html">Gone with the Wind</a></li>
                                    </ul>
                                </li>

                                <li class="dropdown-submenu" class="dropdown-submenu">
                                    <a class="test" href="">Drama<span class="caret"></span></a>
                                    <ul class="dropdown-menu">
                                        <li><a href="The Godfather.html">The Godfather</a></li>
                                        <li><a href="The Shawshank Redemption.html">The Shawshank Redemption</a></li>
                                    </ul>
                                </li>
                            </ul>
                        </li>    
                        <li class="dropdown-submenu">
                            <a class="test" tabindex="-1" href="#">Rating<span class="caret"></span></a>
                            <ul class="dropdown-menu">
                                <li class="dropdown-submenu">
                                    <a class="test" href="#">>4.5<span class="caret"></span></a>
                                    <ul class="dropdown-menu">
                                        <li><a href="#">Movie 1</a></li>
                                        <li><a href="#">Movie 2</a></li>
                                    </ul>

                                </li>
                                <li class="dropdown-submenu">
                                    <a class="test" href="#">4-4.5<span class="caret"></span></a>
                                    <ul class="dropdown-menu">
                                        <li><a href="#">Movie 1</a></li>
                                        <li><a href="#">Movie 2</a></li>
                                    </ul>

                                </li>

                                <li class="dropdown-submenu">
                                    <a class="test" href="#">3.5-4<span class="caret"></span></a>
                                    <ul class="dropdown-menu">
                                        <li><a href="#">Movie 1</a></li>
                                        <li><a href="#">Movie 2</a></li>
                                    </ul>

                                </li>

                                <li class="dropdown-submenu">
                                    <a class="test" href="#">3-3.5<span class="caret"></span></a>
                                    <ul class="dropdown-menu">
                                        <li><a href="#">Movie 1</a></li>
                                        <li><a href="#">Movie 2</a></li>
                                    </ul>
                                </li>
                            </ul>
                        </li>    
                        
                    </ul>
                </div>
            <div class="profile-container">
                <img class="profile-picture" src="img/profile.jpg" alt=""></img>
                <div class="profile-text-container">
                    <span class="profile-text">Profile</span>
                    <i class="fa-solid fa-sort-down"></i>
                </div>
                <div class="toggle">
                    <i class="fa-solid fa-moon toggle-icon"></i>
                    <i class="fa-regular fa-sun toggle-icon"></i>
                    <div class="toggle-ball"></div>
                </div>
            </div>
        </div>
    </div>
    <!-- <div class="sidebar">
        <button onclick= "func()" ><i class="left-menu-icon fa-solid fa-magnifying-glass"></i></button>
        <i class="left-menu-icon fa-solid fa-house-user"></i>
        <i class="left-menu-icon fa-solid fa-user-large"></i>
        <i class="left-menu-icon fa-solid fa-bookmark"></i>
        <i class="left-menu-icon fa-solid fa-tv"></i>
        <i class="left-menu-icon fa-solid fa-hourglass-half"></i> -->
        <!-- <i class="left-menu-icon fa-solid fa-cart-shopping"></i> -->
    <!-- </div> -->
    <div class="container">
        <div class="searchBox" id="searchBox">
            <div class="row">
                <input type="text" id="input-box" placeholder="Search here..." autocomplete="off">
                <!-- <button> <i class="left-menu-icon fa-solid fa-magnifying-glass"></i></button> -->
                
            </div>
            <div class="result-box">
                <ul>
                   {list_searchbar_string}
                </ul>
            </div>
            
            
        </div>
        <div class="content-container">
            <div class="featured-content" style="background:linear-gradient(to bottom,rgba(0,0,0,0) ,rgb(16,29,45)), url('img/f-2.jpg');">
                <img class="featured-title" src="img/f-t-1.png" alt="">
                <p class="featured-desc">Development of Django Unchained began in 2007 when Tarantino was writing a book on Corbucci. By April 2011, Tarantino sent his final draft of the script to The Weinstein Company (TWC).</p>
                    <button class="featured-button">WATCH TRAILER!</button>
            </div>
            <div class="movie-list-container">
                <h1 class="movie-list-title">BOLLYWOOD</h1>
                <div class="movie-list-wrapper">
                    <div class="movie-list">{movie_container_bolly}
                    </div>
                    <i class="fa-solid fa-caret-right arrow"></i>
                </div>
            <div class="featured-content" style="background:linear-gradient(to bottom,rgba(0,0,0,0),#090765),url('img/f-2.jpg');">
                <img class="featured-title" src="img/f-t-1.png" alt="">
                <p class="featured-desc">Development of Django Unchained began in 2007 when Tarantino was writing a book on Corbucci. By April 2011, Tarantino sent his final draft of the script to The Weinstein Company (TWC).</p>
                    <button class="featured-button">...!</button>
            </div>
            <div class="movie-list-container">
                <h1 class="movie-list-title">HOLLYWOOD</h1>
                <div class="movie-list-wrapper">
                    <div class="movie-list">{movie_container_holly}
                </div>
                    <i class="fa-solid fa-caret-right arrow"></i>
                </div>
                
            <div class="featured-content" style="background:linear-gradient(to bottom,rgba(0,0,0,0),#090765),url('img/f-2.jpg');">
                <img class="featured-title" src="img/f-t-1.png" alt="">
                <p class="featured-desc">Development of Django Unchained began in 2007 when Tarantino was writing a book on Corbucci. By April 2011, Tarantino sent his final draft of the script to The Weinstein Company (TWC).</p>
                    <button class="featured-button">...!</button>
            </div>
            <div class="movie-list-container">
                <h1 class="movie-list-title">SERIES</h1>
                <div class="movie-list-wrapper">
                    <div class="movie-list">{movie_container_series}
            </div>
                    <i class="fa-solid fa-caret-right arrow"></i>
                </div>
            </div>    
        </div>
    </div>
    <script src="app2.js"></script>
</body>
</html>

          

"""
with open('project.html','w') as web_file:
     web_file.write(data)