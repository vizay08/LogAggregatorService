from django.contrib import admin
from . import views

# Register your models here.
admin.site.register(views.ClientLogs)
admin.site.register(views.ClientTokens)
admin.site.register(views.MessageStatistics)
admin.site.register(views.LogSummary)