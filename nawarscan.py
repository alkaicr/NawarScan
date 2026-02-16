#!/usr/bin/env python3

"""
NawarScan - Professional Multi-threaded Port Scanner
Author: Ahmed Ben Nawar
GitHub: https://github.com/YOUR_USERNAME

For educational and authorized penetration testing only.
"""

import socket
import argparse
import threading
from queue import Queue
import time
import sys

open_ports = []
lock = threading.Lock()


def scan_port(target, port, timeout):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((target, port))

            if result == 0:
                banner = ""
                try:
                    banner = s.recv(1024).decode().strip()
                except:
                    banner = "No banner"

                with lock:
                    open_ports.append((port, banner))

    except:
        pass


def worker(target, queue, timeout):
    while not queue.empty():
        port = queue.get()
        scan_port(target, port, timeout)
        queue.task_done()


def validate_ports(start_port, end_port):
    if start_port < 1 or end_port > 65535:
        print("[-] Ports must be between 1 and 65535.")
        sys.exit()
    if start_port > end_port:
        print("[-] Start port cannot be greater than end port.")
        sys.exit()


def main():
    parser = argparse.ArgumentParser(
        description="NawarScan - Professional Multi-threaded Port Scanner"
    )

    parser.add_argument("target", help="Target IP or Domain")
    parser.add_argument("start_port", type=int, help="Start port")
    parser.add_argument("end_port", type=int, help="End port")

    parser.add_argument(
        "-t", "--threads", type=int, default=100,
        help="Number of threads (default: 100)"
    )

    parser.add_argument(
        "--timeout", type=float, default=1,
        help="Socket timeout in seconds (default: 1)"
    )

    args = parser.parse_args()

    validate_ports(args.start_port, args.end_port)

    print(f"\n[+] NawarScan by Ahmed Ben Nawar")
    print(f"[+] Target: {args.target}")
    print(f"[+] Ports: {args.start_port}-{args.end_port}")
    print(f"[+] Threads: {args.threads}")
    print(f"[+] Timeout: {args.timeout}s\n")

    start_time = time.time()

    port_queue = Queue()

    for port in range(args.start_port, args.end_port + 1):
        port_queue.put(port)

    threads = []

    for _ in range(args.threads):
        thread = threading.Thread(
            target=worker,
            args=(args.target, port_queue, args.timeout)
        )
        thread.daemon = True
        thread.start()
        threads.append(thread)

    port_queue.join()

    end_time = time.time()

    print("\n[+] Scan Completed\n")

    if open_ports:
        print("Open Ports:")
        for port, banner in sorted(open_ports):
            print(f"  - {port:<6} | {banner}")
    else:
        print("No open ports found.")

    print(f"\n[+] Time Taken: {round(end_time - start_time, 2)} seconds\n")


if __name__ == "__main__":
    main()
