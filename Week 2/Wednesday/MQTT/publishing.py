import random
import time
import argparse

from paho.mqtt import client as mqtt_client

my_parser = argparse.ArgumentParser(description='Send messages to the MQTT server.')

"""Params to use for testing:
broker: 192.168.101.66
port: 1883
topic = python/mqtt
username = remote
password = remote"""

my_parser.add_argument('Broker',
                       metavar='broker',
                       type=str,
                       help='MQTT broker to connect to.')
my_parser.add_argument('Port',
                       metavar='port',
                       type=int,
                       help='Port to connect to.')
my_parser.add_argument('Topic',
                       metavar='topic',
                       type=str,
                       help='Topic to publish to.')
my_parser.add_argument('Username',
                       metavar='username',
                       type=str,
                       help='Username for connection to MQTT broker.')
my_parser.add_argument('Password',
                       metavar='password',
                       type=str,
                       help='Password for connection to MQTT broker.')

args = my_parser.parse_args()

client_id = f'python-mqtt-{random.randint(0, 1000)}'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(args.Username, args.Password)
    client.on_connect = on_connect
    client.connect(args.Broker, args.Port)
    return client


def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(args.Topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{args.Topic}`")
        else:
            print(f"Failed to send message to topic {args.Topic}")
        msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()