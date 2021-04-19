from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .predictions import *
from apscheduler.triggers.interval import IntervalTrigger

def start():
    trigger = IntervalTrigger(days=1,start_date=datetime.now())
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_predictions,trigger, days=1)