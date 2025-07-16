import socket
import threading
import ipaddress
from concurrent.futures import ThreadPoolExecutor

ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3306, 3389, 8080]

def get_hosts(ip,cidr):
    network = ipaddress.IPv4Network(f'{ip}/{cidr}', strict=False)
    hosts = list(network.hosts())

    return hosts

def scan_host(ip):
    open_ports = []
    
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1.0)
            result = s.connect_ex((ip,port))
            s.close()

            if result == 0:
                open_ports.append(port)
        except:
            pass
    
    if open_ports:
        print(f"[_]Scanning ip address {ip} \n[+] open ports are : {', '.join(map(str, open_ports))}")
    else:
        print(f"[_]Scanning ip address {ip} \n[+] open ports are: None")

    return ip, open_ports

def scan_hosts(ip, cidr):
    hosts = get_hosts(ip,cidr)
    scan_results = []

    with ThreadPoolExecutor(max_workers= 100) as executor:
        task_ip_map = {}
        for host in hosts:
            task = executor.submit(scan_host, str(host))
            task_ip_map[task] = str(host)

        for task in task_ip_map:
            ip_result, open_port = task.result()
            scan_results.append((ip_result, open_port))

        scan_results.sort(key=lambda x: tuple(map(int, x[0].split('.'))))

scan_hosts("172.17.177.60" , "24")