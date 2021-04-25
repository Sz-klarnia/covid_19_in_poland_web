
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .tasks import *
from apscheduler.triggers.interval import IntervalTrigger

# schedulers for updating data
def start():
    scheduler = BackgroundScheduler()
    trigger = IntervalTrigger(days=1,start_date=datetime.now()+pd.Timedelta(10,"s"))
    # checking for new data in google spreadsheet, every 60 minutes
    scheduler.add_job(check_for_new_data, "interval", minutes=60)
    # checking for new modelling data, once a day
    scheduler.add_job(get_new_modelling_data,"interval",hours=24)
    scheduler.start()

