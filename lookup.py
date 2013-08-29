#!/usr/bin/env python

import csv
import os
import sys


import geonames


GEONAMES_USERNAME = os.environ['GEONAMES_USERNAME']


def get_latlng(q_arg):

    result = geonames.search(q=q_arg, username=GEONAMES_USERNAME)

    matches = result.get('geonames', [])

    if len(matches) > 0:
        return matches[0]['lat'], matches[0]['lng'] 

    return None



def main():

    if len(sys.argv) < 2:
        exit("Missing argument.")

    reader = csv.reader(open(sys.argv[1]))
    writer = csv.writer(sys.stdout)

    for r in reader:
        coords = get_latlng(r[0])
        if coords:
            row = [r[0], coords[0], coords[1]]
            writer.writerow(row)



if __name__ == '__main__':
    main()


       