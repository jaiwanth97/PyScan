import typer #type: ignore
from core.if_ip_given import scan_ports
from core.scanner import scan_hosts as scan_hosts_lan
from core.if_cidr_given import scan_hosts

app = typer.Typer(help="PyScan - Lightweight Network Scanner")

@app.command("scan-ports")
def scan_ports_cli(ip: str = typer.Argument(..., help="IP address to scan ports on")):
    scan_ports(ip)

@app.command("scan-hosts")
def scan_hosts_cli(ip: str = typer.Argument(..., help="IP address"),
                   cidr: int = typer.Argument(..., help="CIDR value (e.g., 24 for /24)")):
    scan_hosts(ip, cidr)

@app.command("lan-sweep")
def lan_sweep():
    scan_hosts_lan()

if __name__ == "__main__":
    app()
