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

def scan_ports(ip):
    for i in range(1,65536, 1000):
        threads = []
        for port in range(i, min(i+1000, 65536)):
            t = threading.Thread(target=scan_port, args=(ip, port))
            threads.append(t)
            t.start()
        
        for thread in threads:
            thread.join()
