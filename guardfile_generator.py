#!/usr/bin/env python

import os
from functools import partial

GUARDFILE = 'Guardfile'


class Python(object):
    """
    Infer from pip what packages are present.
    """
    string_list = {
        'django': '`python manage.py test`',
        'pytest': '`py.test --color=yes -s path/to/specific/test`',
        'default': '`python setup.py test`'
    }

    def get_guard_string(self):
        packages = self.run_pip_freeze()
        if 'django' in packages:
            return self.string_list.get('django')
        elif 'pytest' in packages:
            return self.string_list.get('pytest')
        else:
            return self.string_list.get('default')

    def run_pip_freeze(self):
        try:
            import pip
        except ImportError:
            pass
        else:
            return {i.key for i in pip.get_installed_distributions()}


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


def output():
    print('Guardfile will generate based on your current venv...')


def handler(language):
    print('Working with a %s project') % language
    if language == 'python':
        handler = Python()
    if language == 'ruby':
        handler = Ruby()
    print handler.get_guard_string()

if __name__ == '__main__':
    count = partial(count_by_extension, '.')
    handler('ruby') if count('*.rb') > count('*.py') else handler('python')
