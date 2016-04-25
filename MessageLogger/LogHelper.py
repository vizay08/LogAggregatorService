import datetime

LOG_LEVELS = ['debug','info','error','system','warning']

def write_to_logfile(logfilename,loglevel,message):
    '''
    creates the log or appends message to the log file
    :param logfilename: filename of the logfile that is to be saved in the filesystem
    :param loglevel: loglevel of the message
    :param message: message in the log
    '''
    if loglevel.lower() in LOG_LEVELS:
        loglevel = loglevel.upper()
    else:
        loglevel = "OTHER"
    with open(logfilename,"a") as f:
        f.write(datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S") + " ["+loglevel+"] "+message+"\n")