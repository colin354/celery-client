from __future__ import absolute_import
from celery1.celery import app

import time
from celery import task


@task(name='apps.users.tasks.do_train')
def do_train(x, y):
    """
    训练
    :param data:
    :return:
    """
    time.sleep(10)
    return dict(data=str(x+y),msg="train")
