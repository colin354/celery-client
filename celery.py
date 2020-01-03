from __future__ import absolute_import
from celery import Celery,platforms
CELERY_IMPORTS = ("celery1.tasks", )
platforms.C_FORCE_ROOT = True
app = Celery('myapp',
             # 此处涉及到RabbitMQ的知识，RabbitMQ是对应主节点上的
             broker='amqp://colin:123456@172.16.3.115:5672/testhost',
             backend='amqp://colin:123456@172.16.3.115:5672/testhost',
             include=['celery1.tasks'])

app.config_from_object('celery1.config')

if __name__ == '__main__':
  app.start()
