import pandas as pd

data = pd.read_csv("candyhierarchy2017.csv", encoding = 'unicode_escape', engine ='python')
data.head()

## Missing data
data = pd.read_csv('candyhierarchy2017.csv', encoding = 'unicode_escape', engine ='python', header=0, na_values=[''])
#If a dataset contains missing data indicated by 'NA', you can read the data as above
print (data[pd.isnull(data['Q1: GOING OUT?'])])


#Replace data
print(data.drop_duplicates()) #remove duplicates, if any
newdata = data.replace("I'd rather not say", 'Not Mentioned') # replaced 'Not applicable' with 'N/A'
print (newdata.loc[:,['Q2: GENDER']]) # Get the required columns
print(newdata.iloc[:30,:]) #get the first 30 observations in a dataset (rows)

#Join 2 CSV files
csv1 = pd.read_csv("candyhierarchy2017.csv", encoding = 'unicode_escape', engine ='python')
csv1.head()
csv2 = pd.read_csv("candyhierarchy.csv", encoding = 'unicode_escape', engine ='python')
csv2.head()
merged_data = csv1.merge(csv2,on=["Internal ID"])
print(merged_data.head())

#Reshape
csv2= csv2.iloc[:12][:1000]
print (csv2.head())

#Pivot Tables
csv2 = pd.pivot_table(csv1, columns=['Q5: STATE, PROVINCE, COUNTY, ETC'], index=csv1.index)
csv2.to_csv('Pivot_Output.csv')


#Split
#c1 = []
#c2 = []
#c3 = []
#with open('candyhierarchy.csv', 'r') as f:
#    reader = csv2.reader(f, delimiter=',', encoding = 'unicode_escape', engine ='python')
#    for row in reader:
#        c1.append(row[0])
#        c2.append(row[1])
#        c3.append(row[2])
#print (row)


#Group data from a CSV file by field value

#result = {}

#with open('candyhierarchy.csv', 'rb') as csvfile:
#    csvreader = csv2.reader(csvfile, delimiter=',', quotechar='"')
#    for row in csvreader:
#        if row[0] in result:
#            result[row[0]].append(row[1])
#        else:
#            result[row[0]] = [row[1]]


#Grouping with Dicts/Series
FILENAME = "candyhierarchy2017.csv"
river_dict = dict()

with open(FILENAME) as fd:
    line = (l for l in fd.readlines())
    detail = (d.split(',') for d in line)
    for river_name, branch, length in detail:
        river_name, branch, length = map(str.strip, [river_name, branch, length])
        with open(river_name.title() + ".csv", "a") as rd:
            rd.write("{0}, {1}\n".format(branch, length))
            
            
#Convert between string and date time      
#import csv
#import datetime
#with open ('candyhierarchy.csv') as csvfile:
#    readablefile = csv.reader(csvfile)
#    writablefile = csv.writer(csvfile)
#    for row in readablefile:
#        date_format = datetime.datetime.strftime('%Y-%m-%d %H:%M:%S')
#        writablefile.writerow(date_format)
        
      
df = pd.read_csv("candyhierarchy2017.csv", encoding = 'unicode_escape', engine ='python')
saved_column = df['St Date']
print(saved_column)
        
import datetime
format = "%Y-%m-%d %H:%M:%S"
#dt_object = datetime.datetime.strptime(data['End Date'], format)
#print("Datetime: ", dt_object)
#print("Minute: ", dt_object.minute)
#print("Hour: ", dt_object.hour)
#rint("Second: ", dt_object.second)


pd.read_csv("candyhierarchy2017.csv", encoding = 'unicode_escape', engine ='python', parse_dates = ['End Date']) 
data['St Date'] = pd.to_datetime(data['St Date'], format = '%d/%m/%y')
print(data['St Date'])