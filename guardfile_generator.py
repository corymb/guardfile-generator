#!/usr/bin/env python

import os


def python():
    print 'Files predominantly Python'


def ruby():
    print 'Files predominantly Ruby'


def count_by_extension(path, extension):
    return len([y for __, __, x in os.walk(
        path) for y in x if y.endswith(extension)])
