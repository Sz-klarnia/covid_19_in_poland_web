
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .tasks import *
from apscheduler.triggers.interval import IntervalTrigger


def start():
    scheduler = BackgroundScheduler()
    trigger = IntervalTrigger(days=1,start_date=datetime.now()+pd.Timedelta(10,"s"))
    scheduler.add_job(check_for_new_data, trigger, minutes=60)
    scheduler.add_job(get_new_modelling_data,'interval',hours=24)
    scheduler.start()

