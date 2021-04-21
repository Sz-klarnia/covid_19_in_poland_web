from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .predictions import run_predictions
import pandas as pd
from apscheduler.triggers.interval import IntervalTrigger

def start():
    trigger = IntervalTrigger(days=1,start_date=datetime.now()+pd.Timedelta(10,"s"))
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_predictions,"interval", days=1)
    scheduler.start()
