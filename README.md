# NetHawk - Lightweight Network Scanner

A fast and efficient network scanner built in Python for discovering hosts and scanning ports on local networks and specific IP addresses.

## Features

- **LAN Sweep**: Automatically discover and scan all hosts on your local network
- **Port Scanning**: Scan all ports (1-65535) on a specific IP address
- **Network Range Scanning**: Scan hosts within a specified CIDR range
- **Multi-threaded**: Fast concurrent scanning for improved performance
- **Output Logging**: Automatically saves scan results to timestamped files
- **Cross-platform**: Works on Windows, Linux, and macOS

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd nethawk
```

2. Install required dependencies:
```bash
pip install typer
```

3. Make the script executable (Linux/macOS):
```bash
chmod +x main.py
```

## Usage

NetHawk provides three main scanning modes through a command-line interface:

### 1. LAN Sweep
Automatically discovers your local network configuration and scans all hosts:

```bash
python main.py lan-sweep
```

This command will:
- Detect your local IP address and subnet mask
- Calculate the network range
- Scan all hosts in the network for common open ports

### 2. Port Scanning
Scan all ports (1-65535) on a specific IP address:

```bash
python main.py scan-ports <IP_ADDRESS>
```

Example:
```bash
python main.py scan-ports 192.168.1.100
```

### 3. Network Range Scanning
Scan hosts within a specific CIDR range:

```bash
python main.py scan-hosts <IP_ADDRESS> <CIDR>
```

Example:
```bash
python main.py scan-hosts 192.168.1.0 24
```

## Common Ports Scanned

NetHawk scans the following commonly used ports by default in LAN sweep and network range scanning modes:

- **21** - FTP
- **22** - SSH
- **23** - Telnet
- **25** - SMTP
- **53** - DNS
- **80** - HTTP
- **110** - POP3
- **135** - RPC
- **139** - NetBIOS
- **143** - IMAP
- **443** - HTTPS
- **445** - SMB
- **3306** - MySQL
- **3389** - RDP
- **8080** - HTTP Alternative

## Output

Scan results are automatically saved to timestamped files in the format:
```
scan_YYYY-MM-DD_HH-MM-SS.txt
```

The output includes:
- Scan timestamp
- IP addresses scanned
- Open ports found on each host
- Clear indicators for hosts with no open ports

Example output:
```
File created at: 2024-01-15 14:30:25.123456
[_]Scanning ip address 192.168.1.1:
[+] Open ports are: 22,80,443

[_]Scanning ip address 192.168.1.100:
[-]Open ports are: None
```

## Project Structure

```
nethawk/
├── main.py                 # CLI entry point
├── core/
│   ├── __init__.py
│   ├── discovery.py        # Network discovery functions
│   ├── scanner.py          # LAN scanning functionality
│   ├── if_ip_given.py      # Single IP port scanning
│   └── if_cidr_given.py    # CIDR range scanning
└── output/
    └── output.py           # Output handling and file writing
```

## Performance Features

- **Concurrent Scanning**: Uses ThreadPoolExecutor with up to 100 worker threads for fast network scanning
- **Optimized Timeouts**: 1-second socket timeouts to balance speed and accuracy
- **Efficient Port Scanning**: Batched port scanning in chunks of 1000 ports for single IP scans
- **Smart Network Detection**: Automatic IP and subnet mask detection on Windows systems

## Requirements

- Python 3.6+
- `typer` library for CLI interface
- Standard library modules: `socket`, `subprocess`, `ipaddress`, `concurrent.futures`, `threading`

## Platform Support

- **Windows**: Full support with automatic network configuration detection
- **Linux/macOS**: Core functionality supported (may require manual network configuration for some features)

## Security Considerations

- Only scans common ports by default to minimize network impact 
- Uses non-invasive TCP connect scans
- Implements reasonable timeouts to avoid overwhelming target systems
- Intended for authorized network security testing only

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Help

For help and available commands:
```bash
python main.py --help
```

For help with specific commands:
```bash
python main.py scan-ports --help
python main.py scan-hosts --help
python main.py lan-sweep --help
```