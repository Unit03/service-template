#!/usr/bin/env python

from distutils.core import setup

_testing_libs = [
    'pytest-tornado',
    'mock',
]

setup(name='template',
      version='0.1.0',
      description='Growbots app template',
      install_requires=[
          'requests',
          'tornado',
      ],
      extras_require={
          'dev': [
              'ipython',
          ] + _testing_libs,
          'ci': [
               'coverage'
          ] + _testing_libs,
      },
      )
