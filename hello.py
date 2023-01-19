import schedule
import time

def job():
    print("I'm working...")
    time.sleep(3)
    print("done")

schedule.every(1).seconds.do(job)
time.sleep(3)
schedule.run_pending()
while True:
    for job in schedule.get_jobs():
        job.run()
        time.sleep(1)

