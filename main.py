from core.if_ip_given import scan_ports
from core.scanner import scan_hosts as scan_hosts_lan
from core.if_cidr_given import scan_hosts

if __name__ == "__main__":
    while True:
        print("\n1. Scan the ports (IP required)")
        print("2. Scan hosts (IP and CIDR required)")
        print("3. LAN sweep")
        print("4. Exit")
        option = input("Select an option: ")

        if option == "1":
            ip = input("Enter the IP address: ")
            scan_ports(ip)
        elif option == "2":
            ip = input("Enter the IP address: ")
            cidr = input("Enter the CIDR: ")
            scan_hosts(ip,cidr)
        elif option == "3":
            print("LAN sweep not implemented yet.")
            scan_hosts_lan()
        elif option == "4":
            print("Exiting...")
            break
        else:
            print("Please select an appropriate option (1-4).")
