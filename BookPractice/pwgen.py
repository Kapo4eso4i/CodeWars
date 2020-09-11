#!/usr/bin/env python
# pwgen.py - Random password generator

import string
import random
import sys
import pyperclip


# print(sys.argv)
pw = random.sample(string.ascii_letters + string.digits + string.punctuation, int(sys.argv[-1]))
pyperclip.copy(''.join(pw))
#print(''.join(pw))