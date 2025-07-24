import socket
import threading
from output.output import print_output

def scan_port(ip,port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        result = s.connect_ex((ip,port))
        if result==0:
            print(f"[+] {port} is open")
        elif result == 111 or result == 10061:
            print(f"[+] {port} is closed")
        s.close()
    except:
        pass

