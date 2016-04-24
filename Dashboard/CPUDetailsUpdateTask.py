from .models import CPUStatistics
import time
import psutil
import thread

updateFlag = False

def updateDB():
    timestamp = time.time()
    ioreadusage = psutil.disk_io_counters().read_count
    iowriteusage = psutil.disk_io_counters().write_count
    memoryusage = psutil.used_phymem()
    cpupercent = psutil.cpu_percent()
    cpuDetails  = CPUStatistics(timestamp=timestamp,ioreadusage=ioreadusage,iowriteusage=iowriteusage,memoryusage=memoryusage,cpupercent=cpupercent)
    cpuDetails.save()

def updateEverySecond(numSeconds):
    global updateFlag

    if not updateFlag:
        updateFlag = True
        while True:
            updateDB()
            time.sleep(numSeconds)

def startupdatethread():
    print "thread called"
    thread.start_new_thread(updateEverySecond,(1,))

if __name__ == "__main__":
    updateEverySecond()