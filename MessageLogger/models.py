from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ClientTokens(models.Model):
    clienttoken = models.CharField(max_length=6,unique=True)
    email_id = models.EmailField(unique=True)

class ClientLogs(models.Model):
    clienttoken = models.CharField(max_length=6)
    logname = models.CharField(max_length=12)
    logphysicalmap = models.CharField(max_length=30)

class MessageStatistics(models.Model):
    time = models.IntegerField()
    numrequests = models.IntegerField(default=1)

class LogSummary(models.Model):
    timestamp = models.IntegerField()
    clienttoken = models.CharField(max_length=6)
    loglevel = models.CharField(max_length=10)
    message = models.TextField()