import subprocess
import re
import ipaddress

def get_ip():
    address = subprocess.check_output('ipconfig', shell=True).decode()
    ip_search = re.search(r'IPv4 Address[.\s]*:\s*([\d.]+)', address)
    subnet_search = re.search(r'Subnet Mask[.\s]*:\s*([\d.]+)', address)

    ip = ip_search.group(1)
    subnet = subnet_search.group(1)

    return ip,subnet

def get_cidr(subnet):
    parts = subnet.split('.')
    cidr = 0

    for part in parts:
        binary = bin(int(part))
        ones = binary.count('1')
        cidr+= ones
    return cidr

def get_hosts(ip,cidr):
    network = ipaddress.IPv4Network(f'{ip}/{cidr}', strict=False)
    hosts = list(network.hosts())

    return hosts