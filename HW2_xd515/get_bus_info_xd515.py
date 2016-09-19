from __future__ import print_function
import json
import os
import urllib2 
import csv
import sys

apikey = sys.argv[1]
bus = sys.argv[2]
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s" % (apikey, bus)

response = urllib2.urlopen(url)
data = response.read()
data = json.loads(data)
# Author: Fedhere

busline = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
busnumber = len(busline)

with open(sys.argv[3], 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Latitude', 'Longitude', 'Stop Name', 'Stop Status'])
        
        for i in range(busnumber):
            Lat = busline[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
            Lon = busline[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
