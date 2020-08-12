#!/usr/local/bin/python

import influxdb
from time import sleep, time
from influxdb import InfluxDBClient
from boto3.dynamodb.conditions import Key, Attr
from boto3 import resource as boto3r
from datetime import datetime

# Create dynamodb table resource
print("INFO: creating dynamodb client")
dynamodb = boto3r('dynamodb')
dynamodb_table = dynamodb.Table('AquaBotData')

print("INFO: creating influxdb sensors client")
# Create influxdb resource
influxdb_client = InfluxDBClient(host='influxdb', port=8086)
influxdb_client.create_database('telegraf')
influxdb_client.switch_database('telegraf')
bucket = f'telegraf/sensor_readings'

print("INFO: creating influxdb last_sort_key client")
# Create influxdb resource
influxdb_client_last_sort_key = InfluxDBClient(host='influxdb', port=8086)
influxdb_client_last_sort_key.create_database('last_sort_key')
influxdb_client_last_sort_key.switch_database('last_sort_key')

# Set initial time variables before start of loop
print("INFO: determining last timestamp")
last_timestamp=0

tables = influxdb_client.query('SELECT last("temperature") FROM "sensor_readings";')


print("INFO: printing bucket contents")
print(list(tables.get_points())[0]["time"]
print(time())


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
print(last_timestamp)


# print("INFO: beginning import loop")
# start_time=time()
#
# while True:
#     datetime_top_of_loop=str (datetime.now().replace(microsecond=0))
#     start_time_loop=time()
#
#     # Query dynamodb for new points
#     response = dynamodb_table.query(
#         KeyConditionExpression=Key('id').eq('aquabot-data') & Key('timestamp').gt(last_timestamp),
#         ReturnConsumedCapacity='INDEXES',
#         Limit=5000,
#     )
#
#     # write points to influxdb if more than zero points were returned from dynamodb
#     if response['Count'] > 0:
#         payloads = [item["payload"] for item in response['Items']]
#         last_timestamp = int(response['Items'][-1]['timestamp'])
#         influxdb_client.write_points(payloads,protocol='json')
#
#     print(
#             'INFO: '
#             + datetime_top_of_loop + ' - '
#             + 'new: "' + str(response['Count']) + '", '
#             + 'scanned: "' + str(response['ScannedCount']) + '", '
#             + 'rcu_used: "' + str(response['ConsumedCapacity']['CapacityUnits']) + '"'
#           )
#
#     if time() < start_time_loop + 5:
#         sleep(5 - (time() - start_time_loop))
