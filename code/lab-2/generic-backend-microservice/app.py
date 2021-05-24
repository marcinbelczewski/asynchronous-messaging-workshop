import json
import os
import random
import time

SERVICE_NAME = os.environ["SERVICE_NAME"]


def process(event):
    print("{} process: {}".format(SERVICE_NAME, event))
    message_id = event["id"]

    # will fail randomly to show the Amazon SNS redelivery feature
    if random.choice([True, False]):
        print("--------------------------------------")
        print("{{'msg-id': '{}', 'status': 'FAILED'}}".format(message_id))
        print("--------------------------------------")
        raise Exception("I'm failing randomly...")

    print("+++++++++++++++++++++++++++++++++++++++++")
    print("{{'msg-id': '{}', 'status': 'PROCESSED'}}".format(message_id))
    print("+++++++++++++++++++++++++++++++++++++++++")


def lambda_handler(event, context):
    print("{} received event: {}".format(SERVICE_NAME, json.dumps(event)))

    # we set the 'BatchSize' to 1
    # raw message delivery is disabled hence the actual message is buried in body/Message
    request_body = request_body = json.loads(json.loads(event["Records"][0]["body"])["Message"])
    process(request_body)
