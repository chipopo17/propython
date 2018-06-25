#!/usr/bin/python
# coding: UTF-8

import urllib
import json

src = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010'
f = urllib.urlopen( src )
str = f.read()
f.close()

q = json.loads( str )

print (q['description']['text'])
