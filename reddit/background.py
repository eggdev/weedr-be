import time
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from reddit.actions import collect_recent_reports

scheduler = BackgroundScheduler()


def initialize_background():
  # Gonna need to figure out background run cadence
    scheduler.add_job(func=collect_recent_reports,
                      trigger="interval", seconds=10)
    scheduler.start()


atexit.register(lambda: scheduler.shutdown())
