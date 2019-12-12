import requests
import json
import numpy as np
import pandas as pd


url = "https://data.smartdublin.ie/cgi-bin/rtpi/busstopinformation?stopid&format=json"
response = requests.get(url)
data = response.json()
#print(data)

#create with json codedump from Dublin Bus API
filename = 'bus.json'
f=open(filename,'w')
json.dump(data, f, indent=4)

#create a formatted pandas df and .csv file data from Dublin Bus API
busList = [] 
for stop in data["results"]:
    busList.append(stop["stopid"])
    busList.append(stop["fullname"])
    busList.append(stop["operators"][0]["routes"]) #source: https://stackoverflow.com/questions/25855276/parsing-json-with-python-typeerror-list-indices-must-be-integers-not-str
#print(busList)

if busList == 0:
    print('No Bus Routes Found')
else:
    a = np.asarray([ busList ]) 
    a = pd.DataFrame(a).T
    b = pd.DataFrame(np.asarray(a.iloc[::3, :]))
    c = np.asarray(a.iloc[1::3, :])
    d = np.asarray(a.iloc[2::3, :])
    b['2'] = c
    b['3'] = d
    b.columns=['StopID','Name','Routes']
    print('starting export')
    #b.to_csv("bus.csv", index=False, index_label=False)
    
c=b.to_dict('index')
#print(c)
print(c[8180]['Name'])
for entry in c:
    print(c[entry]['StopID'], c[entry]['Name'],c[entry]['Routes'] )

#for entry in c:
#    print(entry["Name"])
#    print(i['Routes'])
