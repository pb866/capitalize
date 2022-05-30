#!/usr/bin/env python

from setuptools import setup
import re

# Read version from file in _version.py
VERSIONFILE="capitalize/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\']([^'\']*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))


setup(name='capitalize',
      version='0.1.0-DEV',
      # list folders, not files
      packages=['capitalize',
                'capitalize.test'],
      scripts=['capitalize/bin/cap_script.py'],
      package_data={'capitalize': ['data/cap_data.txt']},
      install_requires = ['pandas', 'holidays']
      )
