#1.
import pandas as pd
import numpy as np
accidents=pd.DataFrame()
for i in range(1975,1982):
  s=str(i)
  accidents=pd.concat([accidents,pd.read_csv("/class/datamine/data/fars/"+s+"/ACCIDENT.CSV")])

accidents.head
accidents['YEAR']="19"+accidents['YEAR'].astype(str)
accidents['YEAR']

#2.
temp=accidents.loc[accidents.loc[:, 'SCH_BUS'] >0, :]
temp=temp.loc[temp.loc[:, 'DRUNK_DR'] >0, :]
temp.shape[0]

#3.
temp=temp.groupby(['YEAR'])
a=temp['YEAR'].count()
a
a.idxmax()

#4.
drk=[]
for i in range(0,7):
  tmp=accidents.loc[accidents.loc[:,'DRUNK_DR'] == i,:]
  count=tmp['PERSONS'].mean()
  drk.append(count)
drk

#5.
np.unique(accidents['HOUR'])
accidents['bins']=pd.cut(accidents['HOUR'], bins=[0,6,12,18,24,99],labels=[1,2,3,4,5],include_lowest=True,right=False,duplicates='drop')
acc=accidents.groupby(['bins'])
acc['FATALS'].sum()
acc['FATALS'].mean()
