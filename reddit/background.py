import time
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from reddit.actions import main

scheduler = BackgroundScheduler()


def initialize_background():
    scheduler.add_job(
        func=main,
        trigger="interval",
        minutes=5
    )
    scheduler.start()


atexit.register(lambda: scheduler.shutdown())
