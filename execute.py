from apscheduler.schedulers.background import BackgroundScheduler
import scheduler_jobs

scheduler = BackgroundScheduler()


scheduler.add_job(scheduler_jobs.refill_shop, 'interval', seconds=100)
scheduler.start()