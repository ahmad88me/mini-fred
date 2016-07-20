import requests
myheaders = {"Accept": "text/plain"}
r = requests.get("http://wit.istc.cnr.it/stlab-tools/fred", headers=myheaders, params={'text': 'My name is Ahmad'})
print r.text

