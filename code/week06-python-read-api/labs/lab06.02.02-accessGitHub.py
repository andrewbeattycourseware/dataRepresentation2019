import requests
import json


# remove the minus sign
apiKey = 'b55d312da577ba479f7dc4f8f3f5b1384bdf3b2-e'
url = 'https://api.github.com/repos/datarepresentationstudent/aPrivateOne'
filename ="repo.json"

response = requests.get(url, auth=('token',apiKey))

repoJSON = response.json()
#print (response.json())

file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)

