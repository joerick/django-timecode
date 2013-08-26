#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='django-timecode',
    version='0.1.4',
    description='Provides classes for working with timecodes (as used in the video industry).',
    long_description=open('README.md').read(),
    author='Joe Rickerby',
    author_email='joerick@mac.com',
    url='http://github.com/joerick/django-timecode/',
    packages=[
        'timecode',
        'timecode.test',
    ],
    license='LICENSE.txt',
    install_requires=[
        "Django >= 1.5",
    ]
)
