#1
import pandas as pd

photos = pd.read_parquet("/class/datamine/data/yelp/data/parquet/businesses_sample.parquet")
photos.head()
pd.set_option('display columns', None)
myDF[0:5]

#The names of the datasets are businesses, checkins, reviews, users, businesses_sample, photos, and tips.

#The businesses includes the busseiness id and hours.
#The checkins includes the business id and the date.
#The review includes the review id and the date.
#The users includes the user id, name, compliment writer, and compliment photos.
#The businesses sample includesthe business id and hours.
#The photos include the photoid and label.
#The tips includes the userid and compliment count.

#2

business = pd.read_parquet("/class/datamine/data/yelp/data/parquet/businesses.parquet")
len(business.loc[:, "attributes"].iloc[0].keys()) # 39
len(business.loc[:, "hours"].iloc[0].keys())
def has_attributes(business_id_number):
  returnval = False
  
  for i in range (0, business.shape[0]):
    if (business["business_id"][i] == business_id_number):
      
      if(business["attributes"][i] != None):
        returnval = True
  return returnval

print(has_attributes('f9NumwFMBDn751xgFiRbNA')) # True
print(has_attributes('XNoUzKckATkOD1hP6vghZg')) # False
print(has_attributes('Yzvjg0SayhoZgCljUJRF9Q')) # True
print(has_attributes('7uYJJpwORUbCirC1mz8n9Q')) # False

#3

businesses.loc[0:5, "hours"].apply(pd.series)
businesses.loc[0:5, "attributes"].apply(pd.series)

from pathlib import Path

def fix_businesses_data(data_path: str, output_dir: str) -> None:
    """
    fix_data accepts a parquet file that contains data in a specific format. 
    fix_data "explodes" the attributes and hours columns into 39+7=46 new 
    columns.
    Args:
        data_path (str): Full path to a file in the same format as businesses.parquet.
        output_dir (str): Path to a directory where new_businesses.parquet should be output.
    """
    # read in original parquet file
    businesses = pd.read_parquet(data_path)
  
    # unnest the attributes column
    businesses = pd.concat([business.drop(columns=['attributes']), businesses.loc[:, 'attributes'].apply(pd.Series)], axis=1)

    # unnest the hours column
    businesses = pd.concat([business.drop(columns=['hours']), businesses.loc[:, 'hours'].apply(pd.Series)], axis=1)

    # output new file
    businesses.to_parquet(str(Path(f"{output_dir}").joinpath("new_businesses.parquet")))
    
    return None
    
print(business["attributes"])
print(business["hours"])

attributesDF = business.loc[ : , "attributes"].apply(pd.Series)
hoursDF = business.loc[ : , "hours"].apply(pd.Series)
attributesDF.shape
hoursDF.shape
myDF = pd.concat([attributesDF,hoursDF], axis=1)
myDF.shape

p = Path(f"/scratch/scholar/choe29").glob('**/*')
files = [x for x in p if x.is_file()]
print(files)


#4

def unnest(inputDF: pd.DataFrame, columns: list) -> pd.DataFrame:
  #inputDF = pd.DataFrame()
  for mycolumn in columns:
    tempDF = inputDF.loc[ : , mycolumn].apply(pd.Series)
    inputDF = pd.concat([inputDF,tempDF], axis=1)
  return inputDF

businesses = pd.read_parquet("/class/datamine/data/yelp/data/parquet/businesses.parquet")

new_businesses_df = unnest(businesses, ["attributes", ])
new_businesses_df.shape # (209393, 39)
new_businesses_df.head()

new_businesses_df = unnest(businesses, ["attributes", "hours"])
new_businesses_df.shape # (209393, 46)
new_businesses_df.head()

#5
def unnest(inputDF: pd.DataFrame, columns: list) -> pd.DataFrame:
  myDF = pd.DataFrame()
  for mycolumn in columns:
    if mycolumn in inputDF.columns:
      mysum = 0
      for i in range(0,inputDF.shape[0]):
        if isinstance(inputDF[mycolumn][i],dict):
          mysum += 1
      if mysum > 0:
  
        tempDF = inputDF.loc[ : , mycolumn].apply(pd.Series)
        myDF = pd.concat([myDF,tempDF], axis=1)
  return myDF

businesses = pd.read_parquet("/class/datamine/data/yelp/data/parquet/businesses.parquet")


businesses['attributes'][2]
isinstance(business['attributes'][2],dict)

businesses = pd.read_parquet("/class/datamine/data/yelp/data/parquet/businesses.parquet")
results = unnest(businesses, ["doesntexist", "postal_code", "attributes"])
results.shape # (209393, 39)
results.head()
