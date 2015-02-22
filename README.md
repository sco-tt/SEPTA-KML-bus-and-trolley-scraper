## About

This is a basic Python script for downloading all bus and trolley route trace KML files from the [SEPTA data page](http://www3.septa.org/hackathon/). The script uses the Beautiful Soup library to build a list of routes from the list of [bus](http://www.septa.org/schedules/bus/index.html) and [trolley](http://www.septa.org/schedules/trolley/index.html) routes and then downloads a KML for each file. Using Node modules, each .KML can be converted to a geoJSON file, and each geoJSON can be combined into a single large geoJSON file (see geoJSON Usage).

## Dependencies

#### KML Only

Python 2.7
Python Libraries:

- BeautifulSoup
- urllib2
- requests
- shutil


#### geoJSON
Additional:

- NodeJS
- npm
- Python subprocess library


## KML Only Usage
	chmod +x scrape-septa-only-kml.py
	python scrape-septa-only-kml.py

KML files will appear in __output/kml__. Filename is [route]-[type].[extension], like _13-trolley.kml_ or _33-bus.geojson_. Open them all in Google Earth.

## geoJSON Usage:

	npm install
	chmod +x scrape-septa-kml-geojson.py
	python scrape-septa-kml-geojson.py

This will populate two directorie, __output/kml__ and __output/geojson__ that include all routes of the respective file type. 

If you'd like to compress _all-routes.geojson_, install the [geojson-minifier](https://github.com/igorti/geojson-minifier) package globally.

	npm install -g geojson-minifier
	geojson-minifier -o pack -f output/all_routes.geojson -p 6

That will compress all_routes.geojson to ~10 MB. It's possible to load with leaflet.js if you change the extension to .js and declare a variable in the first line, like:

	var septa = {
	  "type": "FeatureCollection",
	  "features": [
	    {
	      "type": "Feature",

and so on.

Leaflet can load the 10MB geoJSON file, but it will put some stress on your browser and take a _long_ time to load. Proof of concept [here](http://jsfiddle.net/sco_tt/tpp4jof7/4/).