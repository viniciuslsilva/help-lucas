from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

from taks_queue import Job

def start():
    executors = {
        'default': ThreadPoolExecutor(1),
        'processpool': ProcessPoolExecutor(1)
    }

    sched = BackgroundScheduler(timezone='UTC', executors=executors)
    sched.add_job(Job, 'interval', seconds=20)
    sched.start()
