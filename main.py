import requests

r = requests.get('https://api.github.com/user', auth=('factober', '@darshan1'))
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print(r.json())
print("Content Aggregator by Factober")