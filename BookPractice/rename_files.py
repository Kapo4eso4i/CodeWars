#!/usr/bin/env python
# Rename files created by randomquiz.py script so I can  play with them around.
# Add a date to end of filenames of .txt files contained in directory.
# Usage: rename_files.py [path] . If no path given cwd will be used as path.

import os
from datetime import date
import sys
import shutil

try:
    path = sys.argv[1]
except:
    print('You give me a wrong parameter')
    path = os.getcwd()
os.chdir(path)

for file in os.listdir(path):
    if file.endswith('.txt'):
        newname = ('_' + date.today().strftime('%m-%d-%Y')+'.').join([a for a in file.split('.')])
        shutil.move(file, newname)
