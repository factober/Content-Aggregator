import requests

r = requests.get('https://api.github.com/user', auth=('', ''))
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print(r.json())
print("Content Aggregator by Factober")
