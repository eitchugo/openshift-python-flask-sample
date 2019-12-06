# -*- coding: utf-8 -*-
"""
    openshift-python-flask-sample.config
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Configuration defaults

    :copyright: (c) 2019 by Hugo Cisneiros.
    :license: WTFPL, see LICENSE for more details.
"""
import os
basedir = os.getcwd()

class OPFSDefaultConfig(object):
  CONF_FILE = os.environ.get('CONF', 'opfs.conf')
  SERVER_LISTEN = '0.0.0.0'
  SERVER_PORT = 8000
  DEBUG = False
  TESTING = False
  USE_RELOADER = False
  LOGGER_NAME = 'opfsLogger'
  LOG_LEVEL = 'INFO'
  JSONIFY_PRETTYPRINT_REGULAR = True
