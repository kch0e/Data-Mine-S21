#Q1

#First place - My first impression is that the author had great visuals and graphics but some of them were smaller and harder to read.
#Second place - My first impression is that the author spend time on the poster to explain their visuals as there is various descriptions.
#Third place - My first impression is that the author had great struture organizing their visuals and there are lot of colors represening variables.
#Honorable mention-  My first impression is that the author spent alot of time on their poster explaning the complicated conepts in a very simple way to understand.
#Other posters - My first impression is that the author put alot of code but is lacking visuals to explain thier concepts. There was some text but not enough to understand.
#Other posters - My first impression is that the author had some detailed graphics but it was very confusing to follow and grasp what they wanted to display.
#Other posters - My first impression is that the author spent alot of time organizing the plots and it was easy to see their thought process and execution.
#Other posters - My first impression is that the author spend little time putting effort into their poster's aesthetic as it was very basic and did not have much content.

#Q2
#One interesting thing I liked was how the author presented the ownership of government securities. The graph was well presented and I understood how the budget was spread out.
#The second thing I learned was the various trends of imports and exports of England that shifted the balance of trade data. I liked how they included multiple iteratiosn of it.

#One thing I liked about this excerpt was the various ways the author presents their data and shows the reader how to do so and how to display meaning and imapct behind the graphs.
#Another thing I learned is how we can pack a large amount of quantitive information into a small region. This maximizes space and allows the reader to see the various datapoint impact.

#Q3
import pandas as pd
import matplotlib.pyplot as plt
myDF = pd.read_csv("/class/datamine/data/flights/subset/2008.csv")
myDF.head()
pd.set_option('display.max_columns', None)
myDF = myDF.loc[: , ['DepDelay', "DayOfWeek", "Month", "Origin", "ArrDelay"]].dropna()
myDF['DayOfWeek'] = myDF['DayOfWeek'].replace([1,2,3,4,5,6,7],['Mon','Tues','Wed','Thurs','Fri','Sat','Sun'])
myDF.head()
plt.scatter(myDF.loc[: ,"DayOfWeek"].to_list()[0:500000], myDF.loc[: ,"DepDelay"].to_list()[0:500000])
plt.show()
plt.close()
# I comapred each Day of the Week to the number of departure delays occurances. The best practices from 2 texts I followed was visualzing all days and including various datapoints.
 
myDF['Month'] = myDF['Month'].replace([1,2,3,4,5,6,7,8,9,10,11,12],['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
myDF.head()
plt.scatter(myDF.loc[: ,"Month"].to_list()[0:500000000000], myDF.loc[: ,"DepDelay"].to_list()[0:500000000000])
plt.show()
plt.close()

# I comapred the first few months of the Spring season to the number of departure delays occurances. Practices I used were including a specfic range of time and including many samples.
myDF['Origin'] = myDF['Origin'].replace([1,2],['IND','LAX',])
myDF.head()
plt.scatter(myDF.loc[: ,"Origin"].to_list()[0:500], myDF.loc[: ,"DepDelay"].to_list()[0:500])
plt.show()
plt.close()

# I compared a sample of flight location orgins against the number of depature delay occurances. Practices I used were spreading my data apart and having it look visually appealing.

myDF['Origin'] = myDF['Origin'].replace([1,2],['HOU','LAX',])
myDF.head()
plt.scatter(myDF.loc[: ,"Origin"].to_list()[0:500], myDF.loc[: ,"ArrDelay"].to_list()[0:500])
plt.show()
plt.close()

# I compared the flight origins of location origns versus the nymber of arriveal delay occurances. Pracitices I used were including as many origins and including outliers within it.

#Q4
#First place - My second impression is that the author had decent visuals and some graphics but many were smaller and harder to read.
#Second place - My second impression is that the author spent some time on the poster to explain their decent visuals as there is long descriptions.
#Third place - My second impression is that the author had some struture organizing their visuals and various colors represening variables.
#Honorable mention-  My second impression is that the author spent some time on their poster explaning the complex conepts in bits and pieces.
#Other posters - My second impression is that the author put alot of their working code but needs more bright visuals to make it appealing.
#Other posters - My second impression is that the author had various detailed graphics but it was still very confusing to follow and grasp what they wanted to display.
#Other posters - My second impression is that the author spent some time organizing the plots and it was somewhat easy to see their thought process and execution.
#Other posters - My second impression is that the author spend very little time putting effort into their poster's aesthetic as it was very basic and did not have much content.





 



