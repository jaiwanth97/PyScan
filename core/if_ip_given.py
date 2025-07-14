import socket
import threading

def scan_port(ip,port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)
        result = s.connect_ex((ip,port))
        if result==0:
            print(f"[+] {port} is open")
        s.close()
    except:
        pass

def scan_ports(ip):
    threads = []

    for port in range(1, 65536):
        t = threading.Thread(target=scan_port, args=(ip,port))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()
