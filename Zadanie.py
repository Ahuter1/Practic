import requests, json
#r = requests.get('https://raw.githubusercontent.com/QCplus/practice/main/query.json')
#b = r.text
file = open('json.txt')
f = file.read()
a = json.dumps(f)
print(a)