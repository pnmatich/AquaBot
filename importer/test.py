#!/usr/bin/python3

import pprint
from time import sleep, time
from influxdb import InfluxDBClient
from boto3.dynamodb.conditions import Key, Attr
from boto3 import resource as boto3r
from datetime import datetime

pp = pprint.PrettyPrinter(indent=2)

# Create dynamodb table resource
dynamodb = boto3r('dynamodb')
dynamodb_table = dynamodb.Table('AquaBotData')

# Create influxdb resource
influxdb_client = InfluxDBClient(host='localhost', port=8086)
influxdb_client.create_database('AquaBot')
influxdb_client.switch_database('AquaBot')

last_timestamp=0
start_time=time()

while True:
    datetime_top_of_loop=str (datetime.now().replace(microsecond=0))
    # Query dynamodb and parse the results
    response = dynamodb_table.query(
        KeyConditionExpression=Key('id').eq('aquabot-data') & Key('timestamp').gt(last_timestamp),
        ReturnConsumedCapacity='INDEXES',
        Limit=5000,
    )

    # pp.pprint({x: response[x] for x in response if x in {"ScannedCount","ConsumedCapacity","Count"}})

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

    sleep(5 - ((time() - start_time) % 5))
