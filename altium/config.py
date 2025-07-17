'''
This is the base configuration file.
All configuration options live here
'''

SECRET_KEY = 'ALTIUM DESIGNER LIBRARY SECRET KEY 379164825'
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/altium_lib'
STATIC_ROOT = None

ALTIUM_SVN_URL = 'https://LAPTOP-0FDRGRER/svn/altium_lib/'
ALTIUM_SVN_USER = 'M'
ALTIUM_SVN_PASS = 'xd'

ALTIUM_SYM_PATH = '/symbol'
ALTIUM_FTPT_PATH = '/footprint'

SESSION_PATH = '.sessions'

TRACK_SQLALCHEMY_MODS = False

import subprocess
print(subprocess.check_output(['svn', '--version']))
