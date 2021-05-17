#Q1
import pandas as pd
myDF = pd.read_csv("/class/datamine/data/craigslist/vehicles.csv")
myDF.head()

from pathlib import Path
p = Path("/class/datamine/data/craigslist/vehicles.csv")
p.stat().st_size
print(f'my file size is: {p.stat().st_size/1000000}')

#Q2
myDF.shape
print(f'The number of rows are: {myDF.shape[0]}')
print(f'The number of columns are: {myDF.shape[1]}')
myDF = pd.read_csv("/class/datamine/data/craigslist/vehicles.csv")
myDF.columns

#Q3
columns
columns = list(myDF.columns)
len(columns)
columns.append("extra")
print(f'Second column name is :{columns[1]}')
print(f'Patterned column names are: {columns[::2]}')
print(f'Last four column names are: {columns[-4:]}')
columns.remove("extra")


#Q4
from matplotlib import pyplot as plt
my_values = list(tuple(myDF.loc[:, 'odometer'].dropna().to_list()))
my_values.sort()
plt.plot(my_values[0:-50], color="blue")
plt.title("Cars vs odometer readings")
plt.xlabel("Amount of cars")
plt.ylabel("Odometer readings")
plt.show()
plt.close()

#Q5
from matplotlib import pyplot as plt
myDF.sort_values(['year', 'price'], inplace = True)
plt.plot(myDF['year'], myDF['price'], color="#FB8072", linestyle="dashed")
plt.title("Price and Year")
plt.xlabel("Price")
plt.ylabel("Year")
plt.show()
plt.close()


