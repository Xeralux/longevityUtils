import argparse
import datetime

import DeviceActionLib


def test_deviceBasicInfo(connectionlist):
    print("INFO: Checking device basic status")
    basic_device_checks = ['cfgtool -k nodeid',
                           'date',
                           'uptime -p',
                           'lsb_release -r',
                           'netstat -a | grep 9883',
                           'cat /data/log/messages | grep exited | wc -l',
                           # 'find /data/crash/ -mtime -1 -type f -print | xargs ls -ltr',
                           'find /data/crash/ -mtime -1 -type f -print']
    print("\n<<<<<<<<<<<<<<<<<<<<<<<<< Basic Device Check CMD >>>>>>>>>>>>>>>>>>>>>>>>>>")
    for cmd in basic_device_checks:
        print ("\n=> Checking cmd: {0}".format(cmd))
        DeviceActionLib.subprocess_to_execute_cmd(connectionlist, cmd)


def test_deviceProcessStatus(connectionlist):
    print("INFO: Checking different process status")
    process_checks = ['systemctl status nirung',
                      'systemctl status shadow.service',
                      'systemctl status *modem*',
                      'systemctl status gate-keeper',
                      'systemctl status mediaserver',
                      'systemctl status mnrecorder',
                      'systemctl status *mve*']
                      # 'netstat -a | grep 9883']
    # 'systemctl status nmm.service']
    print ("\n<<<<<<<<<<<<<<<<<<<<<<<<< Service Check CMD >>>>>>>>>>>>>>>>>>>>>>>>>>")
    for service in process_checks:
        print ("\n=> Checking cmd: {0}".format(service))
        DeviceActionLib.subprocess_to_check_service(connectionlist, service)


# def test_BootingErrorInMessageLog(connectionlist):
#     print("INFO: Checking Booting error in message log")
#     booting_checks = [  # 'tail -20 /data/log/errors.log',
#         'cat /data/log/messages | grep Booting',
#         'cat /data/log/messages.1 | grep Booting',
#         'zcat /data/log/messages.2.gz | grep Booting'
#     # 'zcat /data/log/messages.*.gz | grep Booting',
#     ]
#
#     # print("\n<<<<<<<<<<<<<<<<<<<<<<<<< Message Log Check CMD >>>>>>>>>>>>>>>>>>>>>>>>>>")
#     for cmd in booting_checks:
#         print ("\n=> Checking cmd: {0}".format(cmd))
#         DeviceActionLib.subprocess_to_check_message_log(connectionlist, cmd)
#
#
# def test_RebootInMessageLog(connectionlist):
#     print("INFO: Checking Reboot in message log")
#     reboot_checks = [  # 'tail -20 /data/log/errors.log',
#         'cat /data/log/messages | grep Booting',
#         'cat /data/log/messages.1 | grep Booting',
#         'zcat /data/log/messages.2.gz | grep Booting'
#         # 'zcat /data/log/messages.*.gz | grep Booting',
#     ]
#
#     # print("\n<<<<<<<<<<<<<<<<<<<<<<<<< Message Log Check CMD >>>>>>>>>>>>>>>>>>>>>>>>>>")
#     for cmd in reboot_checks:
#         print ("\n=> Checking cmd: {0}".format(cmd))
#         DeviceActionLib.subprocess_to_check_message_log(connectionlist, cmd)
#
#
# def test_SEGVErrorInMessageLog(connectionlist):
#     print("INFO: Checking Reboot in message log")
#     segv_checks = [ 'cat /data/log/messages | grep SEGV',
#         'cat /data/log/messages.1 | grep SEGV',
#         'zcat /data/log/messages.*.gz | grep SEGV'
#     ]
#
#     # print("\n<<<<<<<<<<<<<<<<<<<<<<<<< Message Log Check CMD >>>>>>>>>>>>>>>>>>>>>>>>>>")
#     for cmd in segv_checks:
#         print ("\n=> Checking cmd: {0}".format(cmd))
#         DeviceActionLib.subprocess_to_check_message_log(connectionlist, cmd)
#
#
# def test_SEGVErrorInMessageLog(connectionlist):
#     print("INFO: Checking Reboot in message log")
#     segv_checks = [ 'cat /data/log/messages | grep SEGV',
#         'cat /data/log/messages.1 | grep SEGV',
#         'zcat /data/log/messages.*.gz | grep SEGV'
#     ]
#
#     # print("\n<<<<<<<<<<<<<<<<<<<<<<<<< Message Log Check CMD >>>>>>>>>>>>>>>>>>>>>>>>>>")
#     for cmd in segv_checks:
#         print ("\n=> Checking cmd: {0}".format(cmd))
#         DeviceActionLib.subprocess_to_check_message_log(connectionlist, cmd)


def test_errorInMessageLog(connectionlist):
    print("INFO: Checking different error in message log")
    message_checks = [  # 'tail -20 /data/log/errors.log',
        'cat /data/log/messages | grep Booting',
        'cat /data/log/messages.1 | grep Booting',
        # 'zcat /data/log/messages.2.gz | grep Booting',
        'zcat /data/log/messages.*.gz | grep Booting',
        'cat /data/log/messages | grep reboot',
        'cat /data/log/messages.1 | grep reboot',
        # 'zcat /data/log/messages.2.gz | grep reboot'
        'zcat /data/log/messages.*.gz | grep reboot',
        'cat /data/log/messages | grep SEGV',
        'cat /data/log/messages.1 | grep SEGV',
        'zcat /data/log/messages.*.gz | grep SEGV',
        'cat /data/log/messages | grep panic',
        'cat /data/log/messages.1 | grep panic',
        # 'zcat /data/log/messages.2.gz | grep panic',
        'zcat /data/log/messages.*.gz | grep panic',
        'cat /data/log/messages | grep killed',
        'cat /data/log/messages.1 | grep killed',
        'zcat /data/log/messages.2.gz | grep killed',
        # 'zcat /data/log/messages.*.gz | grep killed',
        'cat /data/log/messages | grep "Pipeline stall"',
        'cat /data/log/messages.1 | grep "Pipeline stall"',
        # 'zcat /data/log/messages.2.gz | grep "Pipeline stall"',
        'zcat /data/log/messages.*.gz | grep "Pipeline stall"',
        'cat /data/log/messages | grep "ABRT"',
        'cat /data/log/messages.1 | grep "ABRT"',
        # 'zcat /data/log/messages.2.gz | grep "ABRT"'
        'zcat /data/log/messages.*.gz | grep "ABRT"',
        # 'cat /data/log/messages | grep "Failed to read registration status"',
        # 'cat /data/log/messages.1 | grep "Failed to read registration status"',
        # 'zcat /data/log/messages.*.gz | grep "Failed to read registration status"',
        # 'cat /data/log/messages | grep "PPP daemon is not running"',
        # 'cat /data/log/messages.1 | grep "PPP daemon is not running"',
        # 'zcat /data/log/messages.*.gz | grep "PPP daemon is not running"',
        'cat /data/log/messages | grep "input/output error"'
        # 'cat /data/log/messages.1 | grep "input/output error"',
        # 'zcat /data/log/messages.*.gz | grep "input/output error"'
    ]
    # 'cat /data/log/messages | grep exited']

    print("\n<<<<<<<<<<<<<<<<<<<<<<<<< Message Log Check CMD >>>>>>>>>>>>>>>>>>>>>>>>>>")
    for cmd in message_checks:
        print ("\n=> Checking cmd: {0}".format(cmd))
        DeviceActionLib.subprocess_to_check_message_log(connectionlist, cmd)


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
    PrivKey = str(args.PrivKey)
    Debug = str(args.Debug)

    # Connecting to the test devices
    connectionlist = DeviceActionLib.ConnectNode(ipcsvfile, UserName=UserName, PrivKey=PrivKey)

    test_deviceBasicInfo(connectionlist)
    test_deviceProcessStatus(connectionlist)
    test_errorInMessageLog(connectionlist)



if __name__ == '__main__':
    print ("=================== Test START at: {0} ===================\n ".format(datetime.datetime.now()))
    LongevityNodeTestMain()
    print ("\n=================== Test END at: {0} =================== ".format(datetime.datetime.now()))

## Instruction to RUN
# python /Users/saadira/rsDevelopment/projects/longevityUtils/src/LongevityNodeTest.py --ipcsvfile /Users/saadira/
# rsDevelopment/projects/longevityUtils/data/merlin_node_ip.csv --PrivKey ~/.ssh/saadira


# python2.7 ~/python/script/LongevityNodeTest.py  --ipcsvfile ~/python/data/merlin_node_ip.csv   --PrivKey ~/.ssh/alkesh
