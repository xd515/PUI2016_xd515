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

# Author: Febhere

data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]
busline = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]\
                ['VehicleActivity']
busnumber = len(busline)

with open(sys.argv[3], 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Latitude', 'Longitude', 'Stop Name', 'Stop Status'])
        
        for i in range(busnumber):
            Lat = busline[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
            Lon = busline[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
                
            if busline[i]['MonitoredVehicleJourney']['OnwardCalls'] == {}:
                StopName = "N/A"
                StopStatus = "N/A"
            else:
                Stop_Name = busline[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
                Stop_Status = busline[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
                    
            writer.writerow([Lat, Lon, Stop_Name, Stop_Status])
