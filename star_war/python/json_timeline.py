#!/usr/bin/env python
# coding:utf8

import sys 
reload(sys)
sys.setdefaultencoding('utf8')

import time
import json
import pprint

films = []
characters = []
planets = []
starships = []
vehicles = []
species = []

fr = open('../csv/films.csv', 'r')
for line in fr:
	tmp = json.loads(line.strip('\n'))
	films.append(tmp)
fr.close()
fr = open('../csv/characters.csv', 'r')
for line in fr:
	tmp = json.loads(line.strip('\n'))
	characters.append(tmp)
fr.close()
fr = open('../csv/planets.csv', 'r')
for line in fr:
	tmp = json.loads(line.strip('\n'))
	planets.append(tmp)
fr.close()
fr = open('../csv/starships.csv', 'r')
for line in fr:
	tmp = json.loads(line.strip('\n'))
	starships.append(tmp)
fr.close()
fr = open('../csv/vehicles.csv', 'r')
for line in fr:
	tmp = json.loads(line.strip('\n'))
	vehicles.append(tmp)
fr.close()
fr = open('../csv/species.csv', 'r')
for line in fr:
	tmp = json.loads(line.strip('\n'))
	species.append(tmp)
fr.close()

print len(characters), len(planets), len(starships), len(vehicles), len(species)

data = []
for item in characters:
	tmp = []
	for film in films:
		flag = False
		for f in film['characters']:
			if item['url'] == f:
				flag = True
				break
		if flag:
			tmp.append(1)
		else:
			tmp.append(0)
	data.append({'name': item['name'], 'type': 'character', 'group': 0, 'vector': tmp})
for item in planets:
	tmp = []
	for film in films:
		flag = False
		for f in film['planets']:
			if item['url'] == f:
				flag = True
				break
		if flag:
			tmp.append(1)
		else:
			tmp.append(0)
	data.append({'name': item['name'], 'type': 'planet', 'group': 1, 'vector': tmp})
for item in starships:
	tmp = []
	for film in films:
		flag = False
		for f in film['starships']:
			if item['url'] == f:
				flag = True
				break
		if flag:
			tmp.append(1)
		else:
			tmp.append(0)
	data.append({'name': item['name'], 'type': 'starship', 'group': 2, 'vector': tmp})
for item in vehicles:
	tmp = []
	for film in films:
		flag = False
		for f in film['vehicles']:
			if item['url'] == f:
				flag = True
				break
		if flag:
			tmp.append(1)
		else:
			tmp.append(0)
	data.append({'name': item['name'], 'type': 'vehicle', 'group': 3, 'vector': tmp})
for item in species:
	tmp = []
	for film in films:
		flag = False
		for f in film['species']:
			if item['url'] == f:
				flag = True
				break
		if flag:
			tmp.append(1)
		else:
			tmp.append(0)
	data.append({'name': item['name'], 'type': 'species', 'group': 4, 'vector': tmp})

films = [[films[x]['title'], films[x]['release_date']] for x in xrange(0, len(films))]
result = {'films': films, 'data': data}

fw = open('../html/timeline.json', 'w')
fw.write(json.dumps(result))
fw.close()


