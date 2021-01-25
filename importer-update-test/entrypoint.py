#!/usr/local/bin/python

import influxdb
from time import sleep, time
from influxdb import InfluxDBClient
from boto3.dynamodb.conditions import Key, Attr
from boto3 import resource as boto3r
from datetime import datetime

sleep(5)

# Create dynamodb table resource
print("INFO: creating dynamodb client")
dynamodb = boto3r('dynamodb')
dynamodb_table = dynamodb.Table('AquaBotData')

print("INFO: creating influxdb sensors client and timestamp client")
# Create influxdb sensors resource
influxdb_client_sensors = InfluxDBClient(host='influxdb', port=8086)
influxdb_client_sensors.create_database('telegraf')
influxdb_client_sensors.switch_database('telegraf')


# Set initial time variables before start of loop
print("INFO: determining last timestamp")
last_timestamp=0
# try:
#     last_timestamp = list(influxdb_client_timestamps.query('SHOW MEASUREMENTS;').get_points(measurement='sensor_readings'))[0]
# except Exception as e:
#     print(e)


# print(influxdb_client_sensors.query('SHOW MEASUREMENTS;').get_points(measurement='sensor_readings')[0])

try:
  last_timestamp = int(list(influxdb_client_sensors.query('SELECT last(dynamodb_timestamp) FROM "sensor_readings";').get_points(measurement='sensor_readings'))[0]['last'])
except:
  print("INFO: could not set last timestamp (this might be the first time running import)")

print(last_timestamp)
print("Result: {0}".format(last_timestamp))
print("Result: {0}".format(datetime.now().replace(microsecond=0)))


# Query dynamodb for new points
# response = dynamodb_table.query(
#     KeyConditionExpression=Key('id').eq('aquabot-data') & Key('timestamp').gt(last_timestamp),
#     ReturnConsumedCapacity='INDEXES',
#     Limit=5000,
# )
# last_timestamp = int(response['Items'][-1]['timestamp'])

# print("Result: {0}".format(last_timestamp))


# print("yo2")

# write points to influxdb if more than zero points were returned from dynamodb


print("INFO: beginning import loop")
start_time=time()

while True:
    datetime_top_of_loop=str (datetime.now().replace(microsecond=0))
    start_time_loop=time()

    print(last_timestamp)

    # Query dynamodb for new points
    response = dynamodb_table.query(
        KeyConditionExpression=Key('id').eq('aquabot-data') & Key('timestamp').gt(last_timestamp),
        ReturnConsumedCapacity='INDEXES',
        Limit=5000,
    )

    # write points to influxdb tables if more than zero points were returned from dynamodb
    if response['Count'] > 0:

        items = response['Items']
        for item in items:
            item['payload']['fields'].update({'dynamodb_timestamp': item['timestamp']})

        payloads = [item["payload"] for item in response['Items']]
        last_timestamp = int(response['Items'][-1]['timestamp'])
        influxdb_client_sensors.write_points(payloads,protocol='json')

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
