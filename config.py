from __future__ import absolute_import
from kombu import Queue,Exchange
from datetime import timedelta

CELERY_TASK_RESULT_EXPIRES=3600
CELERY_TASK_SERIALIZER='json'
CELERY_RESULT_SERIALIZER='json'
CELERY_ACCEPT_CONTENT = ['json','pickle','msgpack','yaml']

CELERY_DEFAULT_EXCHANGE = 'train'
# exchange type可以看RabbitMQ中的相关内容
CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'

CELERT_QUEUES =  (
  Queue('train',exchange='train',routing_key='train'),
)
