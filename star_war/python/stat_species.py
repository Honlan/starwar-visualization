#!/usr/bin/env python
# coding:utf8

import sys 
reload(sys)
sys.setdefaultencoding('utf8')

import time
import json
import pprint

fr = open('../csv/species.csv', 'r')
fw = open('../csv/stat_species.csv', 'w')
fw.write('name,height,lifespan,classification\n')
for line in fr:
	tmp = json.loads(line.strip('\n'))
	if tmp['classification'] == 'mammals':
		tmp['classification'] = 'mammal'
	if tmp['classification'] == 'reptilian':
		tmp['classification'] = 'reptile'
	if tmp['average_height'] in ['unknown', 'n/a']:
		tmp['average_height'] = '-1'
	if tmp['average_lifespan'] in ['unknown', 'indefinite']:
		tmp['average_lifespan'] = '-1'
	fw.write(tmp['name'] + ',' + tmp['average_height'] + ',' + tmp['average_lifespan'] + ',' + tmp['classification'] + '\n')

fr.close()
fw.close()