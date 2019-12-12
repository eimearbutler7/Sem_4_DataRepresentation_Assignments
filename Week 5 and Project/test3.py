
import requests
import json
import numpy as np
import pandas as pd

urla = "https://data.smartdublin.ie/cgi-bin/rtpi/realtimebusinformation"
urlb = str(235)
urlc = "&format=json"

url = urla+urlb+urlc
response = requests.get(urla)
data = response.json()
print(data)

#create with json codedump from Dublin Bus API
filename = 'realtime.json'
f=open(filename,'w')
json.dump(data, f, indent=4)

#create a formatted pandas df and .csv file data from Dublin Bus API
busArrivals = [] 
for nextBus in data["results"]:
    busArrivals.append(nextBus["route"])
    busArrivals.append(nextBus["destination"])
    busArrivals.append(nextBus["duetime"]) 
print('RealTime Arrival Info for Bus Stop:', data["stopid"])
print(busArrivals)

if busArrivals == 0:
    print('No Bus Routes Found... you will have to walk')
else:
    a = np.asarray([ busArrivals ]) 
    a = pd.DataFrame(a).T
    b = pd.DataFrame(np.asarray(a.iloc[::3, :]))
    c = np.asarray(a.iloc[1::3, :])
    d = np.asarray(a.iloc[2::3, :])
    b['2'] = c
    b['3'] = d
    b.columns=['Route','Destination','Duetime']
#    b.to_csv("realtime.csv")
#    b.to_csv("server/realtime.csv")
live = b.to_dict('index')
print(live)

