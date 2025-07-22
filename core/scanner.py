import socket
from concurrent.futures import ThreadPoolExecutor
from discovery import get_hosts, get_cidr, get_ip
from output import print_output

ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3306, 3389, 8080]

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


def scan_hosts():
    ip, subnet = get_ip()
    cidr = get_cidr(subnet)
    hosts = get_hosts(ip, cidr)
    scan_results = []

    with ThreadPoolExecutor(max_workers=100) as executor:
        task_ip_map = {}
        for host in hosts:
            task = executor.submit(scan_host, str(host))
            task_ip_map[task] = str(host)

        for task in task_ip_map:
            ip_result, open_port = task.result()
            scan_results.append((ip_result, open_port))

    scan_results.sort(key=lambda x: tuple(map(int, x[0].split('.'))))
    lines = []
    for ip, open_ports in scan_results:
        print(f"[_]Scanning ip address {ip}:")
        lines.append(f"[_]Scanning ip address {ip}:")
        if open_ports:
            print(f"[+] Open ports are: {','.join(map(str,open_ports))}\n")
            lines.append(f"[+] Open ports are: {','.join(map(str,open_ports))}\n")
        else:
            print(f"[-]Open ports are: None\n")
            lines.append(f"[-]Open ports are: None\n")

    print_output(lines)
