import json
import urllib
import urllib2
def traveledDistance(travelLog):
    
    dist = 0
    
    maps_key = 'enterKeyHere' #enter API key
    base_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
    

    start = travelLog[:-1]
    end = travelLog[1:]
    #find all of the start and end points in the journey by zipping together an offset version of the travelLog
    travelLog = zip(start,end)
    #iterate over the travelLog and find the distance between each tuple of locations in google's distanceMatrix API
    #could have used the full list with one call, but this produces distances bewteen every permutation of entries
    #which seemed unnecessary and time consuming
    for d in travelLog: 
        params = urllib.urlencode({
            'origins': d[0],
            'destinations': d[1],
            'key': maps_key,
        })
        url = base_url + params
        response = str(urllib2.urlopen(url).read())
        map_dict = json.loads(response.replace('\\n', ''))
        #extract the distance value from the json response of the API and add to the running distance total
        dist += (map_dict['rows'][0]['elements'][0]['distance']['value'])
    return dist
