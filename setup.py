#!/usr/bin/env python

from distutils.core import setup

setup(
    name='codefights',
    version='0.1',
    description='Codefights.net SDK for Python developers',
    author='Gytis Talocka',
    author_email='kurideja@gmail.com',
    url='https://github.com/codefights/sdk-python',
    download_url='https://github.com/codefights/sdk-python/tarball/0.1',
    packages=['codefights', 'codefights.boilerplate', 'codefights.boilerplate.server', 'codefights.model', 'codefights.samples'],
)
