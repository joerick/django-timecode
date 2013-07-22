#!/bin/sh

django-admin.py test --pythonpath=. --settings=timecode.test.settings
