from pyasn1_modules.rfc1905 import max_bindings

from django.shortcuts import render
from django.http.response import HttpResponse
from MessageLogger.models import MessageStatistics,LogSummary,ClientLogs,ClientTokens
from django.db.models import Max
from django.views.decorators.csrf import csrf_exempt
from .models import CPUStatistics
import time
import psutil


def view_dashboard(request):
    loglist = ClientLogs.objects.all()
    context_obj = []
    for i in loglist:
        context_obj.append([ClientTokens.objects.get(clienttoken=i.clienttoken).email_id,i.logname])

    current_uri = request.get_raw_uri()
    context = {
        'current_uri': current_uri,
        'loglist' : context_obj
    }
    return render(request,"dashboard.html",context=context)

@csrf_exempt
def cpustatistics(request):
    if request.method == 'GET':
        return HttpResponse('[[0],[0],[0]]')
    elif request.method == 'POST':
        numSeconds = request.POST.get('num_seconds',5)
        numSeconds = int(numSeconds)
        if numSeconds < 5:
            numSeconds = 5
        if numSeconds > 300:
            numSeconds = 300
        cpul = []
        ml = []
        ir = []
        iw = []

        L = [0 for _ in xrange(numSeconds)]
        ls = CPUStatistics.objects.all()
        if ls:
            max_value = int(time.time())#ls.aggregate(Max('timestamp'))['timestamp__max']

            ls = CPUStatistics.objects.filter(timestamp__gte = max_value - numSeconds)
            print len(ls)
            for i in ls:
                try:
                    cpul.append(i.cpupercent)
                    ml.append(i.memoryusage)
                    ir.append(i.ioreadusage)
                    iw.append(i.iowriteusage)
                except:
                    print "going to exception blah blah"
        cpul.reverse()
        ml.reverse()
        ir.reverse()
        iw.reverse()
        CLO = []
        MLO = []
        IRO = []
        IWO = []
        L.reverse()

        #can use list comprehensions
        for i in range(numSeconds):
            try:
                CLO.append([i,cpul[i]])
            except:
                pass
            try:
                MLO.append([i,ml[i]])
            except:
                pass
            try:
                IRO.append([i,ir[i]])
            except:
                pass
            try:
                IWO.append([i,iw[i]])
            except:
                pass


        opt = str([CLO,MLO,IRO,IWO])
        print opt
        return HttpResponse(opt)

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
                try:
                    L[max_value - i.timestamp] += 1
                except:
                    pass
        LO = []
        L.reverse()
        for i in range(numSeconds):
            LO.append([i,L[i]])


        return HttpResponse(str(LO)) #("[" +  ",".join(map(str,LO)) + "]")






