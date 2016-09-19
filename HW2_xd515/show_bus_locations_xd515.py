from __future__ import print_function
import json
import os
import urllib2 
import sys

apikey = os.getenv("BUSAPIKEY")
bus = sys.argv[2]
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?\
key=2a4a54c7-f386-4aaf-90a7-82fe5ed31bc4&VehicleMonitoringDetailLevel=calls&LineRef=B52"

response = urllib2.urlopen(url)
data = response.read()
data = json.loads(data)
print (data)

# Author: Fedhere

data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]
busline = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]\
                ['VehicleActivity']
busnumber = len(busline)

print 'Bus line : %s' %sys.argv[2]
print 'Number of Active Buses : %s' %busnumber

for i in range (0,len(busnumber)):
    latitude = busline[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude = busline[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print ('Bus {} is at latitude {} and longitude {}'.format(i,latitude,longitude))
