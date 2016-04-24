from pyasn1_modules.rfc1905 import max_bindings

from django.shortcuts import render
from django.http.response import HttpResponse
from MessageLogger.models import MessageStatistics,LogSummary
from django.db.models import Max
from django.views.decorators.csrf import csrf_exempt
import time
import psutil

    
def view_dashboard(request):
    ms = MessageStatistics.objects.all().order_by('-id')[:5]
    for i in ms:
        print i.time,i.numrequests

    return render(request,"dashboard.html")


def statistics(request):
    maap = {} #not a map, its a maap

    #mesage statistics part
    ms = MessageStatistics.objects.all().order_by('-id')[:5]
    msm = {}
    msc = 5
    for i in ms:
        msm[i] = ms.numRequests
        msc -= 1

    #if num of records are less than required,fill with 0
    for i in range(msc,0,-1):
        msm[i] = 0

    #cpu statistics part

    cpu  = {i:psutil.cpu_percent(0.1) for i in xrange(1,5)}

    #memory statistics part

    memory = {i:psutil}

    return HttpResponse('ok')

@csrf_exempt
def messageincomingstatistics(request):
    if request.method == 'GET':
        return HttpResponse('[0,0]')
    elif request.method == 'POST':
        numSeconds = request.POST.get('num_seconds',5)
        numSeconds = int(numSeconds)
        if numSeconds < 5:
            numSeconds = 5
        if numSeconds > 300:
            numSeconds = 300

        L = [0 for _ in xrange(numSeconds)]
        ls = LogSummary.objects.all()
        if ls:
            max_value = int(time.time())#ls.aggregate(Max('timestamp'))['timestamp__max']

            ls = LogSummary.objects.filter(timestamp__gte = max_value - numSeconds)

            for i in ls:
                L[max_value - i.timestamp] += 1
        LO = []
        L.reverse()
        for i in range(numSeconds):
            LO.append([i,L[i]])


        return HttpResponse("[" +  ",".join(map(str,LO)) + "]")



