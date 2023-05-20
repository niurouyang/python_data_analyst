import json
import urllib3
http = urllib3.PoolManager()
r= http.request('GET', 'https://newsapi.org/v2/everything?q=Python programming language&apiKey=e584fe8c8fb545f4b0884204f29437fc&pageSize=5')
# q is the search parameter in request URL; the other requested parameter is apikey =e584fe8c8fb545f4b0884204f29437fc
articles = json.loads(r.data.decode('utf-8'))

for article in articles['articles']:
    print(article['title'])
    print(article['publishedAt'])
    print(article['url'])
    print()


import requests
import ast
request_strings={'q':'Python programming language',
                 'apiKey':'e584fe8c8fb545f4b0884204f29437fc', 'pageSize':2}
r=requests.get(url='https://newsapi.org/v2/everything',params=request_strings)
articles=json.loads(r.text)
for article in articles['articles']:
    print(article['title'])
    print(article['publishedAt'])
    print(article['url'])
    print()


