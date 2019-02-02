import paramiko
import scp
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
import datetime
import time


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


def CopyFile(connectionlist, FiletoCopy, PathtoCopy):
    for key, value in connectionlist.items():
        try:
            hostip = key
            connection = value
            scp = SCPClient(connection.get_transport(), sanitize=lambda x: x)
            print ("Copying file {} to {} {}".format(FiletoCopy, hostip, PathtoCopy))
            # scp.get(remote_path=FiletoCopy, local_path=PathtoCopy)
            scp.put(FiletoCopy, PathtoCopy)
        except:
            print ("Not able to transfer the file to {}".format(hostip))
            continue


 # Firmware update
def subprocess_to_firmware_update(connectionlist, command_1):
    for key, value in connectionlist.items():
        hostip = key
        connection = value
        stdin, stdout, stderr = connection.exec_command(command_1)
        print ("Updating Firmware of {}".format(hostip))
        # line = stdout.readlines()
        for line in stdout:
            line = line.strip('\n')
            lines = line.split()
            for line_1 in lines:
                #lines = lines.split('')
                if (re.findall('reboot',line_1)):
                    print (line)
                    print ("Rebooting ..........{}".format(hostip))
                    stdin, stdout, stderr = connection.exec_command("sudo reboot")
                    print ("Firmware update done..{}\n".format(hostip))
                elif (re.findall('failed',line_1)):
                    print (line)
    time.sleep(100)


# def subprocess_cmd_2(connectionlist, command_2):
#     for key, value in connectionlist.items():
#         hostip = key
#         connection = value
#         stdin, stdout, stderr = connection.exec_command(command_2)
#         print ("----------------------------------------------------------------")
#         search_word = ['Release','Active','tcp', 'MQTT', 'Subscribe']
#         for line in stdout:
#             line = line.strip('\n')
#             lines = line.split()
#             for line_1 in lines:
#                 for word in search_word:
#                     if word in line_1:
#                         print ("{0}  for IP= {1} ".format(line,hostip))
#                         #result = subprocess.check_output(['uptime'])
#                         #print (result)
#                 else:
#                     continue


def subprocess_to_execute_cmd(connectionlist, command_3):
    for key, value in connectionlist.items():
        hostip = key
        connection = value
        stdin, stdout, stderr = connection.exec_command(command_3)
        print ("----------------------------------------------------------------")
        for line in stdout:
            line = line.strip('\n')
            lines = line.split()
            print line


def subprocess_to_check_service(connectionlist, command):
    for key, value in connectionlist.items():
        hostip = key
        connection = value
        stdin, stdout, stderr = connection.exec_command(command)
        # line = stdout.readlines()
        print ("----------------------------------------------------------------")
        for line in stdout:
            line = line.strip('\n')
            lines = line.split()
            for line_1 in lines:
                # lines = lines.split('')
                if line_1 == "Failed":
                    print ("Service is not running  {}".format(hostip), line)
                elif line_1 == "inactive":
                    print ("Service is inactive  {}".format(hostip), line)
                elif line_1 == "active":
                    print ("Service is active  {}".format(hostip), line)
                elif line_1 == " ":
                    print ("Servcie not found")
                else:
                    continue


def subprocess_to_check_message_log(connectionlist, command):
    for key, value in connectionlist.items():
        hostip = key
        connection = value
        print ("                                          ")
        print ("Checking message log---------------{}\n".format(hostip))
        stdin, stdout, stderr = connection.exec_command(command)
        # line = stdout.readlines()
        print ("----------------------------------------------------------------")
        search_word = ['local0.warning', 'kern.err', 'local6.err', 'daemon.warning', 'daemon.err', 'exited', 'Warning']
        for line in stdout:
            line = line.strip('\n')
            lines = line.split()
            for line_1 in lines:
                for word in search_word:
                    if word in line_1:  # and not linelist(search_word,line_1):
                        print (line)


# *********** Executing command from CSV file**********************************
def ExecCommand(connectionlist, cmdcsvfile):  # command execution
    with open(cmdcsvfile) as csvfile:
        readline = csv.DictReader(csvfile)
        for row in readline:
            command = row['command_name']
            print ("                ")
            print ("Executing command: {}".format(command))
            for key, value in connectionlist.items():
                hostip = key
                connection = value
                stdin, stdout, stderr = connection.exec_command(command)
                print ("----------------------------------------------")
                print ("Executing HostIp:{} for command {}\n".format(hostip, command))
                # print "--------------------------------------------------------------\n"

                for lines in stdout:
                    lines = lines.strip('\n')
                    print (lines)