#!/usr/bin/env python

import os
import sys
import zipfile


def backup2zip(folder):
    # Backups the entire contents of folder - folder into .zip file
    folder = os.path.abspath(folder)
    print(folder)
    number = 1
    while True:
        zipfilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        print(zipfilename)
        if not os.path.exists(zipfilename):
            break
        number += 1
    print('Creating %s...' % (zipfilename))
    backupzipfile = zipfile.ZipFile(zipfilename, 'w')

    os.chdir(os.path.dirname(folder))

    for foldername, subfolders, files in os.walk(os.path.basename(folder)):
        print('Adding files in %s...' %(foldername))
        backupzipfile.write(foldername)
        for file in files:
            backupzipfile.write(os.path.join(foldername, file))

    backupzipfile.close()


backup2zip(sys.argv[1])
