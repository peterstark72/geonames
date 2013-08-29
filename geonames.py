#!/usr/bin/env python
# -*- coding: utf-8 -*-


import urllib2
import urllib
import json
import csv


USERNAME = "pstark"

GEONAMES_SEARCH_URL = u"http://api.geonames.org/searchJSON"




def get_latlng(name):

    params = {
        'formatted': 'true',
        'name': name,
        'maxRows':10,
        'lang': 'en',
        'username':USERNAME
    }


    url = GEONAMES_SEARCH_URL + "?" + urllib.urlencode(params)

    try:
        response = urllib2.urlopen(url)
        result = json.load(response)
    except Exception as e:
        print "Could not search {} : {}".format(name, e.message)
        return None

    geonames = result['geonames']

    if len(geonames) > 0:
        return geonames[0]['lat'], geonames[0]['lng'] 

    return None


def readarenas():

    f = open('arena_view.csv', 'rb')

    reader = csv.reader(f, escapechar='\\')
    reader.next()
    
    for row in reader:
        yield row




if __name__ == '__main__':

    writer = csv.writer(open("arena_latlng.csv", "w"))

    writer.writerow(["arena", "lat", "lng"])

    for arena in readarenas():
        coords = get_latlng(arena[2])
        if coords:
            print writer.writerow([arena[0],coords[0], coords[1]])

       







