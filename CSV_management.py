import pandas as pd
import csv

# read the CSV with first row as header
df = pd.read_csv('file_path.csv', header=[0])
df .head()

#print the csv read
print(df )

# if for example df . has 3 columns with user, pass and status
# iterate and print a column
for i in len(df ):
  print(df ['user'][i])
  
#edit a entity in the CSV file
df ['user'][5]="Aegan@gmail.com"

#append a row to the csv
df  = df .append({'user': "rs@indigo.ca",'pas':"Password",'status':"Blocked"}, ignore_index=True)

#$$$ in drop function also takes in list of entities or a string and deletes respective row or column
#delete a column in csv
df .drop('status', inplace=True, axis=1)
#deletea row in csv
df .drop(['rs@indigo.ca', inplace = True)

#save the edited instance back to csv file
df .to_csv('file_path.csv',index=False)
