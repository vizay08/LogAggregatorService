from django.shortcuts import render
from django.http import request,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ClientTokens,ClientLogs,MessageStatistics,LogSummary
from LogAggregatorService import settings
import json
import LogHelper
import time

starttime = -1
endtime = -1

#changed the design, won't be used
def messagecount():
    '''
        Not following this method
        This counts the requests in the same second
    '''
    global starttime,endtime
    if starttime == -1:
        starttime = int(time.time())
    if endtime == -1:
        endtime = starttime
    else:
        endtime = int(time.time())

    try:

        ms = MessageStatistics.objects.get(time=endtime)
        #print "saving already existing one"
        t = ms.numrequests
        ms.numrequests = t+1

        ms.save()
    except MessageStatistics.DoesNotExist:
        ms = MessageStatistics(time=endtime)
        #print "creating new one"
        ms.save()

# Create your views here.
@csrf_exempt
def put_in_log(request):
    '''
        reason for api to put the data into the logfile
        returns OK if on successful execution
        returns NOK if failure
    '''
    timestamp = int(time.time())
    ret = ""
    j = None
    try:
        s = request.body



        client_token = request.POST.get('client_token','')
        log_name = request.POST.get('log_name','')
        message = request.POST.get('message','')
        log_level = request.POST.get('log_level','')

        #print "post data",client_token,log_level,log_name,message

        try:
                c = ClientTokens.objects.get(clienttoken=client_token)
                r = ""
                try:
                    r = ClientLogs.objects.get(clienttoken=client_token,logname=log_name)
                except ClientLogs.DoesNotExist:
                    filename = client_token+log_name
                    r = ClientLogs(clienttoken=client_token,logname=log_name,logphysicalmap=filename)
                    r.save()
                absfilepath = settings.BASE_DIR+'/'+r.logphysicalmap

                #saving logs into db
                ls = LogSummary(clienttoken=client_token,loglevel=log_level,message=message,timestamp=timestamp)
                ls.save()

                #save the message into the logs
                LogHelper.write_to_logfile(logfilename=absfilepath,loglevel=log_level,message=message)
                return HttpResponse("OK")


        except ClientTokens.DoesNotExist:
                return HttpResponse('NOK')

    except Exception as e:
        ret = "Exception"+str(e)

        return HttpResponse("NOK")
