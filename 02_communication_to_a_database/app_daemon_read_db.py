from time import sleep
from daemonize import Daemonize
import argparse
import os

from tasks import scan_database

pid = "/tmp/this_app.pid"

def main():
    
    # Set global variables from argparse
    timeout, db_path  = set_global(args)

    while True:
        sleep(timeout)
        os.system('python tasks.py')

def set_global(args):
    
    return args['timeout'], args['db_path']

if __name__ == '__main__':
    
    # Arguments
    parser = argparse.ArgumentParser(description='Read database constantly using a daemon app')
    parser.add_argument('--timeout', default=10, type=float)
    parser.add_argument('--db-path', default=os.getcwd(), type=str)
    args = vars(parser.parse_args()) 

    # Start the app_daemon.py as service in UNIX

    daemon = Daemonize(app="app_daemon_read_db", pid=pid, action=main())
    daemon.start()
    