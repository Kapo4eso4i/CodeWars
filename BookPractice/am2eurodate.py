#!/usr/bin/env python

import re
import os
import sys
import shutil

amDate = re.compile(r'''
                    ^(.*?) # all text before date if exists
                    ([01]?\d)-  #month
                    ([0123]?\d)- #date
                    (19|20\d\d) # year
                    (.*?)$ #all that remains 
                    ''', re.VERBOSE)

try:
    workingFolder = sys.argv[1]
except:
    workingFolder = os.getcwd()

for file in os.listdir(workingFolder):
    if re.search(amDate, file):
#       print(re.sub(amDate, r'\1\3*\2-\4\5', file))
#       print(workingFolder)
        shutil.move(os.path.join(workingFolder, file), os.path.join(workingFolder, re.sub(amDate, r'\1_\3-\2-\4\5', file)))
