import argparse
import datetime

import DeviceActionLib


def sanityTestMain():

    UserName = "sensity"
    PrivKey = None
    connectionlist = dict()

    parser = argparse.ArgumentParser()
    parser.add_argument("--Debug", action="store_true", help="Print detailed messages to stdout")
    parser.add_argument("--ipcsvfile", default='None', help="Specify Ip CSV file with full path")
    parser.add_argument("--PrivKey", default='None', help="Specify the HostIP")

    args = parser.parse_args()
    ipcsvfile = str(args.ipcsvfile)
    PrivKey = str(args.PrivKey)
    Debug = str(args.Debug)

    # *************Calling Function******************************
    connectionlist = DeviceActionLib.ConnectNode(ipcsvfile, UserName=UserName, PrivKey=PrivKey)

    cmdlist = ['cfgtool -k nodeid',
               'uptime -p',
               'tail -20 /data/log/errors.log',
               'Top.sh']

    for cmd in cmdlist:
        print("\n<*********************** NEW CMD ***********************>")
        print ("checkcmd ..", cmd)
        DeviceActionLib.subprocess_to_execute_cmd(connectionlist, cmd)


if __name__ == '__main__':
    print ("=================== Test START at: {0} ===================\n ".format(datetime.datetime.now()))
    sanityTestMain()
    print ("\n=================== Test END at: {0} =================== ".format(datetime.datetime.now()))