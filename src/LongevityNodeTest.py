import argparse
import datetime

import DeviceActionLib


def LongevityNodeTestMain():
    UserName = "sensity"
    PrivKey = None
    connectionlist = dict()

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
    connectionlist = DeviceActionLib.ConnectNode(ipcsvfile, UserName=UserName, PrivKey=PrivKey)

    process_check = ['lsb_release -r',
                     'systemctl status mediaserver',
                     'netstat -a|grep 9883',
                     'systemctl status nmm.service']
    for service in process_check:
        print ("\n<*********************** NEW CMD ***********************>")
        print ("checking .. ", service)
        DeviceActionLib.subprocess_cmd_2(connectionlist, service)

    cmdlist = ['cfgtool -k nodeid',
               'uptime -p',
               'tail -20 /data/log/errors.log',
               'cat /data/log/messages | grep Booting',
               'cat /data/log/messages.1 | grep Booting',
               'zcat /data/log/messages.*.gz | grep Booting',
               'cat /data/log/messages | grep SEGV',
               'cat /data/log/messages.1 | grep SEGV',
               'zcat /data/log/messages.*.gz | grep SEGV',
               'cat /data/log/messages | grep Panic',
               'cat /data/log/messages | grep Killed',
               'cat /data/log/messages | grep Exited']

    for cmd in cmdlist:
        print("\n<*********************** NEW CMD ***********************>")
        print ("checkcmd ..", cmd)
        DeviceActionLib.subprocess_cmd_3(connectionlist, cmd)



if __name__ == '__main__':
    print ("=================== Test START at: {0} ===================\n ".format(datetime.datetime.now()))
    LongevityNodeTestMain()
    print ("\n=================== Test END at: {0} =================== ".format(datetime.datetime.now()))

  
## Instruction to RUN
# python /Users/saadira/rsDevelopment/projects/longevityUtils/src/LongevityNodeTest.py --ipcsvfile /Users/saadira/
# rsDevelopment/projects/longevityUtils/data/merlin_node_ip.csv --PrivKey ~/.ssh/saadira


# python2.7 ~/python/script/LongevityNodeTest.py  --ipcsvfile ~/python/data/merlin_node_ip.csv   --PrivKey ~/.ssh/alkesh



