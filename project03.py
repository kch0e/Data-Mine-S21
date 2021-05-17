#Q1
import pandas as pd
myDF = pd.read_csv("/class/datamine/data/craigslist/vehicles.csv")
myDF.head()

#Q2
myyears = myDF['year'].dropna().to_list()

# get a list containing each unique year
unique_years = list(set(myyears))

# for each year (key), initialize the value (value) to 0
my_dict = {}
for year in unique_years:
    my_dict[year] = 0
for year in myyears:
    my_dict[year] = my_dict[year] + 1
print(my_dict)

#Q3
import matplotlib.pyplot as plt

my_dict.keys()
my_dict.values()
plt.bar(my_dict.keys(), my_dict.values())
plt.show()
plt.close()
# An example of a key would be 1912 has a value of 5.
print(my_dict[1912])

#Q4
listA = [1, 2, 3, 4, 5, 6, 12, 12]
listB = [2, 1, 7, 7, 7, 2, 8, 9, 10, 11, 12, 13]

# 1. values in list A but not list B
# values in list A but not list B
print(set(listA) - set(listB))

# 2. values in listB but not list A
print(set(listB) - set(listA))

# 3. values in both lists
# values in both lists
print(set.intersection(set(listA),set(listB)))

#Q5
states_list = list(myDF.loc[:, ["state", "lat", "long"]].dropna().to_records(index=False))

geoDict = {}
for my_triple in states_list:
  geoDict[my_triple[0]] = []

for i in states_list:
  geoDict[i[0]].append( (i[1], i[2]) )
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame
usa = gpd.read_file('/class/datamine/data/craigslist/cb_2018_us_state_20m.shp')
usa.crs = {'init': 'epsg:4269'}

pts = [Point(y,x) for x, y in geoDict.get("tx")]
gdf = gpd.GeoDataFrame(geometry=pts, crs = 4269)
fig, gax = plt.subplots(1, figsize=(10,10))
base = usa[usa['NAME'].isin(['Hawaii', 'Alaska', 'Puerto Rico']) == False].plot(ax=gax, color='white', edgecolor='black')
gdf.plot(ax=base, color='darkred', marker="*", markersize=10)
plt.show()
plt.close()

# to save to jpg:
plt.savefig('q5.jpg')

#6
import matplotlib.pyplot as plt

my_dict.keys()
my_dict.values()
plt.scatter(my_dict.keys(), my_dict.values(), color='red')
plt.xlabel("Year")
plt.ylabel("Value");
plt.show()
plt.close()
