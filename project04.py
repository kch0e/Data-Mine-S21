#Q1
import pandas as pd
import csv
myDF = pd.read_csv("/class/datamine/data/craigslist/vehicles.csv")
myDF.head()
myDF.shape

#myDF = pd.DataFrame(columns = ['LAT', 'LONG', 'STATE'])

#pair = list(myDF.loc[:'LAT', 'LONG']].dropna().to_records(index=False))
stateDict = {}
for my_index, my_row in myDF.iterrows():
    stateDict[my_row["state"]] = []
for my_index, my_row in myDF.iterrows():
    stateDict[my_row["state"]].append( (my_row['lat'],my_row['long'])) 
print(stateDict.get("in")[0:2])

#2
for mystate, value in stateDict.items():
  print(f'{mystate}:')
  for myindex, mytriple in enumerate(value):
    if (myindex % 5000 == 0):
      print(f'Lat: {mytriple[0]} Long: {mytriple[1]}')

#3
from collections import defaultdict
import matplotlib.pyplot as plt

my_list = list(myDF.loc[:, ["year", "price",]].dropna().to_records(index=False))

dictionary = defaultdict(list)

for year, price in my_list:
    dictionary[year].append(float(price))

listyear = []
listprice = []

import statistics
for year, price in sorted(dictionary.items()):
  listyear.append(year)
  bob = statistics.median(dictionary[year])
  listprice.append(bob)
  print(f'Year {year} Price {bob}')


plt.bar(listyear, listprice)
plt.show()
plt.close()

#4

dictionary = defaultdict(list)

for year, price in my_list:
  if (price) < 200000:
    dictionary[year].append(price)

listyear = []
listprice = []

import statistics
for year, price in sorted(dictionary.items()):
  listyear.append(year)
  bob = statistics.mean(dictionary[year])
  listprice.append(bob)
  print(f'Year {year} Price {bob}')


plt.bar(listyear, listprice)
plt.show()
plt.close()

#5
import statistics

my_list = list(myDF.loc[:, ["state", "price"]].dropna().to_records(index=False))
myIndianaprices = [price for (state, price) in my_list if state.upper() == "IN"]
statistics.mean(myIndianaprices)

myMidwestprices = [price for (state, price) in my_list if state.upper() == "IN" or state.upper() == "MI" or state.upper() == "IL"]
statistics.mean(myMidwestprices)

my_list = list(myDF.loc[:, ["manufacturer", "year", "price",]].dropna().to_records(index=False))
mycarprices = [price for (manufacturer, year, price) in my_list if manufacturer == "honda" and year >= 2010]
statistics.mean(mycarprices)

#6
import spacy

# get list of descriptions
my_list = list(myDF.loc[:, ["description",]].dropna().to_records(index=False))
my_list = [m[0] for m in my_list]

# load the pre-built spacy model
nlp = spacy.load("en_core_web_lg")

# apply the model to a description
doc = nlp(my_list[0])

for doc in my_list[:10]:
    d = nlp(doc)
    for entity in d.ents:
        print(entity.text.encode('ascii', errors='ignore'), entity.label_)

for doc in my_list[:10]:
    d = nlp(doc)
    for entity in d.ents:
        if entity.label_ == "CARDINAL":
            print(entity.text.encode('ascii', errors='ignore'), entity.label_)

for doc in my_list[:10]:
    d = nlp(doc)
    for entity in d.ents:
        if entity.label_ == "CARDINAL" and len(entity.text) in [7, 8, 10, 11, 12, 14]:
            print(entity.text.encode('ascii', errors='ignore'), entity.label_)

import re
pattern = '\(?([0-9]{3})?\)?[-.]?([0-9]{3})[-.]?([0-9]{4})'
for doc in my_list[:10]:
    if matches := re.finditer(pattern, doc):
        for match in matches:
            print(match.group())
#It filters through all the data and keeping instances that match the pattern in line 119. The output includes phone numbers that match the pattern.
