
#Author: Asif Hassan
#Main author:Shaikh Nazrul Islam



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
        print ("**************************************************************")
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
        for line in stdout:
            line = line.strip('\n')
            lines = line.split()
            print line 

def subprocess_cmd_4(connectionlist):
    for key, value in connectionlist.items():
        hostip = key
        connection = value
        print ("***********************************************************************")
        stdin, stdout, stderr = connection.exec_command('cfgtool -k nodeid') 
        for line in stdout:
            line = line.strip('\n')
            lines = line.split()
            print line
        stdin, stdout, stderr = connection.exec_command('lsb_release -r')
        for line in stdout:
            line = line.strip('\n')
            lines = line.split()
            print line
        stdin, stdout, stderr = connection.exec_command('uptime -p')
        for line in stdout:
            line = line.strip('\n')
            lines = line.split()
            print line
        stdin, stdout, stderr = connection.exec_command('tail -10 /data/log/errors.log')
        for line in stdout:
            line = line.strip('\n')
            lines = line.split()
            print line 
        stdin, stdout, stderr = connection.exec_command('cat /data/log/messages|grep Booting')
        for line in stdout:
            line = line.strip('\n')
            lines = line.split()
            print line
        stdin, stdout, stderr = connection.exec_command('zcat /data/log/messages.1.gz|grep Booting')
        for line in stdout:
            line = line.strip('\n')
            lines = line.split()
            print line
        stdin, stdout, stderr = connection.exec_command('zcat /data/log/messages.2.gz|grep Booting')
        for line in stdout:
            line = line.strip('\n')
            lines = line.split()
            print line
        stdin, stdout, stderr = connection.exec_command('cat /data/log/messages|grep Panic')
        for line in stdout:
            line = line.strip('\n')
            lines = line.split()
            print line
        stdin, stdout, stderr = connection.exec_command('cat /data/log/messages|grep Killed')
        for line in stdout:
            line = line.strip('\n')
            lines = line.split()
            print line
        stdin, stdout, stderr = connection.exec_command('cat /data/log/messages|grep Exited')
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
    cmdlist = ['cfgtool -k nodeid','uptime -p','tail -5 /data/log/errors.log']
    #for cmd4 in connectionlist:
    subprocess_cmd_4(connectionlist)
    for cmd in cmdlist:
        print("********************************************************")
        print ("checkcmd ..", cmd)
        subprocess_cmd_3(connectionlist, cmd)
    process_check = ['lsb_release -r','systemctl status mediaserver','netstat -a|grep 9883', 'systemctl status nmm.service']
    for service in process_check:
        print ("      ")
        print ("checking .. ",service)
        subprocess_cmd_2(connectionlist, service)
    ExecStart = time.time()

if __name__ == '__main__':
    main()

  
#for NGCN
#/usr/bin/python2.7 ~/Documents/python_automate/new_code.py  --ipcsvfile ~/Documents/python_automate/test_node_ip.csv  
# --PathtoCopy /data/sensity/ --FiletoCopy ~/Downloads/fiat-lux-cnext.fwpkg  --PrivKey ~/.ssh/hasas2x



