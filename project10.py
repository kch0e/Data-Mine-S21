#1
import numpy as np
import pandas as pd
beers = pd.read_parquet("/class/datamine/data/beer/beers.parquet")
breweries = pd.read_parquet("/class/datamine/data/beer/breweries.parquet")
reviews = pd.read_parquet("/class/datamine/data/beer/reviews.parquet")
def prepare_data(myDF, min_num_reviews: int):
  myDF = myDF.loc[myDF.loc[:, "score"].notna(), :]
  myDF = myDF.loc[myDF.loc[:, "username"].notna(), :]
  myDF = myDF.loc[myDF.loc[:, "beer_id"].notna(), :]
  myDF.reset_index(drop=True)
  goodbeers = myDF.loc[:, "beer_id"].value_counts() >= min_num_reviews
  goodbeers = goodbeers.loc[goodbeers].index.values.tolist()
  goodusers = myDF.loc[:, "username"].value_counts() >= min_num_reviews
  goodusers = goodusers.loc[goodusers].index.values.tolist()
  myreturnDF = myDF.loc[myDF.loc[:, "username"].isin(goodusers)&myDF.loc[:, "beer_id"].isin(goodbeers), :]
  return myreturnDF
train = prepare_data(reviews, 1000)

def normalize(data):
    data['mean_score'] = data['score'].mean()
    data['std_score'] = data['score'].std()
    data['normalized'] = (data['score'] - data['mean_score'])/data['std_score']
    return data

train= train.groupby(["username"]).apply(normalize)
score_matrix = train.pivot(index='username',columns='beer_id',values='normalized')
myresults=score_matrix.mean(axis=0)
score_matrix=score_matrix.fillna(value=myresults)

from sklearn.metrics.pairwise import cosine_similarity
cosine_similarity_matrix=cosine_similarity(score_matrix)
np.fill_diagonal(cosine_similarity_matrix,0)
cosine_similarity_matrix= pd.DataFrame(cosine_similarity_matrix)
cosine_similarity_matrix.index = score_matrix.index
cosine_similarity_matrix.columns = score_matrix.index
cosine_similarity_matrix[0:4]
cosine_similarity_matrix[1820:]

#2.
def get_knn (cosine_similarity_matrix,user,k):
  return cosine_similarity_matrix[user].sort_values(ascending=False)[0:k].index.tolist()

k_similar=get_knn(cosine_similarity_matrix,"2GOOFY",4)
print(k_similar) # ['Phil-Fresh', 'mishi_d', 'SlightlyGrey', 'MI_beerdrinker']

#3.

import matplotlib.pyplot as plt
aux = pd.DataFrame()
neighbor = get_knn(cosine_similarity_matrix, "2GOOFY", 4)[0]
aux = reviews.loc[((reviews['username'] == "2GOOFY") | (reviews['username'] == neighbor)), :] aux = aux.pivot(index = 'beer_id', columns = 'username', values = 'score')
aux = aux.dropna(how = "any")
aux.sort_values(by = "2GOOFY")
plt.scatter(aux["2GOOFY"], aux["Phil-Fresh"])
plt.plot(np.arange(0, 6), np.arange(0, 6), color = "red")
plt.show()
plt.close()

#4
def recommend_beers(train: pd.DataFrame, username: str, cosine_similarity_matrix: pd.DataFrame, k: int):
  neighbors = get_knn(cosine_similarity_matrix, username, k)
  aux = pd.DataFrame()
  aux = train.loc[train.loc[:, "username"].isin(neighbors), :]
  temp = train.loc[train.loc[:, "username"] == username, "beer_id"]
  temp = train.loc[-aux.loc[:, "beer_id"].isin(temp), :]
  aux = aux.loc[:, ("beer_id", "standardized_score")].groupby(["beer_id"]).mean()
  aux.sort_values(by = "standardized_score", ascending = False, inplace = True)
  return aux[0:5].index.tolist()

recommend_beers(train, "22Blue", cosine_similarity_matrix, 30) # [40057, 69522, 22172, 59672, 86487]
