from __future__ import print_function
import json
import os
import urllib2 
import sys

apikey = sys.argv[1]
bus = sys.argv[2]
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s" %(apikey, bus)

response = urllib2.urlopen(url)
data = response.read()
data = json.loads(data)

# Author: Fedhere

data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]
busline = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
busnumber = len(busline)

print ("Bus line : %s" %(sys.argv[2]))
print ("Number of Active Buses : %s" %(busnumber))

for i in range (busnumber):
    latitude = busline[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude = busline[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print ('Bus {} is at latitude {} and longitude {}'.format(i,latitude,longitude))
