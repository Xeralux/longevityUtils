import paramiko
import scp
import time
import os
import subprocess
import datetime
from optparse import OptionParser
import argparse
import csv
from paramiko import SSHClient
from scp import SCPClient
import random
import urllib
import re
import subprocess
import datetime


start_time = time.time()   

def ConnectNode(ipcsvfile, UserName, PrivKey):    #Connection established
    connection = dict()
    with open(ipcsvfile) as csvfile:
        readline = csv.DictReader(csvfile)
        for row in readline:
            try:
                InHostIp = row['Ip_address']
                print ('Host is {0}'.format(InHostIp))
                inconnection = paramiko.SSHClient()              
                inconnection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                print ("Connecting...Host={}\n".format(InHostIp))
                inconnection.connect(hostname=InHostIp, username=UserName, key_filename=PrivKey, timeout=100)
                print ("Connected...Host={}\n".format(InHostIp))
                connection[InHostIp] = inconnection
            except:
                print ("Not Connected to...Host={}\n".format(InHostIp))
                continue
    return (connection)


def subprocess_cmd_2(connectionlist, command_2):
    for key, value in connectionlist.items():
        hostip = key
        connection = value
        stdin, stdout, stderr = connection.exec_command(command_2)
        print ("----------------------------------------------------------------")
        search_word = ['Release','Active','tcp']
        for line in stdout:
            line = line.strip('\n')
            lines = line.split()
            for line_1 in lines:
                for word in search_word:
                    if word in line_1:
                        print ("{0}  for IP= {1} ".format(line,hostip))
                        #result = subprocess.check_output(['uptime'])
                        #print (result)
                else:
                    continue 
def subprocess_cmd_3(connectionlist, command_3):
    for key, value in connectionlist.items():
        hostip = key
        connection = value
        stdin, stdout, stderr = connection.exec_command(command_3)
        print ("----------------------------------------------------------------")
        for line in stdout:
            line = line.strip('\n')
            lines = line.split()
            print line




def main():
    HostIp = "192.168.66.118"
    UserName = "sensity"

    csvfile = None
    PrivKey = None
    connectionlist = dict()
    printcommand = None

    parser = argparse.ArgumentParser()
#    parser.add_argument("--HostIp", default='92.168.65.103', help="Specify the HostIP")
    parser.add_argument("--Debug", action="store_true", help="Print detailed messages to stdout")
    parser.add_argument("--ipcsvfile", default='None', help="Specify Ip CSV file with full path")
    parser.add_argument("--PrivKey", default='None', help="Specify the HostIP")

    args = parser.parse_args()
    ipcsvfile = str(args.ipcsvfile)
    PrivKey  = str(args.PrivKey)
    Debug = str(args.Debug)

#*************Calling Function******************************
    connectionlist = ConnectNode(ipcsvfile, UserName=UserName, PrivKey=PrivKey)
    cmdlist = ['cfgtool -k nodeid',
               'uptime -p',
               'tail -10 /data/log/errors.log',
               'cat /data/log/messages | grep Booting',
               'cat /data/log/messages.1 | grep Booting',
               'zcat /data/log/messages.*.gz | grep Booting',
               'cat /data/log/messages | grep Panic',
               'cat /data/log/messages | grep Killed',
               'cat /data/log/messages|grep Exited']

    for cmd in cmdlist:
        print("\n<*********************** NEW CMD ***********************>")
        print ("checkcmd ..", cmd)
        subprocess_cmd_3(connectionlist, cmd)

    process_check = ['lsb_release -r',
                     'systemctl status mediaserver',
                     'netstat -a|grep 9883',
                     'systemctl status nmm.service']
    for service in process_check:
        print ("\n<*********************** NEW CMD ***********************>")
        print ("checking .. ",service)
        subprocess_cmd_2(connectionlist, service)


if __name__ == '__main__':
    print ("=================== Test START at: {0} ===================\n ".format(datetime.datetime.now()))
    main()
    print ("\n=================== Test END at: {0} =================== ".format(datetime.datetime.now()))

  
## Instruction to RUN
# python /Users/saadira/rsDevelopment/projects/longevityUtils/src/chklongnodetest.py --ipcsvfile /Users/saadira/
# rsDevelopment/projects/longevityUtils/data/merlin_node_ip.csv --PrivKey ~/.ssh/saadira


# python2.7 ~/python/script/chklongnodetest.py  --ipcsvfile ~/python/data/merlin_node_ip.csv   --PrivKey ~/.ssh/alkesh



