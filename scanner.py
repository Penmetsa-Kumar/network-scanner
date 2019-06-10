import os, sys, re, uuid, getip, socket, platform, subprocess

os.system('cls')

def host_tcp(sock01):
    sock01 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def host_udp(sock02):
    sock02 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mac = os.system('GETMAC /V'"\n")
host_name = socket.gethostname()
host_local_ip = socket.gethostbyname(host_name)
host_public_ip = getip.get()
print ("\n""Host Name:",host_name,"\n" "Local IP:",host_local_ip,"\n" "Public IP:",host_public_ip, "\n")
remoteServer    = input("Enter a remote host to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)

 #-----PING_CODE-----

response = os.system("ping " + remoteServerIP)
if response == 0:
  print (remoteServer, 'is up!')
else:
  print (remoteServer, 'is down!')

#-------tcp_port_scanner----

print ("-" * 60)
print ("Please wait, scanning remote host", remoteServerIP)
print ("-" * 60)

try:
    for port in range(1,1025):  
        sock01 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock01.connect_ex((remoteServerIP, port))
        if result == 0:
            print ("| Port {}  | Open |".format(port))
        sock01.close()

except KeyboardInterrupt:
    print ("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print ('Hostname could not be resolved. Exiting')
    sys.exit()

except socket.error:
    print ("Couldn't connect to server")
    sys.exit()

#-------UDP_port_scanner-------

print ("-" * 60)
print ("Please wait, scanning remote host", remoteServerIP)
print ("-" * 60)

try:
    for port in range(1,1025):
        sock02 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        result = sock02.connect_ex((remoteServerIP, port))
        if result == 0:
            print ("UDP | Port {}  | Open |".format(port))
        sock02.close()

except KeyboardInterrupt:
    print ("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print ('Hostname could not be resolved. Exiting')
    sys.exit()

except socket.error:
    print ("Couldn't connect to server")
    sys.exit()
