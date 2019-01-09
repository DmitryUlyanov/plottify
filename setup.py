#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='imutils',
      version='0.1',
      packages=['imutils'],
      package_dir={'imutils': 'imutils'},
      install_requires = ['matplotlib', 'numpy', 'pillow'],
     )