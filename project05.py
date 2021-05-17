#Q1

from pathlib import Path
p = Path("/class/datamine/data/stackoverflow/unprocessed/2018.csv")
size_in_csv = p.stat().st_size
size_in_csv
print(f'Size in bytes: {size_in_csv}')

from pathlib import Path
p = Path("/class/datamine/data/stackoverflow/unprocessed/2018.parquet")
size_in_parquet = p.stat().st_size
size_in_parquet
print(f'Size in bytes: {size_in_parquet}')

from pathlib import Path
p = Path("/class/datamine/data/stackoverflow/unprocessed/2018.feather")
size_in_feather = p.stat().st_size
size_in_feather
print(f'Size in bytes: {size_in_feather}')

print(f'The parquet file is smaller than the csv by {(size_in_csv-size_in_parquet)/size_in_parquet:.2%}')
print(f'The feather file is smaller than csv by {(size_in_csv-size_in_feather)/size_in_feather:.2%}')


from block_timer.timer import Timer
import pandas as pd
with Timer(title="csv") as csv:
  myDF = pd.read_csv("/class/datamine/data/stackoverflow/unprocessed/2018.csv")

with Timer(title="parquet") as parquet:
  myDF1 = pd.read_parquet("/class/datamine/data/stackoverflow/unprocessed/2018.parquet")

with Timer(title="feather") as feather:
  myDF1 = pd.read_feather("/class/datamine/data/stackoverflow/unprocessed/2018.feather")
  
print(f'The parquet file is faster than the csv by {(csv.elapsed-parquet.elapsed)/parquet.elapsed:.2%}')
print(f'The feather file is faster than the csv by {(csv.elapsed-feather.elapsed)/feather.elapsed:.2%}')


("/class/datamine/data/stackoverflow/unprocessed/2018.csv")
with Timer(title="csv") as csv:
  myDF.to_csv("/scratch/scholar/choe29/2018.csv")

with Timer(title="parquet") as parquet:
  myDF.to_parquet("/scratch/scholar/choe29/2018.parquet")

with Timer(title="feather") as feather:
  myDF.to_feather(("/scratch/scholar/choe29/2018.feather"))
  
print(f'The parquet file is faster than the csv by {(csv.elapsed-parquet.elapsed)/parquet.elapsed:.2%}')
print(f'The feather file is faster than the csv by {(csv.elapsed-feather.elapsed)/feather.elapsed:.2%}')


#Q2
import pandas as pd

myDF = pd.read_csv("/class/datamine/data/stackoverflow/unprocessed/2018.csv")

not_studentsDF = myDF.loc[myDF.loc[:,"Student"] == 'No', :]
percentage = len(not_studentsDF.loc[:,"Respondent"])/len(myDF.loc[:,"Respondent"])

print(f'{percentage*100}%')


#Q3

professions = [p.split(";") for p in not_studentsDF.loc[:, "DevType"].dropna().tolist()]

professions = [p for li in professions for p in li]
professions = list(set(professions))
print(professions)

print(len(professions))


studentsDF = myDF.loc[(myDF.loc[:,"Student"] == 'No') & (myDF.loc[:,"DevType"].str.contains("Student")), :]
len(studentsDF)

#There are 20 professions. There are 3723 number of respondents that replied "No" to Student, yet put "Student" as the DevType.

#Q4
#FEMALES
import random
print(f"A random integer between 1 and 100 is {random.randint(1, 101)}")
females = myDF.loc[(myDF.loc[:, "Gender"]=="Female"), :]
femaleage=[]
femaleage = [random.randint(0, len(females)) for i in range(0,100)]
females = females.iloc[femaleage]
print(femaleage)
females.loc[:,"Age"].value_counts().plot.bar()
print(females)
plt.show()
plt.close()

import random
print(f"A random integer between 1 and 100 is {random.randint(1, 101)}")
males = myDF.loc[(myDF.loc[:, "Gender"]=="Male"), :]
maleage=[]
maleage = [random.randint(0, len(males)) for i in range(0,100)]
males = males.iloc[femaleage]
print(maleage)
males.loc[:,"Age"].value_counts().plot.bar()
print(males)
plt.show()
plt.close()

#

#5
import pandas as pd
from matplotlib import pyplot as plt
my_values = list(tuple(myDF.loc[:, 'odometer'].dropna().to_list()))
my_values.sort()
plt.plot(my_values[0:-50], color="blue")
plt.title("Cars vs odometer readings")
plt.xlabel("Amount of cars")
plt.ylabel("Odometer readings")
plt.show()
plt.close()

#I created a lineplot of the odometer readings from all of the vehicles in our dataset.

