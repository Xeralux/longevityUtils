import argparse
import datetime

import DeviceActionLib


def LongevityNodeTestMain():
    UserName = "sensity"
    PrivKey = None
    connectionlist = dict()

    # Parsing commandline arguments
    parser = argparse.ArgumentParser()
#    parser.add_argument("--HostIp", default='92.168.65.103', help="Specify the HostIP")
    parser.add_argument("--Debug", action="store_true", help="Print detailed messages to stdout")
    parser.add_argument("--ipcsvfile", default='None', help="Specify Ip CSV file with full path")
    parser.add_argument("--PrivKey", default='None', help="Specify the HostIP")

    args = parser.parse_args()
    ipcsvfile = str(args.ipcsvfile)
    PrivKey  = str(args.PrivKey)
    Debug = str(args.Debug)

    # Connecting to the test devices
    connectionlist = DeviceActionLib.ConnectNode(ipcsvfile, UserName=UserName, PrivKey=PrivKey)

    # Checking device basic status
    basic_device_checks = ['cfgtool -k nodeid',
                           'uptime -p',
                           'lsb_release -r']
    print("\n<<<<<<<<<<<<<<<<<<<<<<<<< Basic Device Check CMD >>>>>>>>>>>>>>>>>>>>>>>>>>")
    for cmd in basic_device_checks:
        print ("\n=> Checking cmd: {0}".format(cmd))
        DeviceActionLib.subprocess_to_execute_cmd(connectionlist, cmd)

    # Checking different process status
    process_checks = ['systemctl status nirung',
                     'systemctl status shadow.service',
                     'systemctl status *modem*',
                     'systemctl status gate-keeper',
                     'systemctl status mediaserver',
                     'systemctl status *mve*',
                     'netstat -a | grep 9883',
                     'systemctl status nmm.service']
    print ("\n<<<<<<<<<<<<<<<<<<<<<<<<< Service Check CMD >>>>>>>>>>>>>>>>>>>>>>>>>>")
    for service in process_checks:
        print ("\n=> Checking cmd: {0}".format(service))
        DeviceActionLib.subprocess_to_check_service(connectionlist, service)

    # Checking different error in message log
    message_checks = ['tail -20 /data/log/errors.log',
                      'cat /data/log/messages | grep Booting',
                      'cat /data/log/messages.1 | grep Booting',
                      'zcat /data/log/messages.*.gz | grep Booting',
                      'cat /data/log/messages | grep SEGV',
                      'cat /data/log/messages.1 | grep SEGV',
                      'zcat /data/log/messages.*.gz | grep SEGV',
                      'cat /data/log/messages | grep panic',
                      'cat /data/log/messages.1 | grep panic',
                      'cat /data/log/messages | grep killed',
                      'cat /data/log/messages.1 | grep killed',
                      'cat /data/log/messages | grep exited']
    print("\n<<<<<<<<<<<<<<<<<<<<<<<<< Message Log Check CMD >>>>>>>>>>>>>>>>>>>>>>>>>>")
    for cmd in message_checks:
        print ("\n=> Checking cmd: {0}".format(cmd))
        DeviceActionLib.subprocess_to_check_message_log(connectionlist, cmd)


if __name__ == '__main__':
    print ("=================== Test START at: {0} ===================\n ".format(datetime.datetime.now()))
    LongevityNodeTestMain()
    print ("\n=================== Test END at: {0} =================== ".format(datetime.datetime.now()))

  
## Instruction to RUN
# python /Users/saadira/rsDevelopment/projects/longevityUtils/src/LongevityNodeTest.py --ipcsvfile /Users/saadira/
# rsDevelopment/projects/longevityUtils/data/merlin_node_ip.csv --PrivKey ~/.ssh/saadira


# python2.7 ~/python/script/LongevityNodeTest.py  --ipcsvfile ~/python/data/merlin_node_ip.csv   --PrivKey ~/.ssh/alkesh



