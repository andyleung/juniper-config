#!/usr/bin/python

import sys
import re
import os
import shutil
import commands

from jnpr.junos import Device
from pprint import pprint as pp

"""Display SRX AppTrack Table
"""

def print_app_table(dev):
    """ Print the application tracking table. """
    applications = []
    bytes = []
    sessions = []
    encrypted = []
    output_file = open('output.html','w')
    dev.open()
    jj = dev.cli("show services application-identification statistics application")
    kk = jj.splitlines()
    tsize = len(kk)
    for i in range(3,tsize):
      information = kk[i].split()
      applications.append(information[0])
      sessions.append(information[1])
      bytes.append(information[2])
      encrypted.append(information[3])

## Debug ##
##    print "Application :", applications
##    print "Sessions :", sessions
##    print "Bytes :", bytes
##    print "Encrypted :", encrypted

    output_file.write("<html><body><table border=1 frame=box rules=all>\n")
    output_file.write("<tr><td>"+"Applications"+"</td><td>"+"Sessions"+"</td><td>"+"Bytes"+"</td><td>"+"Encrypted"+"</td></tr>") 
    for i in range(0, tsize-3):
        output_file.write("<tr><td>"+applications[i]+"</td><td>"+sessions[i]+"</td><td>"+bytes[i]+"</td><td>"+encrypted[i]+"</td></tr>") 
    output_file.write("</table></body></html>")
    output_file.close()

def print_appgroup_table(dev):
    """ Print the application tracking table. """
    appgroup = []
    app_sessions = []
    kbytes = []
    output_file = open('output2.html','w')
    dev.open()
    jj = dev.cli("show services application-identification statistics application-groups")
    kk = jj.splitlines()
    tsize = len(kk)
    for i in range(1,tsize):
      information = kk[i].split()
      appgroup.append(information[0])
      app_sessions.append(information[1])
      kbytes.append(information[2])

    output_file.write("<html><body><table border=1 frame=box rules=all>\n")
    output_file.write("<tr><td>"+"Application Group"+"</td><td>"+"Sessions"+"</td><td>"+"Kilo Bytes "+"</td></tr>") 
    for i in range(2, tsize-1):
        output_file.write("<tr><td>"+appgroup[i]+"</td><td>"+app_sessions[i]+"</td><td>"+kbytes[i]+"</td></tr>") 
    output_file.write("</table></body></html>")
    output_file.close()


def main():
    args = sys.argv[1:]
    if not args:
       print "usage: [host] [user] [password]";
       sys.exit(1)
    host = args[0] 
    username = args[1] 
    passwd = args[2] 

    dev = Device(host,user=username,password=passwd)
    print_app_table(dev)
    print_appgroup_table(dev)
## end main() ##

if __name__ == "__main__":
    main()
    
