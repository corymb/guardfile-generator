#!/usr/bin/env python

import os

GUARDFILE = 'Guardfile'


class Python(object):
    """
    Infer from pip what packages are present.
    """
    def run_pip_freeze(self):
        try:
            import pip
        except ImportError:
            pass
        else:
            print pip.main('freeze')


class Ruby(object):
    pass


def count_by_extension(path, extension):
    return len([y for __, __, x in os.walk(
        path) for y in x if y.endswith(extension)])


def write_guardfile(ext, command):
    with open(GUARDFILE, 'w') as guard:
        guard.write('guard :shell do\n')
        guard.write('watch /.*.rb/ do\n')
        guard.write('`rake test:integration`\n')
        guard.write('end\n')
        guard.write('end\n')
