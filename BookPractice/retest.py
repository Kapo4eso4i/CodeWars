#!/usr/bin/env python

import re

patt = re.compile(r'''(.*?)# begining
                      ([01]?\d)-# month
                      ([0-3]?\d)-#day
                      (19|20\d\d)#year
                      (.*?)$#ending
                      ''', re.VERBOSE)

text = 'capitals_quiz_000209-21-2020.txt'

print(re.sub(patt, r'\1_\3-\2-\4\5', text))
print(text)
for group in re.match(patt, text).groups():
    print(group)
