from bs4 import BeautifulSoup
import csv
import numpy as np
import pandas as pd
with open("c:/Users/Eimear/Documents/GitHub/Sem_4_DataRepresentation_Assignments/Lab Week 3.html") as fp:
	soup = BeautifulSoup(fp, 'html.parser')

#print(soup.tr)

employee_file = open('c:/Users/Eimear/Documents/GitHub/Sem_4_DataRepresentation_Assignments/Week 3/week02data.csv', mode='w')
employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

rows = soup.findAll("tr")

for row in rows:
    cols = row.findAll("td")
dataList = []
for col in cols:
    dataList.append(col.text)

DL = pd.DataFrame(dataList).T ##Extra code to convert to pandas DF and remove 2 columns
employee_writer.writerow(DL.iloc[0, 0:3].T)
employee_file.close()
