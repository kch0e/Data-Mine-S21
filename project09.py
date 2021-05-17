#1
import pandas as pd
beers = pd.read_parquet("/class/datamine/data/beer/beers.parquet")
breweries = pd.read_parquet("/class/datamine/data/beer/breweries.parquet")
reviews = pd.read_parquet("/class/datamine/data/beer/reviews.parquet")
def prepare_data(myDF, min_num_donations):
  myDF = myDF.loc[myDF.loc[:, "score"].notna(), :]
  myDF = myDF.loc[myDF.loc[:, "username"].notna(), :]
  myDF = myDF.loc[myDF.loc[:, "beer_id"].notna(), :]
  myDF = myDF.reset_index(drop=True)
  
  goodusernames = myDF.loc[:, "username"].value_counts() >= min_num_donations
  goodusernames = goodusernames.loc[goodusernames].index.values.tolist()
  
  goodid = myDF.loc[:, "beer_id"].value_counts() >= min_num_donations
  goodid = goodid.loc[goodid].index.values.tolist()
  
  myDF = myDF.loc[myDF.loc[:, "username"].isin(goodusernames) & myDF.loc[:, "beer_id"].isin(goodid), :]
  return myDF

train = prepare_data(reviews, 1000)
print(train.shape) # (952105, 10)

#2

def summer(data):
  data['standardized_score'] = ((data['score'] - data['score'].mean())/data['score'].std())
  return data
  
myresults = train.groupby(["username"]).apply(summer)
print(myresults)

#3
score_matrix = pd.DataFrame()
score_matrix = pd.pivot_table(train,index = 'beer_id', columns = 'username', values = 'standardized_score')

score_matrix.head()

type(score_matrix)
score_matrix.shape

#4
myresults = score_matrix.mean(axis=0)
score_matrix.fillna(value=myresults)


