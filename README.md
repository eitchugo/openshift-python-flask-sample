# openshift-python-flask-sample

An example on using Python+Flask in OpenShift.

## Running locally

Create a virtualenv, install dependencies and run:

```bash
cd openshift-python-flask-sample
python -m venv venv
source venv/bin/activate
pip install -e .
FLASK_APP=openshift-python-flask-sample flask run
```

## Running on OpenShift

Do this:

```bash
oc new-app https://github.com/eitchugo/openshift-python-flask-sample --name=opfs
oc expose svc/opfs
```

This will build the image using s2i, expose to the router and you can access
the URL.
