FROM python:latest

RUN pip install influxdb
RUN pip install boto3

COPY entrypoint.py /

CMD ["python","-u","/entrypoint.py"]
