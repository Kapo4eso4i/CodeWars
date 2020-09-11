#!/usr/bin/env python
# Bullet point adder

import pyperclip

textdata = pyperclip.paste()
txlist = textdata.split('\n')
textdata = ['* ' + x if x else x for x in txlist]
pyperclip.copy('\n'.join(textdata))
