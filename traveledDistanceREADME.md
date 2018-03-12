You've been traveling all over the world by car. Once in a while you log your current location into your travelLog. If you don't know the name of the place you're at, you just write the latitude,longitude of your location in the log, where latitude and longitude are expressed in decimal degrees. If you do know where you are, you write the name of the location.

Given the travelLog, find the distance in meters that you've traveled by car, starting from the place from the first travelLog entry and ending at the location of the last travelLog entry.

Useful APIs

In this task you are expected to use a GIS API. For example: Google Maps API or OSRM.

The reference answers are calculated using the Google Maps API, but you can use any GIS APIs you want as long as your answer doesn't differ from the reference by more than 10%.

Example

For travelLog = ["New York, NY, USA", "Toronto, ONT", "Los Angeles, CA, USA"], the output should be
traveledDistance(travelLog) = 4850514.