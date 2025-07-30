'''
This is the base configuration file.
All configuration options live here
'''

SECRET_KEY = 'ALTIUM DESIGNER LIBRARY SECRET KEY 379164825'
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1234@localhost/altium_library'
STATIC_ROOT = None

ALTIUM_SVN_URL = 'https://Xenon02/svn/database/'
ALTIUM_SVN_USER = 'Xenon02'
ALTIUM_SVN_PASS = '1234'

ALTIUM_SYM_PATH = '/SYM'
ALTIUM_FTPT_PATH = '/FTPT'

SESSION_PATH = '.sessions'

TRACK_SQLALCHEMY_MODS = False

import subprocess
print(subprocess.check_output(['svn', '--version']))
