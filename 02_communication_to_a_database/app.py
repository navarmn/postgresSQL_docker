from tasks import scan_database
from time import sleep

while True:
    sleep(10)
    scan_database()