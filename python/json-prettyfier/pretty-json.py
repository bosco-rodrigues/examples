# coding=utf8

# TODO : add header to this document
# TODO : make it such that you could just pipe some text in and then pretty print output.

import sys
import json
import pprint

filename = sys.argv[1]

with open (filename, 'r') as json_data:
    x = json.load(json_data)
    pprint.pprint(x)
