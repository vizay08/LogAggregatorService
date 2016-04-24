import datetime

LOG_LEVELS = ['debug','info','error','system','warning']

def write_to_logfile(logfilename,loglevel,message):
    if loglevel.lower() in LOG_LEVELS:
        loglevel = loglevel.upper()
    else:
        loglevel = "OTHER"
    with open(logfilename,"a") as f:
        f.write(datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S") + " ["+loglevel+"] "+message+"\n")