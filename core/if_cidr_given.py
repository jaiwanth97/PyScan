import socket
import ipaddress
from concurrent.futures import ThreadPoolExecutor

ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3306, 3389, 8080]

def get_hosts(ip, cidr):
    network = ipaddress.IPv4Network(f'{ip}/{cidr}', strict=False)
    return list(network.hosts())

def scan_host(ip):
    open_ports = []
    
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1.0)
            result = s.connect_ex((ip, port))
            s.close()

            if result == 0:
                open_ports.append(port)
        except:
            pass

    return str(ip), open_ports


