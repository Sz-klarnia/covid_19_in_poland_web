
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .tasks import *

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_for_new_data, 'interval', minutes=60)
    scheduler.add_job(get_new_modelling_data,'interval',hours=24)
    scheduler.start()