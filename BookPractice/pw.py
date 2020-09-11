#!/usr/bin/env python3
# pw.py - an insecure password locker program

PASSWORDS = {'email': 'password_email',
             'system': 'password_system',
             'blog': 'password_blog',
             }

import sys
import pyperclip

if len(sys.argv) < 2:
    print('Usage: pw.py [account name] - copy password for account name to clipboard')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Done')
else:
    print('There is no password associated with '+ account)
