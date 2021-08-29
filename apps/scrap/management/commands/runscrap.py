from django.core.management.base import BaseCommand
from scrap import runner


class Command(BaseCommand):
    help = "Run the scrappers"

    def handle(self, *args, **options):
        runner.run()
