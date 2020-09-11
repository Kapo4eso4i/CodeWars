#!/usr/bin/env python
#Extract popular baby names from html file

import re

file = open('/home/andrew/Downloads/Top names of the 2010s.html', "r")
text = file.read()
##print(text)
pattern = re.compile(r'<td>([\w,]+)</td>')

matches = pattern.finditer(text)
for match in matches:
    print(match.group(1))
