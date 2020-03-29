import socket
import sys

print("-----------------------------------------------")
print("Port Scanner")
print("Code By : NG")
print("Usage: python portscan.py and then follow the instructions")
print("-----------------------------------------------")

target = input("Please enter ipaddress or hostname")
host_name = socket.gethostname()
host_ip = socket.gethostbyname(target)

low_range = int(input("Please Enter the Port Where You want to Start Scanning"))
high_range = int(input("Please Enter the Port Where You want to end Scanning"))

try:
    for port in range(low_range,high_range):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect = sock.connect_ex((host_ip, port))
        if connect == 0:
            print("Port {}:    is Open".format(port))
        sock.close()

except socket.gaierror:
    print("HostName Can't be resolved")
    sys.exit()

except socket.error:
    print("Server Not Found")
    sys.exit()
