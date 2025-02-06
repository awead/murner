from celery import Celery
import os
import logging

rabbitmq_host = os.getenv("RABBITMQ_HOST", "localhost")
rabbitmq_queue = os.getenv("RABBITMQ_QUEUE", "task_queue")
logger = logging.getLogger('tasker')

# app = Celery()
# app.config_from_object('celeryconfig')

app = Celery(
    'tasks',
    backend='rpc://',
    broker=f'pyamqp://guest@{rabbitmq_host}//'
)

@app.task
def smoke():
    logger.info('Inside the nvim session')
    return 'n/a'
