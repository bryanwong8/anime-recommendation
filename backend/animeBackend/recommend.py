import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ratingDf = pd.read_csv('../datasets/rating.csv')
animeDf = pd.read_csv('../datasets/anime.csv')

df = pd.merge(ratingDf, animeDf.drop('rating', axis=1), on='anime_id')
df.groupby('name')['rating'].count().sort_values(ascending=False).head(10)

ratings = pd.DataFrame(df.groupby('name')['rating'].mean())
ratings['num of ratings'] = pd.DataFrame(df.groupby('name')['rating'].count())

genre_dict = pd.DataFrame(data=animeDf[['name', 'genre']])
genre_dict.set_index('name', inplace=True)


def check_genre(genre_list, string):
    if any(x in string for x in genre_list):
        return True
    else:
        return False


def get_recommendation(name):
    # generating list of anime with the same genre with target
    anime_genre = genre_dict.loc[name].values[0].split(', ')
    cols = animeDf[animeDf['genre'].apply(
        lambda x: check_genre(anime_genre, str(x)))]['name'].tolist()

    # create matrix based on generated list
    animemat = df[df['name'].isin(cols)].pivot_table(
        index='user_id', columns='name', values='rating')

    # create correlation table
    anime_user_rating = animemat[name]
    similiar_anime = animemat.corrwith(anime_user_rating)
    corr_anime = pd.DataFrame(similiar_anime, columns=['correlation'])
    corr_anime = corr_anime.join(ratings['num of ratings'])
    corr_anime.dropna(inplace=True)
    corr_anime = corr_anime[corr_anime['num of ratings'] > 5000].sort_values(
        'correlation', ascending=False)

    return corr_anime.head(10)
