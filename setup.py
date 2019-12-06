#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    openshift-python-flask-sample setup script
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Setup script for packaging

    :copyright: (c) 2019 by Hugo Cisneiros.
    :license: WTFPL, see LICENSE for more details.
"""
import io
from openshift-python-flask-sample import __version__
from os.path import abspath, dirname, join

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

this_dir = abspath(dirname(__file__))
with io.open(join(this_dir, 'OVERVIEW.rst'), encoding='utf-8') as file:
    long_description = file.read()

config = {
    'name': 'openshift-python-flask-sample',
    'version': __version__,
    'description': 'An example on using Python+Flask in OpenShift',
    'long_description': long_description,
    'url': 'https://github.com/eitchugo/openshift-python-flask-sample',
    'author': 'Hugo Cisneiros',
    'author_email': 'hugo.cisneiros@gmail.com',
    'license': 'WTFPL',
    'classifiers': [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'License :: Freely Distributable',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
    'keywords': [
        'sample',
        'example'
    ],
    'packages': find_packages(exclude=['docs']),
    'include_package_data': True,
    'install_requires': [
        'Flask>=0.10',
    ],
    'entry_points': {
        'console_scripts': [
            'openshift-python-flask-sample=app.run'
        ]
    },
    'zip_safe': False
}

setup(**config)
