# -*- coding: utf-8 -*-
"""
DSC540-T301 Data Preparation (2215-1)
Purpose of Program:  Merging the Data and Storing in a Database/Visualizing Data
Author: Rajasekharreddy Karna
Date: 06/05/2021
"""

#import os #import the os library (enables operating system dependent functionality)
import requests
import pandas as pd
import sqlite3
import os 
import matplotlib.pyplot as plt


#Step-1 -- Read data from website and load into database table and print the data from database table.


#Read the data from the website and store same into CSV format for easy data access
url = 'https://apps.who.int/gho/athena/data/GHO/E1_nat_tv_radio,E2_intl_tv_radio,E3_nat_print,E4_intl_print,E5_billboards,E6a_pt_of_sale,E7_internet,E21a_direct_ad_fines,E_compl_all_dir,E9_free_distrib,E10_promo_discounts,E11_brand_stretching,E12_brand_sharing,E13_brand_placement,E14a_prod_tv_films,E14b_movies_anti_tob_ads,E15a_sponsorship,E15b_sponsor_contribution,E15c_sponsor_publicity,E21b_indirect_ad_fines,E_compl_e_all_indir,E17a_csr_ban,E17b_csr_promo_self,E17c_csr_promo_others,E18_csr_anti_tobacco_media,E6b_ban_display_pt_of_sale,E23_vending_machines,E24_internet_sales_ban,E22_subnational_authority_exists,E_comprehensive_subnat.html?profile=ztable&filter=COUNTRY:*;REGION:*'
html = requests.get(url).content
df_list = pd.read_html(html)
df = df_list[-1]
# Below can be used to export data into CSV file and read the same
#df.to_csv('my_data.csv')
#website_data = pd.read_csv('my_data.csv')

# create database table to store website data
query = """
CREATE TABLE web_source_data
(S_No VARCHAR(20), GHO VARCHAR(100),
 PUBLISHSTATE VARCHAR(20), YEAR VARCHAR(20),
 REGION VARCHAR(20), COUNTRY VARCHAR(20), DISPLAY_VALUE REAL, 
 NUMERIC_VALUE REAL, LOW_RANGE VARCHAR(20),
 HIGH_RANGE VARCHAR(20), COMMENT VARCHAR(20)
);"""

con = sqlite3.connect(':memory:')
con.execute(query) 
con.commit()

# Write the website data into a sqlite table
df.to_sql('web_source_data', con, if_exists='replace', index=False)

# Create a cursor object
cur = con.cursor()
# Fetch and display website loaded data into database table, only top 3 rows
for web_row in cur.execute('SELECT * FROM web_source_data LIMIT 3'):
    print(web_row)
# Close connection to SQLite database
con.close()



#Step-2 -- Read data from CSV file and load into database table and print the data from database table.


os.chdir('C:/Users/vahin/OneDrive/Documents/GitHub/DSC540Spring2021/DSC540/DSC540/Week11&12') #change directory
os.getcwd() #get the current working directory to confirm the directory change
csv_data = pd.read_csv('xmart.csv')

# create database table to store csv source data
query1 = """
CREATE TABLE csv_source_data
(Country VARCHAR(100),
YEAR VARCHAR(100),
Ban_ntl_tel_radio VARCHAR(100),
Ban_adv_tel_radio VARCHAR(100),
Ban_int_tel_radio VARCHAR(100),
Ban_local_mag_new VARCHAR(100),
Ban_int_mag_new VARCHAR(100),
Ban_bill_out_mag VARCHAR(100),
Ban_adv_pos VARCHAR(100),
Ban_adv_int VARCHAR(100),
Law_vio_adv_ban VARCHAR(100),
Overall_compl_score VARCHAR(100),
Ban_free_mail VARCHAR(100),
Ban_prom_dis VARCHAR(100),
Ban_non_t_brand_names VARCHAR(100),
Ban_non_t_products VARCHAR(100),
Ban_t_TV_Films VARCHAR(100),
Ban_app_TV_Films VARCHAR(100),
Requiredanti_timages VARCHAR(100),
Ban_sponsorship_publicity VARCHAR(100),
Ban_form_contribution VARCHAR(100),
Banning_publicity_individuals VARCHAR(100),
Law_requires_fines VARCHAR(100),
Overall_compliance_score VARCHAR(100),
Ban_CSR VARCHAR(100),
Ban_tobacco_CSR VARCHAR(100),
Ban_tobacco_companies_CSR VARCHAR(100),
Ban__smoking_prevention_youth VARCHAR(100),
Ban_product_POS VARCHAR(100),
Ban_tobacco_vending_machines VARCHAR(100),
Ban_internet_sales VARCHAR(100),
Subnational_bans_promotion_sponsorship VARCHAR(100),
Subnational_bans_comprehensive VARCHAR(100)
);"""

con = sqlite3.connect(':memory:')
con.execute(query1) 
con.commit()

# Write the csv data into a sqlite table
csv_data.to_sql('csv_source_data', con, if_exists='replace', index=False)

# Create a cursor object
cur = con.cursor()
# Fetch and display csv loaded data into database table, only top 3 rows
for csv_row in cur.execute('SELECT * FROM csv_source_data LIMIT 3'):
    print (csv_row)

# Close connection to SQLite database
con.close()



# HAVING CODING ISSUE TO LET JOIN WEBSITE SOURCE AND CSV FILE DATA SOURCE INTO SINGLE DATASET

#Join the datasets together in Python into 1 dataset
#for csv_web_row in cur.execute('SELECT * FROM csv_source_data outer join web_source_data on web_source_data.YEAR = csv_source_data.YEAR LIMIT 3'):
#   print (csv_web_row)

# HAVING CODING ISSUE TO VISUALIZE THE DATA

#visualizations the data 
#Creating the generic chart
#csv_web_row.plot(x="YEAR", y=["Country"])
#plt.plot(csv_web_row['YEAR'], csv_web_row['Country']) 
#Show the plot
#plt.show()


