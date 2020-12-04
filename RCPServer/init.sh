#!/bin/sh

virtualenv $PWD/virtualenv

. virtualenv/bin/activate
pip install -r requiments.txt
