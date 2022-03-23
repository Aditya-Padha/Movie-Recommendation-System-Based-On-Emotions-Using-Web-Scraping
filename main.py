from bs4 import BeautifulSoup
import requests
#import itertools
import pandas as pd

movies = []
ratings = []
def createmovielist(url):
    movies = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    scraped_movie = soup.find_all('h3', class_='lister-item-header')
    for movie in scraped_movie:
        movie = movie.get_text().replace('\n', '')
        movie = movie.strip(" ")
        movies.append(movie)
    return movies


def createratinglist(url):
    ratings = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    scraped_ratings = soup.find_all('div', class_='inline-block ratings-imdb-rating')
    for rating in scraped_ratings:
        rating = rating.get_text().replace("\n", "")
        ratings.append(rating)
    return ratings


print("ENTER THE EMOTION WHOSE MOVIES YOU WANT TO SEE:")
print("FOR SAD GENRE, enter sad")
print("for DISGUST genre,enter disgust")
print("for ANTICIPATION genre,enter anticipation")
print("for FEAR genre,enter fear")
print("for ENJOYMENT genre,enter enjoyment")
print("for TRUST genre,enter trust")
print("for SURPRISE genre,enter surprise")
i = input("ENTER YOUR CHOICE:")
if i == "sad":
    url = "https://www.imdb.com/search/title/?genres=drama&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=N19H01AYVVZ6XCMZJCAZ&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_8"
    movies = createmovielist(url)
    ratings = createratinglist(url)
    data = list(zip(movies, ratings))
    df = pd.DataFrame(data, columns=['MOVIES', 'RATINGS'])
    print(df)

    #for (x, y) in zip(movies, ratings):
    #    print(f"{x} :{y}")
elif i == "disgust":
    url = "https://www.imdb.com/search/title/?genres=horror&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=N19H01AYVVZ6XCMZJCAZ&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_3"
    movies = createmovielist(url)
    ratings = createratinglist(url)
    for (x, y) in zip(movies, ratings):
        print(f"{x} :{y}")
elif i == "anger":
    url = "https://www.imdb.com/search/title/?genres=action&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=N19H01AYVVZ6XCMZJCAZ&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_1"
    movies = createmovielist(url)
    ratings = createratinglist(url)
    for (x, y) in zip(movies, ratings):
        print(f"{x} :{y}")
elif i == "anticipation":
    url = "https://www.imdb.com/search/title/?genres=thriller&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=N19H01AYVVZ6XCMZJCAZ&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_22"
    movies = createmovielist(url)
    ratings = createratinglist(url)
    for (x, y) in zip(movies, ratings):
        print(f"{x} :{y}")
elif i == "fear":
    url = "https://www.imdb.com/search/title/?genres=horror&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=N19H01AYVVZ6XCMZJCAZ&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_3"
    movies = createmovielist(url)
    ratings = createratinglist(url)
    for (x, y) in zip(movies, ratings):
        print(f"{x} :{y}")
elif i == "enjoyment":
    url = "https://www.imdb.com/search/title/?genres=adventure&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=N19H01AYVVZ6XCMZJCAZ&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_2"
    movies = createmovielist(url)
    ratings = createratinglist(url)
    for (x, y) in zip(movies, ratings):
        print(f"{x} :{y}")
elif i == "trust":
    url = "https://www.imdb.com/search/title/?genres=romance&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=N19H01AYVVZ6XCMZJCAZ&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_17"
    movies = createmovielist(url)
    ratings = createratinglist(url)
    for (x, y) in zip(movies, ratings):
        print(f"{x} :{y}")
elif i == "surprise":
    url = "https://www.imdb.com/search/title/?genres=fantasy&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=N19H01AYVVZ6XCMZJCAZ&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_10"
    movies = createmovielist(url)
    ratings = createratinglist(url)
    for (x, y) in zip(movies, ratings):
        print(f"{x} :{y}")
