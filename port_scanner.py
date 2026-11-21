import argparse
import socket
import sys
from typing import Dict, List, Optional, Tuple

COMMON_SERVICES: Dict[int, str] = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP Alternative",
}


def parse_ports(ports_arg: Optional[str]) -> Dict[int, str]:
    """Parse a comma-separated port list or range (e.g., '22,80,443' or '20-25')."""
    if not ports_arg:
        return COMMON_SERVICES

    parsed: Dict[int, str] = {}
    for part in ports_arg.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start_str, end_str = part.split("-", 1)
            start, end = int(start_str), int(end_str)
            if not (1 <= start <= end <= 65535):
                raise ValueError(f"Invalid port range: {part}")
            for port in range(start, end + 1):
                parsed[port] = COMMON_SERVICES.get(port, "Unknown")
        else:
            port = int(part)
            if not (1 <= port <= 65535):
                raise ValueError(f"Invalid port number: {port}")
            parsed[port] = COMMON_SERVICES.get(port, "Unknown")

    if not parsed:
        raise ValueError("No valid ports provided.")
    return parsed


def scan_port(target_ip: str, port: int, timeout: float) -> Tuple[bool, Optional[str]]:
    """Attempt a TCP connection to a single port and return (is_open, error_message)."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.settimeout(timeout)
        try:
            result = client.connect_ex((target_ip, port))
            return result == 0, None
        except socket.error as error:
            return False, str(error)


def run_scan(target: str, ports_map: Dict[int, str], timeout: float) -> List[int]:
    """Resolve the target host, scan all specified ports, and return open port numbers."""
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror as error:
        print(f"Error resolving target '{target}': {error}", file=sys.stderr)
        sys.exit(1)

    print("===== TCP PORT SCANNER =====")
    print(f"Target: {target} ({target_ip})")
    print(f"Timeout: {timeout}s | Ports to scan: {len(ports_map)}\n")

    open_ports: List[int] = []
    for port, service in ports_map.items():
        is_open, error = scan_port(target_ip, port, timeout)
        if error:
            print(f"Port {port} ({service}) - ERROR: {error}")
        elif is_open:
            print(f"Port {port} ({service}) - OPEN")
            open_ports.append(port)
        else:
            print(f"Port {port} ({service}) - CLOSED or FILTERED")

    print("\n===== SCAN SUMMARY =====")
    print(f"Total ports scanned: {len(ports_map)}")
    print(f"Open ports: {len(open_ports)}")
    if open_ports:
        print(f"Open port numbers: {open_ports}")
    else:
        print("No open ports detected.")
    print("Scan completed.")

    return open_ports


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Lightweight TCP port scanner for authorized security testing."
    )
    parser.add_argument(
        "-t",
        "--target",
        default="127.0.0.1",
        help="Target IP address or hostname (default: 127.0.0.1)",
    )
    parser.add_argument(
        "-p",
        "--ports",
        default=None,
        help="Comma-separated ports or range, e.g. '22,80,443' or '20-100' (default: common ports)",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=1.0,
        help="Socket timeout in seconds (default: 1.0)",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    try:
        ports_map = parse_ports(args.ports)
    except ValueError as error:
        parser.error(str(error))

    run_scan(args.target, ports_map, args.timeout)


if __name__ == "__main__":
    main()
