from __future__ import unicode_literals

from django.db import models

class CPUStatistics(models.Model):
    timestamp = models.IntegerField()
    cpupercent = models.IntegerField()
    memoryusage = models.IntegerField()
    ioreadusage = models.IntegerField()
    iowriteusage = models.IntegerField()

