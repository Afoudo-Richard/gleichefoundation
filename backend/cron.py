from unicodedata import name
from .models import *


def my_cron_job():
    sponsor = Sponsor.objects.create(name="ArcTech")
    sponsor.save()
