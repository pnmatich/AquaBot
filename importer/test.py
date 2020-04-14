#!/usr/bin/python3

from time import sleep, time
from influxdb import InfluxDBClient
from boto3.dynamodb.conditions import Key, Attr
from boto3 import resource as boto3r
from datetime import datetime

# Create dynamodb table resource
print("INFO: creating dynamodb client")
dynamodb = boto3r('dynamodb')
dynamodb_table = dynamodb.Table('AquaBotData')

print("INFO: creating influxdb client")
# Create influxdb resource
influxdb_client = InfluxDBClient(host='localhost', port=8086)
influxdb_client.create_database('telegraf')
influxdb_client.switch_database('telegraf')

# Set initial time variables before start of loop
print("INFO: beginning import loop")
last_timestamp=0
start_time=time()

while True:
    datetime_top_of_loop=str (datetime.now().replace(microsecond=0))
    start_time_loop=time()

    # Query dynamodb for new points
    response = dynamodb_table.query(
        KeyConditionExpression=Key('id').eq('aquabot-data') & Key('timestamp').gt(last_timestamp),
        ReturnConsumedCapacity='INDEXES',
        Limit=5000,
    )

    # write points to influxdb if more than zero points were returned from dynamodb
    if response['Count'] > 0:
        payloads = [item["payload"] for item in response['Items']]
        last_timestamp = int(response['Items'][-1]['timestamp'])
        influxdb_client.write_points(payloads,protocol='json')

    print(
            'INFO: '
            + datetime_top_of_loop + ' - '
            + 'new: "' + str(response['Count']) + '", '
            + 'scanned: "' + str(response['ScannedCount']) + '", '
            + 'rcu_used: "' + str(response['ConsumedCapacity']['CapacityUnits']) + '"'
          )

    if time() < start_time_loop + 5:
        sleep(5 - ((time() - start_time) % 5))
    else:
        start_time=time()
