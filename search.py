#!/usr/bin/env python
import os
def searchs():
    abs_path = os.path.abspath('.')
    for absdir,subdirs,files in os.walk(abs_path):
        print files
        for f in files:
            print os.path.join(absdir,f)
searchs()
