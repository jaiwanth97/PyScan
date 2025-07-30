from core.if_ip_given import scan_ports

if __name__ == "__main__":

    while(True):
        print("1.Scan the ports (IP required)")
        print("2.Scan hosts (IP and CIDR required)")
        print("3.LAN sweep")
        print("4. Exit")
        option = input("Select an option: ")

        if option == 1:
            ip = input("Enter the ip address: ")
        elif option == 2:
            ip = input("Enter the ip address: ")
            cidr = input("Enter the cidr: ")
        elif option == 3:
            exit
        elif option == 4:
            exit
        else:
            print("Please select appropriate option")