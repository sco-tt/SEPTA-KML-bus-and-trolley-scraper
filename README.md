Dependencies

NodeJS
npm
Python 2.7
Python Libraries:
	BeautifulSoup
	urllib2
	requests
	shutil
	os
	subprocess


Usage:

npm install
chmod +x scrape-septa-kml.py
python scrape-septa-kml.py

This will create two directories, 'kml' and 'geojson' that include all routes of the respective file type. Filename is [route]-[type].[extension], like 13-trolley.kml or 33-bus.geojson.

If you'd like to compress `all_routes.geojson`, install geojson-minifier globally.

npm install -g geojson-minifier
geojson-minifier -o pack -f all_routes.geojson -p 6

That will compress all_routes.geojson to ~10 MB. It's possible to load with leaflet.js if you change the extension to .js and declare a variable in the first line, like:

var septa = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",

and so on.




