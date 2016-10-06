#!/usr/bin/env python
# coding:utf8

import sys 
reload(sys)
sys.setdefaultencoding('utf8')

import urllib2
import urllib
import time
import json
import pprint

films = []
for x in xrange(1, 8):
	films.append('http://swapi.co/api/films/' + str(x) + '/')

headers = {}
headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

fw = open('films.csv', 'w')

for item in films:
	print item
	request = urllib2.Request(url=item, headers=headers)
	response = urllib2.urlopen(request, timeout=20)
	result = response.read()
	fw.write(result + '\n')

fw.close()	
	