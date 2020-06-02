import socket
import sys, argparse
import bcolors

def banner():
    print("""
            ██████╗░░█████╗░██████╗░████████╗░██████╗░█████╗░░█████╗░███╗░░██╗
            ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██╔══██╗████╗░██║
            ██████╔╝██║░░██║██████╔╝░░░██║░░░╚█████╗░██║░░╚═╝███████║██╔██╗██║
            ██╔═══╝░██║░░██║██╔══██╗░░░██║░░░░╚═══██╗██║░░██╗██╔══██║██║╚████║
            ██║░░░░░╚█████╔╝██║░░██║░░░██║░░░██████╔╝╚█████╔╝██║░░██║██║░╚███║
            ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝
                                                                    Code by NG          
          """)

if len(sys.argv) > 1:
    banner()
    if ((sys.argv[1] == '-i') | (sys.argv[1] == '-s1') | (sys.argv[1] == '-s2')):
        try:
            target = sys.argv[2]
            low_range = sys.argv[4]
            high_range = sys.argv[6]

            parser = argparse.ArgumentParser()
            parser.add_argument("-i", required=True)
            parser.add_argument("-s1", required=True)
            parser.add_argument("-s2", required=True)
            args = parser.parse_args()

            host_name = socket.gethostname()
            host_ip = socket.gethostbyname(target)

            try:
                for port in range(int(low_range),int(high_range)):
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
        except:
            print(bcolors.ERR + 'Please provide valid Ip address ')
            print(bcolors.BOLD + 'Please enter python portscan.py -i <valid Ip address path> -s1 <start scan range> -s2 <end scan range>')


    elif (((sys.argv[1] == '-i') & (sys.argv[1] == '-s1')) | (sys.argv[1] == '--help')):
        print(bcolors.BOLD + 'usage: portscan.py [-h] -i valid ip address , -s1 start scan range, -s2 end scan range ' '\n' 'OPTIONS:' '\n' '-h,--help    '
                             'show this help message and exit' '\n''-i valid ip address  --Ip address whose open ports you want to check' '\n''-s1  starting port range,   --start range of port' 
                             '\n' '-s2 ending port range   --end range of port ')
    elif (((sys.argv[1] == '-i') & (sys.argv[1] == '-s1')) | (sys.argv[1] != '-s2')):
        print('Please enter -i <valid ip address> -s1 <starting range of scanning> -s2 <ending range of scanning>')

else:
    banner()
    print(bcolors.ERR + 'Please select options from (-i and (-s1,-s2)) or -h, with a valid domain name')


