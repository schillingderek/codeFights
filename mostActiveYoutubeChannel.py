DEV_KEY = "enterKeyHere"
import urllib, json


def mostActiveYoutubeChannel(videoIDs):
    channels = {}

    for v in videoIDs:
        url = 'https://www.googleapis.com/youtube/v3/videos?part=snippet&id='+v+'&key='+DEV_KEY
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        channel = data['items'][0]['snippet']['channelTitle']
        if channel in channels:
            channels[channel] += 1
        else:
            channels[channel] = 1
    v=list(channels.values())
    k=list(channels.keys())
    s = zip(v,k)
    order = sorted(s, key=lambda x: (-x[0], x[1]))
    return order[0][1]