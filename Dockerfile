    FROM apache/airflow:2.3.4
    USER root
    RUN apt update && apt install -y \
        gcc libxml2-dev libxslt1-dev libxslt-dev python3-dev python3-lxml\
        && apt clean
    USER airflow
    COPY requirements.txt requirements.txt
    RUN pip install -r requirements.txt  --no-cache-dir
