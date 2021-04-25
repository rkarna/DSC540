# -*- coding: utf-8 -*-
"""
DSC540-T301 Data Preparation (2215-1)
Purpose of Program:  Cleaning/Formatting CSV File Source
Author: Rajasekharreddy Karna
Date: 04/24/2021
"""

import os #import the os library (enables operating system dependent functionality)
os.chdir('C:/Users/vahin/OneDrive/Documents/GitHub/DSC540Spring2021/DSC540/DSC540/Week5n6/Milestone-2') #change directory
os.getcwd() #get the current working directory to confirm the directory change

import pandas #import the pandas data analysis library
import numpy as np
data = pandas.read_csv('xmart.csv')

print(data.shape) #dimension of the dataset using the shape command. In our case, the dataset has 1365 rows and 32 columns.

print(data.describe()) #view the descriptive statistics of the varaibles in our dataset with numeric values using the describe command.

## Missing values analysis
data = pandas.read_csv('xmart.csv', header=0, na_values=['NA'])
#If a dataset contains missing data indicated by 'NA', you can read the data as above
print (data[pandas.isnull(data['Subnational bans on tobacco advertising, promotion and sponsorship authority exists'])])

#Subset of dataset
print(data.iloc[:100,:]) #get the first 100 observations in a dataset (rows)
print(data.iloc[:100,:100]) #get the first 100 rows * 100 columns
print (data.loc[:,['Country', 'Year']]) # Get the required columns

#Drop data 
print (data.drop([1, 3])) #drop the rows with index 1 and 3

print(data.drop(['Year', 'Ban on advertising on national television and radio'], axis=1)) #axis=1 indicates a column to be dropped. Axis=0 indicates a row/index to be dropped.


#Transform data
print(data.drop_duplicates()) #remove duplicates --- no duplicates present
newdata = data.replace('Not applicable', 'N/A') # replaced 'Not applicable' with 'N/A'
print (newdata.loc[:,['Country', 'Year', 'Law requires fines for violations of advertising bans']]) # Get the required columns
print(newdata.iloc[:30,:]) #get the first 30 observations in a dataset (rows)

rename_index = newdata.rename(index={0: 'row1'}) #renaming index value 0 with 'row1' data
print(rename_index)
print(pandas.cut(newdata.Year, 4)) #numerical values make more sense if clustered together. Here we are dividing the survery's respondents in 4 groups.
#it displays the break values of the dataset for the four categories divided.

#Create new variable new column “CITIZEN” and designate the value for all observations to be 1:
print(newdata.assign(total_column = 30))

#Rename columns
print(newdata.rename(columns={'Country':'Nation', 'Year':'Yr'}))

#Merge two data sets
#subset_7=data.iloc[:10, :100] #create the first subset
#subset_8=data.iloc[:10, [1, 100, 101, 102]] #create the second subset
#print(subset_7.merge(subset_8))#merge the two subsets
