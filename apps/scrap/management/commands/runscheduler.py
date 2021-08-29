from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from django.core.management.base import BaseCommand
from scrap import runner

JOB_ID = "scrap"
INTERVAL_TIME = {"hours": 1}
SCHEDULER = BlockingScheduler()


class Command(BaseCommand):
    help = f"Run the scrappers every {INTERVAL_TIME}"

    def handle(self, *args, **options):
        SCHEDULER.add_job(
            runner.run,
            "interval",
            **INTERVAL_TIME,
            id=JOB_ID,
            next_run_time=datetime.now(),
        )

        SCHEDULER.start()
