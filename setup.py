#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='mingus_bootstrap_theme',
      version='0.1',
      packages=find_packages(),
      package_data={'mingus_bootstrap_theme': ['bin/*.*', 'static/*.*', 'templates/*.*']},
      exclude_package_data={'mingus_bootstrap_theme': ['bin/*.pyc']},
      scripts=['mingus_bootstrap_theme/manage.py'])
