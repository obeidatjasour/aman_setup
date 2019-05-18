#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import time
from time import sleep

items = list(range(0, 57))
l = len(items)


# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print ('%s |%s| %s%% %s' % (prefix, bar, percent, suffix))
    # Print New Line on Complete
    if iteration == total: 
        print()


def geterror():
    cpuserial="0000000000000000"
    try:
        f=open('/proc/cpuinfo','r')
        for line in f:
            if line[0:6]=='Serial':
                cpuserial=line[10:26]
        f.close()
    except:
        cpuserial="Error"

    return cpuserial

print ("Welcome to Perfect Vision AMAN TB Setup")
print "---------------------------------------------------------------"
time.sleep(0.5)
para1=input("Enter Device Serial Number:")
time.sleep(0.5)
print "Serial Number Assigned to this device is: ",para1


print "Assign Completed!"
print "---------------------------------------------------------------"
para2=raw_input("Enter Operator Tag (in lower case):")
time.sleep(0.5)
print "Operator Tag Assigned to this device is: ",para2.upper()
time.sleep(0.8)
print "Assign Completed!"
print "---------------------------------------------------------------"
para3="Perfect Vision TAG-Base"
time.sleep(0.5)
print "Company Code", para3
time.sleep(0.5)
print "Company Code Assigned Successfully"
print "---------------------------------------------------------------"
time.sleep(0.5)
print "Device Proximity Calibration Please wait ..."
time.sleep(1)
para4=str(geterror())
print "This device calibrated to be:",para4
time.sleep(0.5)
print "---------------------------------------------------------------"

generated='gateway_name="'+str(para3)+'"\n'+'production_tag="'+str(para4)+'"\n'+'device_name="'+str(para1)+'"\n'+'operator_r="'+str(para2.lower())+'"\n'

f = open('/home/pi/aman_project_dongel/user_settings.py', "a")
f.write(str(generated))
f.close()

# Initial call to print 0% progress
printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
for i, item in enumerate(items):
    # Do stuff...
    sleep(0.1)
    # Update Progress Bar
    printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

print "This Device is Activated & Ready Thank you"
