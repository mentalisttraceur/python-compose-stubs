#!/usr/bin/env python

import errno
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


project_directory = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(project_directory, 'README.rst')

with open(readme_path) as readme_file:
    long_description = readme_file.read()


setup(
    name='compose-stubs',
    version='0.0.6',
    description='Type stubs for compose',
    long_description=long_description,
    license='0BSD',
    url='https://github.com/mentalisttraceur/python-compose-stubs',
    author='Alexander Kozhevnikov',
    author_email='mentalisttraceur@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    packages=["compose-stubs"],
    package_data={'compose-stubs': ['__init__.pyi', 'compose.pyi']},
)
