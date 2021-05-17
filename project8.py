#1
import pandas as pd
users = pd.read_parquet("/class/datamine/data/yelp/data/parquet/users.parquet")
reviews = pd.read_parquet("/class/datamine/data/yelp/data/parquet/reviews.parquet")
def get_friends_data(user_id: str) -> pd.DataFrame:
  """
  hbbhjbhbjbh
  """
  myDF = pd.DataFrame()
  for i in range(0, users.shape[0]):
    if (users['user_id'][i] == user_id):
      mylist = users['friends'][i].split(", ")
  for j in range(0, users.shape[0]):
    if (users['user_id'][j] in mylist):
      myDF = myDF.append(users.iloc[j])
  return myDF
  
print(get_friends_data("ntlvfPzc8eglqvk92iDIAw").shape) # (13,22)
print(get_friends_data("AY-laIws3S7YXNl_f_D6rQ").shape) # (1, 22)
print(get_friends_data("xvu8G900tezTzbbfqmTKvA").shape) # (193,22)

#2

def calculate_avg_business_stars(business_id : str) -> float:
  temp = reviews[reviews["business_id"] == business_id]
  return sum(temp["stars"]) / len(temp["stars"])
  

print(calculate_avg_business_stars("f9NumwFMBDn751xgFiRbNA")) # 3.1025641025641026


#3
import matplotlib.pyplot as plt

def visualize_stars_over_time(my_business_id: str):
  
  myyears = []
  for i in range(0,reviews.shape[0]):
    myyears.append(reviews['date'][i].year)
  reviews['year'] = myyears
  averagestars = reviews.groupby(['business_id','year'],as_index=False)['stars'].mean()
  mydict = {}
  for i in range(0,averagestars.shape[0]):
    if averagestars['business_id'][i] == my_business_id:
      mydict[averagestars['year'][i]] = averagestars['stars'][i]
  print (mydict.keys())
  print (mydict.values())
  plt.plot(mydict.keys(), mydict.values())
  
  plt.show()
  plt.close()
  return None
    
visualize_stars_over_time('RESDUcs7fIiihp38-d6_6g')

#4

def visualize_stars_over_time(my_business_id: str, granularity: str = "years"):
  
  myyearsormonths = []
  if granularity == "months":
    for i in range(0,reviews.shape[0]):
      myyearsormonths.append(reviews['date'][i].month)
  else:
    for i in range(0, reviews.shape[0]):
      myyearsormonths.append(reviews['date'][i].year)
  reviews['yearormonth'] = myyearsormonths
  averagestars = reviews.groupby(['business_id','yearormonth'],as_index=False)['stars'].mean()
  mydict = {}
  for i in range(0,averagestars.shape[0]):
    if averagestars['business_id'][i] == my_business_id:
      mydict[averagestars['yearormonth'][i]] = averagestars['stars'][i]
  plt.plot(mydict.keys(), mydict.values())
  
  plt.show()
  plt.close()
    
visualize_stars_over_time('RESDUcs7fIiihp38-d6_6g', "months")

#5

def visualize_stars_over_time(*args, **kwargs):
  
  granularity = ""
  businesses = []
  if (len(kwargs) > 0):
    granularity = kwargs["granularity"]
    businesses = args
  else:
    granularity = args[len(args)-1]
    businesses = args[0:len(args)-1]
  for my_business_id in businesses:
    myyearsormonths = []
    if granularity == "months":
      for i in range(0,reviews.shape[0]):
        myyearsormonths.append(reviews['date'][i].month)
    else:
      for i in range(0, reviews.shape[0]):
        myyearsormonths.append(reviews['date'][i].year)
    reviews['yearormonth'] = myyearsormonths
    averagestars = reviews.groupby(['business_id','yearormonth'],as_index=False)['stars'].mean()
    mydict = {}
    for i in range(0,averagestars.shape[0]):
      if averagestars['business_id'][i] == my_business_id:
        mydict[averagestars['yearormonth'][i]] = averagestars['stars'][i]
    plt.plot(mydict.keys(), mydict.values())
  
    plt.show()
    plt.close()
    
visualize_stars_over_time("RESDUcs7fIiihp38-d6_6g", "4JNXUYY8wbaaDmk3BPzlWw", "K7lWdNUhCbcnEvI0NhGewg", "months")
visualize_stars_over_time("RESDUcs7fIiihp38-d6_6g", "4JNXUYY8wbaaDmk3BPzlWw", "K7lWdNUhCbcnEvI0NhGewg", "months")
visualize_stars_over_time("RESDUcs7fIiihp38-d6_6g", "4JNXUYY8wbaaDmk3BPzlWw", "K7lWdNUhCbcnEvI0NhGewg", granularity="years")

#6
our_businesses = ["RESDUcs7fIiihp38-d6_6g", "4JNXUYY8wbaaDmk3BPzlWw", "K7lWdNUhCbcnEvI0NhGewg"]

visualize_stars_over_time(*our_businesses, granularity="years")
