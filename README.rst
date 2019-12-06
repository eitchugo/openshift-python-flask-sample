Introduction
============

An example on using Python+Flask in OpenShift.

Running locally
===============

Create a virtualenv, install dependencies and run::

    cd openshift-python-flask-sample
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt
    FLASK_APP=openshift-python-flask-sample flask run

Running on OpenShift
====================

Just do this::

    oc new-app https://github.com/eitchugo/openshift-python-flask-sample --name=opfs
    oc expose svc/opfs

This will build the image using s2i, expose to the router and you can access
the URL.

