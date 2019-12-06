# -*- coding: utf-8 -*-
"""
    openshift-python-flask-sample
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    An example on using Python+Flask in OpenShift.

    :copyright: (c) 2019 by Hugo Cisneiros.
    :license: WTFPL, see LICENSE for more details.
"""
from . import config
from flask import Flask
import logging
import logging.config
import sys
import os

# version info
__version__ = '1.0'

# instantiate the application and api
app = Flask(__name__)

# setup logging
log = logging.getLogger("opfsLogger")
log.setLevel(logging.INFO)
log_ch = logging.StreamHandler(sys.stdout)
log_ch.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
log.addHandler(log_ch)

# greetings!
log.info("openshift-python-flask-sample version %s." % __version__)

# load configurations from defaults
log.info("Loading configuration defaults.")
config = config.OPFSDefaultConfig
app.config.from_object(config)

# load configuration from file if it exists
if os.path.isfile(app.config['CONF_FILE']):
    log.info("Loading configuration from file %s." % app.config['CONF_FILE'])
    app.config.from_pyfile(app.config['CONF_FILE'])

# change log level if needed
try:
    log.setLevel(app.config['LOG_LEVEL'])
except ValueError:
    log.warn("Invalid log level on configuration. Using default value (INFO).")
    log.setLevel(logging.INFO)

# load our views
log.debug("Importing views.")
from . import views

# ready
log.info("Ready to serve requests.")
