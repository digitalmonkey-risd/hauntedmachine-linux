import time
import subprocess

try:
    while True:
        os.system('python twitter.py')
        time.sleep(8)
except KeyboardInterrupt:
    print('interrupted!')