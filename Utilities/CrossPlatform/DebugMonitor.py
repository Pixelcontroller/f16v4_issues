import socket
import sys
import getopt
import time
import platform

if platform.system() == "Windows":
    import msvcrt
    def getch():
        return msvcrt.getch()
    def kbhit():
        return msvcrt.kbhit()
else:
    import tty, termios, sys, fcntl, os
    def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    def kbhit():
        fd = sys.stdin.fileno()
        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)
        oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
        try:
            while True:
                try:
                    c = sys.stdin.read(1)
                    return True
                except IOError:
                    return False
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
            fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
                        
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Number of messages to check through to suppress duplicates ... if two identical messages are received subsequent ones will be suppressed
suppressDupCount = 30

# either use the default port or take the port from the command line
port = 10000
if len(sys.argv) > 1:
    port = sys.argv[1]

# Bind the socket to the port
server_address = ('', port)
print ('starting up on port', port)
sock.bind(server_address)

recent = []

while True:

    data, address = sock.recvfrom(4096)
    
    try:
        d = data.decode("utf-8")

        # this suppresses any messages duplicated within the last suppressDupCount messages
        if recent.count(d) == 0:
            print (d)
            recent.append(d)
            while len(recent) > suppressDupCount:
                recent.pop(0)
    except:
        #print("Error receiving data.")
        d = ""

    if kbhit():
        while kbhit():
            getch()
        print('')
        print('paused - press any key to resume')
        print('')
        while not kbhit():
            time.sleep(1)
        while kbhit():
            getch()
