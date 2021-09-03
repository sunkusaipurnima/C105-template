import csv

with open('class2.csv',newline='') as f:
    reader= csv.reader(f)
    file_data= list(reader)
#print(file_data)  
file_data.pop(0) 

total_entries=len(file_data)
total_marks=0

for marks in file_data:
    total_marks+=float(marks[1])
#print(total_marks)   
mean = total_marks/total_entries

print("Mean or Average is ==>"+str(mean))

import pandas as pd
import plotly.express as px

df = pd.read_csv('class2.csv')
fig= px.scatter(df,x='Student Number', y='Marks')
fig.update_layout(shapes=[dict(type='line',y0=mean,y1=mean,x0=0,x1=total_marks)])
fig.show()
