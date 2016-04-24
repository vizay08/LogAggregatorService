from celery import Celery
from datetime import timedelta
from celery.task import periodic_task
from celery.schedules import crontab
from .models import CPUStatistics
import psutil
import time
# A periodic task that will run every minute (the symbol "*" means every)
@periodic_task(run_every=timedelta(seconds=60))
def db_update_statistics():
    p = psutil
    timestamp = time.time()


