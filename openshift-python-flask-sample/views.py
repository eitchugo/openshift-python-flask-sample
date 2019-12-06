# -*- coding: utf-8 -*-
"""
    openshift-python-flask-sample.views
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    View classes for requests through flask

    :copyright: (c) 2019 by Hugo Cisneiros.
    :license: WTFPL, see LICENSE for more details.
"""
from . import app, log
from . import __version__ as VERSION
from flask import request, jsonify
import logging
import os

@app.route('/version')
def version():
    """
    Returns the name, version and api_version of the application when
    a HTTP GET request is made.
    """
    return jsonify(
        name='openshift-python-flask-sample',
        version=VERSION
    )

@app.route('/')
def root():
    """
    Returns all the stuff this app is supposed to do
    """
    return jsonify(
        url=request.url,
        hostname=os.environ.get('HOSTNAME'),
        http_headers=dict(request.headers)
    )
