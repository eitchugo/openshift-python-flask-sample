FROM python:3.12

WORKDIR /app
COPY . /app

RUN pip install -e .

EXPOSE 5000

ENV FLASK_APP=openshift-python-flask-sample
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
