import random

import argparse

from paho.mqtt import client as mqtt_client

my_parser = argparse.ArgumentParser(description='Receive messages from the MQTT server.')

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

client_id = f'python-mqtt-{random.randint(0, 100)}'


def connect_mqtt() -> mqtt_client:
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


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(args.Topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()