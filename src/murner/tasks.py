import json
import logging
import os
import sys

from celery import Celery
from murner.nrs.api import Api

rabbitmq_host = os.getenv("RABBITMQ_HOST", "localhost")
rabbitmq_queue = os.getenv("RABBITMQ_QUEUE", "task_queue")
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

# app = Celery()
# app.config_from_object('celeryconfig')

app = Celery(
    'tasks',
    backend='rpc://',
    broker=f'pyamqp://guest@{rabbitmq_host}//'
)

def from_jsonl(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            json_obj = json.loads(line)  
            call.delay(json_obj)
        return "Success"

def from_json(json_obj):
    call.delay(json_obj)

@app.task
def call(data):
    logging.info("Receiving data")
    logging.info(data)
    fact = Api.get_cat_fact()
    logging.info(fact)
    return fact
