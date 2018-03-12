import json
import urllib
import urllib2
def traveledDistance(travelLog):
    
    dist = 0
    
    maps_key = 'enterKeyHere'
    base_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
    

    start = travelLog[:-1]
    end = travelLog[1:]
    travelLog = zip(start,end)
    for d in travelLog:


        params = urllib.urlencode({
            'origins': d[0],
            'destinations': d[1],
            'key': maps_key,
        })
        url = base_url + params
        response = str(urllib2.urlopen(url).read())
        map_dict = json.loads(response.replace('\\n', ''))
        dist += (map_dict['rows'][0]['elements'][0]['distance']['value'])
    return dist