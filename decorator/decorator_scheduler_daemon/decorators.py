
import os
import sys

import daemon
import daemon.pidfile


PROGNAME = 'monitor'
PATHCTRL = '/tmp/'  # path to control files pid and lock
pidpath = os.path.join(PATHCTRL, PROGNAME + ".pid")


def run_daemon(f):
    def wrapper(*args, **kwargs):
        print("INFO: Daemon Start")
        if os.path.exists(pidpath):
            print("INFO: Daemon already running (according to {0}).".format(pidpath))
            sys.exit(1)
        else:
            with daemon.DaemonContext(
                    stdout=sys.stdout,
                    stderr=sys.stderr,
                    pidfile=daemon.pidfile.PIDLockFile(pidpath)
            ):
                print(pidpath)
                f(args)
                print("INFO: Running daemon...")

    return wrapper
