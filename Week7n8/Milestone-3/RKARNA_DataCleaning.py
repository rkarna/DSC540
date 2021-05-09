# -*- coding: utf-8 -*-
"""
DSC540-T301 Data Preparation (2215-1)
Purpose of Program:  Cleaning/Formatting Website File Source
Author: Rajasekharreddy Karna
Date: 05/09/2021
"""


#import os #import the os library (enables operating system dependent functionality)

import requests
import pandas as pd
import numpy as np

url = 'https://apps.who.int/gho/athena/data/GHO/E1_nat_tv_radio,E2_intl_tv_radio,E3_nat_print,E4_intl_print,E5_billboards,E6a_pt_of_sale,E7_internet,E21a_direct_ad_fines,E_compl_all_dir,E9_free_distrib,E10_promo_discounts,E11_brand_stretching,E12_brand_sharing,E13_brand_placement,E14a_prod_tv_films,E14b_movies_anti_tob_ads,E15a_sponsorship,E15b_sponsor_contribution,E15c_sponsor_publicity,E21b_indirect_ad_fines,E_compl_e_all_indir,E17a_csr_ban,E17b_csr_promo_self,E17c_csr_promo_others,E18_csr_anti_tobacco_media,E6b_ban_display_pt_of_sale,E23_vending_machines,E24_internet_sales_ban,E22_subnational_authority_exists,E_comprehensive_subnat.html?profile=ztable&filter=COUNTRY:*;REGION:*'
html = requests.get(url).content
df_list = pd.read_html(html)
df = df_list[-1]
print(df)
df.to_csv('my data.csv')
data = pd.read_csv('my data.csv')

## Missing values analysis
data = pd.read_csv('my data.csv', header=0, na_values=['NA'])
#If a dataset contains missing data indicated by 'NA', you can read the data as above
print (data[pd.isnull(data['DISPLAY VALUE'])])

#Subset of dataset
print(data.iloc[:100,:]) #get the first 100 observations in a dataset (rows)
print(data.iloc[:100,:100]) #get the first 100 rows * 100 columns
print (data.loc[:,['REGION', 'YEAR']]) # Get the required columns

#Drop data 
print (data.drop([1, 3])) #drop the rows with index 1 and 3

print(data.drop(['YEAR', 'PUBLISHSTATE'], axis=1)) #axis=1 indicates a column to be dropped. Axis=0 indicates a row/index to be dropped.


#Transform data
print(data.drop_duplicates()) #remove duplicates --- no duplicates present
newdata = data.replace('NaN', 'Not Applicable') # replaced 'Not applicable' with 'N/A'
print (newdata.loc[:,['REGION', 'YEAR', 'NUMERIC VALUE']]) # Get the required columns
print(newdata.iloc[:30,:]) #get the first 30 observations in a dataset (rows)

rename_index = newdata.rename(index={0: 'row1'}) #renaming index value 0 with 'row1' data
print(rename_index)
print(pd.cut(newdata.YEAR, 4)) #numerical values make more sense if clustered together. Here we are dividing the survery's respondents in 4 groups.
#it displays the break values of the dataset for the four categories divided.

#Create new variable new column “CITIZEN” and designate the value for all observations to be 1:
print(newdata.assign(total_column = 30))

#Rename columns
print(newdata.rename(columns={'REGION':'City', 'YEAR':'Yr'}))

#Merge two data sets
#subset_7=data.iloc[:10, :100] #create the first subset
#subset_8=data.iloc[:10, [1, 100, 101, 102]] #create the second subset
#print(subset_7.merge(subset_8))#merge the two subsets