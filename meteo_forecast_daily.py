#!/usr/bin/python
#-*- encoding: utf-8 -*-
import datetime
import json
import urllib2

weather = urllib2.urlopen("http://api.openweathermap.org/data/2.5/forecast/daily?id=2659296&cnt=14&units=metric&lang=fr")
wjson = weather.read()
wjdata = json.loads(wjson)

print '-' * 49
print 'METEO DE LA SEMAINE - PREVISION SUR 14 JOURS'
print '-' * 49
for i in wjdata["list"]:
	print 'Le ',(datetime.datetime.fromtimestamp(int(i["dt"])).strftime('%Y-%m-%d %H:%M:%S')), 'il fera :'
	print i["weather"][0]["description"]
	print i["temp"]["day"], 'degrés en journée'
	print i["temp"]["min"], 'degrés au minimum'
	print i["temp"]["max"], 'degrés au maximum'
	print i["temp"]["morn"], 'degrés le matin'
	print i["temp"]["eve"], 'degrés en soirée'
	print i["temp"]["night"], 'degrés la nuit'
	print 'Le vent soufflera à',i["speed"], 'mètres par seconde'
	print i["humidity"], "% d'humidité"
	print "Pression atmosphérique:",i["pressure"], "pascals"
	print '-' * 49

