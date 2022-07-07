"""Publisher and subscriber for an MQTT broker, which run async.
How to run on command line:
'python pub_and_sub.py 192.168.101.66 1883 python/mqtt remote remote'
"""
import random
import argparse
import asyncio

from paho.mqtt import client as mqtt_client

my_parser = argparse.ArgumentParser(description='Send and receive messages to the MQTT server.')

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

def connect_mqtt(name, id) -> mqtt_client:
    """Connect to the MQTT broker with a certain ID. Name is a string only used for the on_connect function
    for a print statement."""
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print(f"{name} got connected to MQTT Broker with id {id}!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(id)
    client.username_pw_set(args.Username, args.Password)
    client.on_connect = on_connect
    client.connect(args.Broker, args.Port)
    return client


async def publish(client):
    """Used to publish messages to the MQTT broker."""
    msg_count = 0
    while True:
        await asyncio.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(args.Topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{args.Topic}`")
        else:
            print(f"Failed to send message to topic {args.Topic}")
        msg_count += 1


async def subscribe(client: mqtt_client):
    """Used to set some variables for the subscriber client, then loops infinitely as a subscriber to the MQTT broker."""
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(args.Topic)
    client.on_message = on_message
    while True:
        await asyncio.sleep(1)


def run():
    # Create a new event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # Generate ids for the publisher and subscriber
    pub_id = f'python-mqtt-{random.randint(0, 1000)}'
    sub_id = f'python-mqtt-{random.randint(0, 100)}'

    # Setup for publisher
    pub = connect_mqtt('Publisher', pub_id)
    pub.loop_start()

    # Setup for subscriber
    sub = connect_mqtt('Subscriber', sub_id)
    sub.loop_start()

    # Create async tasks for subscriber and publisher
    loop.create_task(publish(pub))
    loop.create_task(subscribe(sub))
    # Run the asyncio event loop
    loop.run_forever()


if __name__ == '__main__':
    run()