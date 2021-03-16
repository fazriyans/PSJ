import os

hostname = "192.168.56.1"
response = os.system("ping -c 1 " + hostname)

if response == 0:
    print(hostname, "UP")
else:
    print(hostname, "DOWN")