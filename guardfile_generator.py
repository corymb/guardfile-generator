#!/usr/bin/env python

import os
from functools import partial
from glob import glob


def python():
    print 'Files predominantly Python'


def ruby():
    print 'Files predominantly Ruby'


def _count_by_extension(path, extension):
    return len([y for x in os.walk(path) for y in glob(
        os.path.join(x[0], extension))])
count = partial(_count_by_extension, '.')

ruby() if count('*.rb') > count('*.py') else python()
