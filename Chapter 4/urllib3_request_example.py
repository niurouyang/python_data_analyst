import urllib3
http = urllib3.PoolManager()
r= http.request('GET', 'http://localhost/excerpt.txt')
for i, line in enumerate(r.data.dcode('utf-8').split('\n')):
    if line.strip():
        print('Line %i:' %(i), line.strip())


# use requests library
import requests
r=requests.get('http://localhost/excerpt.txt')
for i, line in enumerate(r.text.split('\n')):
    # request can automatic decode the retrieved content
    if line.strip():
        print('Line %i:' %(i), line.strip())
        # output only have nonempty line, add a line number
        