#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import urllib
import json

GEONAMES_SEARCH_URL = u"http://api.geonames.org/searchJSON"


class ServiceException(Exception):
    """Exception raised on connection error."""

    def __init__(self, url):
        self.url = url

    def __str__(self):
        return "Could not load {}".format(self.url)


def search(**params):
    '''See list of parameters at http://www.geonames.org/export/geonames-search.html'''

    url = GEONAMES_SEARCH_URL + "?" + urllib.urlencode(params)

    try:
        response = urllib2.urlopen(url)
    except:
        raise ServiceException(url)

    return json.load(response)










