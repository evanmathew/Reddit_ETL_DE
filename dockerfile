# pulling docker image
FROM apache/airflow:2.7.1-python3.10

# copyinh the requirements/package/version from local requirements.txt
COPY requirements.txt /opt/airflow/

#initialising the root user in which installing packages suhch as python3-dev
USER root
RUN apt-get update --fix-missing && \
    apt-get install -y gcc python3-dev &&\
    #apt-get install -y postgresql-client && \
    apt-get install -y netcat-openbsd && \
    apt-get install -y wget && \
    apt-get clean


#initialising the airflow user
USER airflow

#installing the requirements which are in requirements.txt inside the airflow docker image
RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt