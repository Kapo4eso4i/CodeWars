#!/usr/bin/env python

import os
import sys

folder = '/home/andrew/TestFolder'
print(folder)

for foldername, folders, files in os.walk(folder):
    print(foldername)
    for file in files:
        print(os.path.join(os.path.basename(foldername), file))
#    print(step)