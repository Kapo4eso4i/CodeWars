#!/usr/bin/env python
#Just a random exercise from Stack Overflow

import re
sentences = []                                                   #empty list for storing result
with open('testtext.txt') as fileObj:
    lines = [line.strip() for line in fileObj if line.strip()]   #makin list of lines allready striped from '\n's
for line in lines:
    sentences += re.split(';', line)                             #spliting lines by ';' and store result in sentences
for sentence in sentences:
    print(sentence +' ' + str(len(sentence.split())))            #out
