import requests
import time
import subprocess

def internet_check(url = "https://www.google.com/"):
    try:
        requests.get(url)
        return True
    except:
        return False

while True:
    time.sleep(5)
    if not internet_check():
        
        print("trying to restart adabter")
        p1 = subprocess.Popen('netsh interface set interface "Wi-Fi" disable')
        p1.wait()
        p1.kill()
        p2 = subprocess.Popen('netsh interface set interface "Wi-Fi" enable')
        p2.wait()
        p2.kill()
    print('not yet', time.time())
