#!/usr/bin/env python
# coding:utf8

import sys 
reload(sys)
sys.setdefaultencoding('utf8')

import time
import json
import pprint

data = {}

fr = open('../csv/films.csv', 'r')
for line in fr:
	tmp = json.loads(line.strip('\n'))
	data[tmp['title']] = tmp
fr.close()
fr = open('../csv/characters.csv', 'r')
for line in fr:
	tmp = json.loads(line.strip('\n'))
	data[tmp['name']] = tmp
fr.close()
fr = open('../csv/planets.csv', 'r')
for line in fr:
	tmp = json.loads(line.strip('\n'))
	data[tmp['name']] = tmp
fr.close()
fr = open('../csv/starships.csv', 'r')
for line in fr:
	tmp = json.loads(line.strip('\n'))
	data[tmp['name']] = tmp
fr.close()
fr = open('../csv/vehicles.csv', 'r')
for line in fr:
	tmp = json.loads(line.strip('\n'))
	data[tmp['name']] = tmp
fr.close()
fr = open('../csv/species.csv', 'r')
for line in fr:
	tmp = json.loads(line.strip('\n'))
	data[tmp['name']] = tmp
fr.close()

fw = open('../html/all.json', 'w')
fw.write(json.dumps(data))
fw.close()

