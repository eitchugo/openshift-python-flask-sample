FROM python:3.6

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=openshift-python-flask-sample
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
