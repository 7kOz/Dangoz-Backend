"""
Django Command To Wait For The Database To Be Available
"""

import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django comman to wait for database"""

    def handle(self, *args, **options):
        """Entrypoint for command"""
        self.stdout.write('Waitng for db...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Db Unavailable, waiting 1 sec...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Db available!'))
