import requests
import json

url = "https://favqs.com/api/qotd"
response = requests.get(url)
data = response.json()
#print(data)

#for item in data["quote"]:
print(data["quote"]["body"])
print("")0-
print(data["quote"]["author"])

filename = 'quote.json'

f=open(filename,'w')
json.dump(data, f, indent=4)
