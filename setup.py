#! /usr/bin/env python

import sys
try:
    from setuptools import setup
    have_setuptools = True
except ImportError:
    from distutils.core import setup
    have_setuptools = False

if sys.version_info[0] >= 3:
    import warnings
    warnings.warn("bipython might not work in Python 3, I'll get to it soon")

VERSION = "0.1"

setup_kwargs = {
    "version": VERSION + '.0',
    "description": 'bipython: boldly indiscriminate python interpreter',
    "author": 'Paul Ivanov',
    "author_email": 'pi@berkeley.edu',
    "url": 'http://bipython.org/',
    "download_url": "https://github.com/ivanov/bipython/zipball/" + VERSION,
    "classifiers": [
        "License :: OSI Approved :: BSD License",
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Interpreters",
        "Topic :: Utilities",
        ],
    "zip_safe": False,
    "data_files": [("", ['LICENSE', 'README.md']),],
    }

if have_setuptools:
    setup_kwargs['install_requires'] = [
        'Pygments >= 1.6',
        'urwid >= 1.1.1',
        'bpython >= 0.12',
        'ipython >= 0.12',
        ]

if __name__ == '__main__':
    with open('README.md') as f:
        descr = f.read()
    descr = descr[:descr.find('TODO')]
    setup(
        name='bipython',
        py_modules=['bipython'],
        entry_points={'console_scripts': ['bipython = bipython:main',],},
        long_description=descr,
        **setup_kwargs
        )
