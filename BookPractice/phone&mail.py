#!/usr/bin/env python
# extract phone numbers and e-mails from text copied to clipboard

import pyperclip
import re

#TODO: create regexp for phone numbers

regphones = re.compile(r'''(
(\d{3}|\(\d{3}\))? #area code
(\s|-|\.) #separator
(\d{3}) #first 3  digits
(\s|-|\.) #separator again
(\d{4}) #last 4 digits of phone number
(\s*(ext|x|ext.)\s*(\d{2,5}))? # optional extention
)''', re.VERBOSE)

#TODO: CREATE REGEXP FOR E-MAILS

regmails = re.compile(r'''(
[a-zA-Z0-9._%+-]+ #username
@ # @ sign
[a-zA-Z0-9.-]+ #domain name
(\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

#TODO: COPY TEXT FROM CLIPBOARD

textdata = str(pyperclip.paste())

#TODO: DO SOME MAGIK

matches = []

for groups in regphones.findall(textdata):
    matches.append(groups[0])

for groups in regmails.findall(textdata):
    matches.append(groups[0])

textdata = '\n '.join(matches)

#TODO: COPY RESULT INTO CLIPBOARD

pyperclip.copy(textdata)

#THE END