import urllib.request
import json
src = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=400040'
f = urllib.request.urlopen( src )
str = f.read()
f.close()
q=json.loads(str)
print(q['description']['text'])
