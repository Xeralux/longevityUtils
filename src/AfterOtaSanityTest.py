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


    #######################################
    # print("\n<*********************** Copy firmware into the Devices ***********************>")
    # filName = "/Users/saadira/Downloads/fiat-lux-cnext.fwpkg"
    # # copyPath = "/var/lib/flatpak-session/remotes"
    # copyPath = "/tmp"
    # DeviceActionLib.CopyFile(connectionlist, filName, copyPath)


    #######################################
    cmdlist = ['cfgtool -k nodeid',
               'date',
               'lsb_release -r',
               # 'sudo mnfw-update -r /tmp/fiat-lux-cnext.fwpkg'
               # 'ls /tmp',
               'uptime -p'
               # 'sudo mv /tmp/runtime.conf /var/lib/flatpak-session/remotes',
               # 'sudo ls /var/lib/flatpak-session/remotes'
               # 'cfgtool -match -k mediaserver.rtspsrc',
               # 'cfgtool -k mediaserver.rtspsrc -reset -local',
               # 'cfgtool -k mediaserver.rtspsrc -local -v rtsp://192.168.67.156:8554/testconvert.264', # For: IDLI
               # 'cfgtool -k mediaserver.rtspsrc -local -v rtsp://192.168.67.156:8554/testconvert.ts', # For: JAM
               # 'cfgtool -match -k mediaserver.rtspsrc'
               # 'sudo redis-cli -n 15 flushdb']
               # 'sudo ./top.sh'
               ]

    print("\n<*********************** Basic Device Check CMD ***********************>")
    for cmd in cmdlist:
        print ("\n=> Checking cmd: {0}".format(cmd))
        DeviceActionLib.subprocess_to_execute_cmd(connectionlist, cmd)


if __name__ == '__main__':
    print ("=================== Test START at: {0} ===================\n ".format(datetime.datetime.now()))
    sanityTestMain()
    print ("\n=================== Test END at: {0} =================== ".format(datetime.datetime.now()))