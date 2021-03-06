"""LogAggregatorService URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url,include
from django.contrib import admin
import MessageLogger
import Dashboard
from Dashboard.CPUDetailsUpdateTask import startupdatethread
from LogViewer import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include("Dashboard.urls")),                                                    #<url>/
    url(r'^log/',MessageLogger.views.put_in_log,name="put_in_log"),                         #<url>/log/
    url(r'^message_chart/',Dashboard.views.messageincomingstatistics,name="message_chart"), #<url>/message_chart/
    url(r'^logview/',views.logview,name='logview'),                                         #<url>/logview/
    url(r'^cpu_chart/',Dashboard.views.cpustatistics,name='cpustatics'),                    #<url>/cpu_chart/
    url(r'^(?P<email>.+)/(?P<logname>.+)/$',views.viewer,name='logviewer'),                 #<url>/email/logname/
]

#starts the db update task
#TODO if blocks use threading -- Done
startupdatethread()