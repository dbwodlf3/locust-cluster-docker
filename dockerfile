FROM python:3.7.2

RUN pip install locust

ADD scripts /locust-cluster-docker/scripts

ENTRYPOINT ['/locust-cluster-docker/scripts/entrypoint.py']