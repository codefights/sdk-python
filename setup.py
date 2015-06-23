#!/usr/bin/env python

from distutils.core import setup

setup(name='codefights',
      version='1.0',
      description='Codefights.net SDK for Python developers',
      author='Gytis Talocka',
      author_email='kurideja@gmail.com',
      packages=['codefights', 'codefights.boilerplate', 'codefights.boilerplate.server', 'codefights.model', 'codefights.samples'],
      )
