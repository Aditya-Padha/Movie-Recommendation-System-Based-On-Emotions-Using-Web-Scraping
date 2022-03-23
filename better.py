# Importing the Libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Asking the User to Enter The Emotion
print("ENTER THE EMOTION WHOSE MOVIES YOU WANT TO SEE:")
print("FOR SAD GENRE, Enter sad")
print("for DISGUST genre, Enter disgust")
print("for ANTICIPATION genre, Enter anticipation")                                    # Mini-Project By: ADITYA PADHA
print("for FEAR genre, Enter fear")
print("for ENJOYMENT genre, Enter enjoyment")
print("for TRUST genre, Enter trust")
print("for SURPRISE genre, Enter surprise")
i = input("ENTER YOUR CHOICE: ")

# User Input Determines Which Case is chosen
url = ""
if i == "sad":
    url = "https://www.imdb.com/search/title/?genres=drama&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL" \
          "&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=N19H01AYVVZ6XCMZJCAZ&pf_rd_s=center-6&pf_rd_t=15051" \
          "&pf_rd_i=genre&ref_=ft_gnr_mvpop_8 "

elif i == "disgust":
    url = "https://www.imdb.com/search/title/?genres=horror&explore=title_type," \
          "genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=N19H01AYVVZ6XCMZJCAZ" \
          "&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_3 "

elif i == "anger":
    url = "https://www.imdb.com/search/title/?genres=action&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL" \
          "&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=N19H01AYVVZ6XCMZJCAZ&pf_rd_s=center-6&pf_rd_t=15051" \
          "&pf_rd_i=genre&ref_=ft_gnr_mvpop_1 "

elif i == "anticipation":
    url = "https://www.imdb.com/search/title/?genres=thriller&title_type=feature&explore=genres&pf_rd_m" \
          "=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=N19H01AYVVZ6XCMZJCAZ&pf_rd_s=center-6" \
          "&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_22 "

elif i == "fear":
    url = "https://www.imdb.com/search/title/?genres=horror&explore=title_type," \
          "genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=N19H01AYVVZ6XCMZJCAZ" \
          "&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_3 "

elif i == "enjoyment":
    url = "https://www.imdb.com/search/title/?genres=adventure&title_type=feature&explore=genres&pf_rd_m" \
          "=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=N19H01AYVVZ6XCMZJCAZ&pf_rd_s=center-6" \
          "&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_2 "

elif i == "trust":
    url = "https://www.imdb.com/search/title/?genres=romance&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL" \
          "&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=N19H01AYVVZ6XCMZJCAZ&pf_rd_s=center-6&pf_rd_t=15051" \
          "&pf_rd_i=genre&ref_=ft_gnr_mvpop_17 "

elif i == "surprise":
    url = "https://www.imdb.com/search/title/?genres=fantasy&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL" \
          "&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=N19H01AYVVZ6XCMZJCAZ&pf_rd_s=center-6&pf_rd_t=15051" \
          "&pf_rd_i=genre&ref_=ft_gnr_mvpop_10 "


# After the Conditions, The HTMl content from the selected URL is Sent Back to Us.
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
# Declaring The Lists that Will Store Data
movie_name = []
year = []
time = []
rating = []
# Using The Beautiful Soup Library To Parse Through The HTML Content To Find What We Are Looking For.
movie_data = soup.find_all('div', attrs={'class': 'lister-item mode-advanced'})
for store in movie_data:
    name = store.h3.a.text
    movie_name.append(name)

    year_of_release = store.h3.find('span', class_='lister-item-year text-muted unbold').text.replace('(', '').replace(')', '').replace(' ','').replace('I','')
    year.append(year_of_release)

    runtime = store.p.find('span', class_='runtime').text.replace(' min', '') if store.find('span', class_='runtime') else 'N/A'
    time.append(runtime)

    rate = store.find('div', class_='inline-block ratings-imdb-rating').text.replace('\n', '') if store.find('div', class_='inline-block ratings-imdb-rating') else 'N/A'
    rating.append(rate)
#The Collected Data Is Framed In An Organised Manner Using The Pandas Library
movie_df = pd.DataFrame({'Name: ': movie_name, 'Year of release': year, 'Watch-time: ': time, 'Rating: ': rating})
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
movie_df.index += 1
print(movie_df)
