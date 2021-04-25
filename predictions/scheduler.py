from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .predictions import run_predictions
import pandas as pd
from apscheduler.triggers.interval import IntervalTrigger

# Scheduler for running predictions. Updated daily, started minutes after deploying to start after 
# job get_new_modelling_data from scheduled tasks finishes
def start():
    trigger = IntervalTrigger(days=1,start_date=datetime.now()+pd.Timedelta(5,"m"))
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_predictions,"interval", days=1)
    scheduler.start()
