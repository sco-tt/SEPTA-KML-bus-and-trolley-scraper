from bs4 import BeautifulSoup                                                   
import urllib2
# https://stackoverflow.com/questions/13137817/how-to-download-image-using-requests
# http://python.dzone.com/articles/how-download-file-python
import requests
import shutil
import os

buses = BeautifulSoup(urllib2.urlopen('http://www.septa.org/schedules/bus/index.html').read())
bus_matches = buses.find_all("div", class_="route_num")
trolleys = BeautifulSoup(urllib2.urlopen('http://www.septa.org/schedules/trolley/index.html').read())
trolley_matches = trolleys.find_all("div", class_="route_num")

print "Download bus route KML files"

for x in bus_matches:
    if x.string:
		route = x.string.strip().upper() 				#Must be uppercase or route 47M is going to fail
		url = 'http://www3.septa.org/transitview/kml/%s.kml' % route
		response = requests.get(url, stream=True)
		if response.status_code == 200:
			with open('%s-bus.kml' % route, 'wb') as out_file:
			    shutil.copyfileobj(response.raw, out_file)
			print "Sucessfully downloaded from: %s" % url
			del response
		else:
			print "Downloaded from %s failed" % url

print "Download trolley route KML files"

for x in trolley_matches:
    if x.string:
		route = x.string.strip().upper() 				
		url = 'http://www3.septa.org/transitview/kml/%s.kml' % route
		response = requests.get(url, stream=True)
		if response.status_code == 200:
			with open('%s-trolley.kml' % route, 'wb') as out_file:
			    shutil.copyfileobj(response.raw, out_file)
			print "Sucessfully downloaded from: %s" % url
			del response
		else:
			print "Downloaded from %s failed" % url

print "Converting to geoJSON"


projectdir = os.getcwd()
dldir = os.path.join(projectdir, 'downloads')
for filename in os.listdir(projectdir):
     print filename





