from bs4 import BeautifulSoup                                                   
import urllib2
import requests
import shutil
import os
import subprocess

# Make Project Directories and assign variables
projectdir = os.getcwd()
os.mkdir(os.path.join(projectdir, 'output'))		
os.mkdir(os.path.join(projectdir, 'output/kml'))		
kml_dir = os.path.join(projectdir, 'output/kml')

# scrape data from SEPTA's website to get all of the routes
buses = BeautifulSoup(urllib2.urlopen('http://www.septa.org/schedules/bus/index.html').read())
bus_matches = buses.find_all("div", class_="route_num")
trolleys = BeautifulSoup(urllib2.urlopen('http://www.septa.org/schedules/trolley/index.html').read())
trolley_matches = trolleys.find_all("div", class_="route_num")

print "Downloading bus route KML files"
for x in bus_matches:
    if x.string:
		route = x.string.strip().upper() 		# Must be uppercase or route 47M is going to fail			
		url = 'http://www3.septa.org/transitview/kml/%s.kml' % route
		response = requests.get(url, stream=True)
		if response.status_code == 200:
			with open('%s/%s-bus.kml' % (kml_dir,route), 'wb') as out_file:
			    shutil.copyfileobj(response.raw, out_file)
			print "Sucessfully downloaded from: %s" % url
			del response
		else:
			print "Downloaded from %s failed" % url

print "Downloading trolley route KML files"
for x in trolley_matches:
    if x.string:
		route = x.string.strip().upper() 				
		url = 'http://www3.septa.org/transitview/kml/%s.kml' % route
		response = requests.get(url, stream=True)
		if response.status_code == 200:
			with open('%s/%s-trolley.kml' % (kml_dir,route), 'wb') as out_file:
			    shutil.copyfileobj(response.raw, out_file)
			print "Sucessfully downloaded from: %s" % url
			del response
		else:
			print "Downloaded from %s failed" % url

print "Converting to geoJSON"
os.mkdir(os.path.join(projectdir, 'output/geojson'))
geojson_dir = os.path.join(projectdir, 'output/geojson')

# Define node module utilities
togeojson_util = os.path.join(projectdir, 'node_modules/togeojson')
geojson_merge_util = os.path.join(projectdir, 'node_modules/geojson-merge')

for filename in os.listdir(kml_dir):
	filepath = os.path.join(kml_dir, filename)
	route_name = os.path.splitext(filename)[0]
	subprocess.call(["%s/togeojson %s > %s/%s.geojson" % (togeojson_util, filepath, geojson_dir, route_name)], shell=True)
	print "%s convereted to geoJSON" % route_name
	
print "Merging geojson files"
all_geojson_files = ""
for filename in os.listdir(geojson_dir):
	filepath = os.path.join(geojson_dir, filename)
	all_geojson_files += "%s/%s " % (geojson_dir, filename)
subprocess.call(["%s/geojson-merge %s > output/all-routes.geojson" % (geojson_merge_util, all_geojson_files)], shell=True)





