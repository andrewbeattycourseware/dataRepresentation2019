import requests
import json

#html = '<h1>hello world</h1>This is html'
f = open("../../week02/carviewer2.html", "r")
html = f.read()

apiKey = '46ceed910c24ff7cce8240e89ec7b71912f6f40f2ec55fd217ce150ad6d4f1c4'
url = 'https://api.html2pdf.app/v1/generate'

# putting the API key in as data
data = {'html': html,'apiKey': apiKey}
response = requests.post(url, json=data)

newFile = open("lab06.02.01.htmlaspdf.pdf", "wb")
newFile.write(response.content)
print (response.status_code)