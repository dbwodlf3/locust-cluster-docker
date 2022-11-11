FROM python:3.11

RUN pip install locust

ADD scripts /locust-cluster/scripts
