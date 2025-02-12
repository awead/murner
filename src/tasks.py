from celery import Celery
import os
import logging
import sys
from nrs.api import Api

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

@app.task
def call():
    logging.info('Getting facts about cats:')
    fact = Api.get_cat_fact()
    logging.info(fact)
    return fact
