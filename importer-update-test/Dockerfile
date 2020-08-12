FROM python:latest

RUN pip install influxdb
RUN pip install boto3
RUN pip install influxdb_client

COPY entrypoint.py /

CMD ["python","-u","/entrypoint.py"]
