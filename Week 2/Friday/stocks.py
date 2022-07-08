# This program uses the interpreter on my raspberry pi
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import random, time
from datetime import datetime

client = InfluxDBClient(url='http://127.0.0.1:8086',token="<my-token>", org="telegraf")
write_api = client.write_api(write_options=SYNCHRONOUS)
bucket = "telegraf"
stocks = ['Apple', 'Amazon', 'Philips', 'LG']
i = 0
while True:
    for item in stocks:
        r1 = round(random.uniform(00.00, 200.00), 2)
        p = Point("Stock Price").tag("company", item).field("price", r1)
        write_api.write(bucket=bucket, record=p)
    print(f'Iteration {i}')
    i += 1
    time.sleep(5)

