'''
DSC540-T301 Data Preparation (2215-1)
Purpose of Program:  visualizations -- Week 9 & 10: Point-4 Excercise
Author: Rajasekharreddy Karna
Date: 05/22/2021
'''

import matplotlib.pyplot as plt
import pandas as pd

#data = pd.read_csv("MetObjects.csv", encoding = 'unicode_escape', engine ='python')
#data.head()

#plt.plot(data)
#plt.show()
download_url = ("https://raw.githubusercontent.com/fivethirtyeight/"
                "data/master/college-majors/recent-grads.csv")
df = pd.read_csv(download_url)
type(df)
pd.set_option("display.max.columns", None)
df.head()
df.head(10)

#Creating the generic chart
df.plot(x="Rank", y=["P25th", "Median", "P75th"])
#Show the plot
plt.show()

#Creating the bar chart 
plt.barh(df['Rank'],df['Major_code'],color = ['#F0F8FF','#E6E6FA','#B0E0E6']) 
#Adding the aesthetics
plt.title('Bar Chart')
plt.xlabel('X axis title - Rank')
plt.ylabel('Y axis title - Major_code') 
#Show the plot
plt.show()


#Creating the line chart
plt.plot(df['Men'], df['Women']) 
#Adding the aesthetics
plt.title('Line Chart')
plt.xlabel('X axis title - Men')
plt.ylabel('Y axis title - Women') 
#Show the plot
plt.show()

#Creating the column histogram
ax = plt.gca()
ax.hist(df['Full_time'], color='blue',alpha=0.5, bins=10)
#Adding the aesthetics
plt.title('Histogram Chart')
plt.xlabel('X axis')
plt.ylabel('Y axis') 
#Show the plot
plt.show()


