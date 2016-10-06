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

headers = {}
headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

fr = open('../csv/films.csv', 'r')
films = []
for line in fr:
	line = json.loads(line.strip('\n'))
	films.append(line)
fr.close()

# 获取 characters, planets, starships, vehicles, species
targets = ['characters', 'planets', 'starships', 'vehicles', 'species']
for target in targets:
	fw = open('../csv/' + target + '.csv', 'w')
	data = []
	for item in films:
		tmp = item[target]
		for t in tmp:
			if t in data:
				continue
			else:
				data.append(t)

			while 1:
				print t
				try:
					request = urllib2.Request(url=t, headers=headers)
					response = urllib2.urlopen(request, timeout=20)
					result = response.read()
				except Exception, e:
					continue
				else:
					fw.write(result + '\n')
					break
				finally:
					pass
	print str(len(data)) + ' ' + target
	fw.close()
