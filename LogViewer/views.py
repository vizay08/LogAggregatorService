from django.shortcuts import render
from MessageLogger.views import ClientLogs,ClientTokens
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse

# Create your views here.
def viewer(request,email,logname):
    '''
        takes email and logname and presents a logviewer page
        for those details
    '''
    context = {
        'email':email,
        'logname':logname
    }

    return render(request,"logviewer.html",context=context)

@csrf_exempt
def logview(request):
        '''
            takes email and logname and reads last
            30 lines in the log file
        '''
        email = request.POST.get('email','')
        logname = request.POST.get('logname','')

        clienttoken = ClientTokens.objects.get(email_id=email).clienttoken
        log = ClientLogs.objects.get(clienttoken=clienttoken,logname=logname).logphysicalmap

        #open the log with the last few lines
        ret = ""
        with open(log,"r") as f:
            ret = "\n".join(f.readlines()[-30:])

        return HttpResponse(ret)