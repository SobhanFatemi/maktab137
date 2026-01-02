#!/usr/bin/env python3

import argparse
import re as regex
from collections import Counter 
import time

IP_PATTERN = r"\b(?:(?:2(?:[0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9])\.){3}(?:2(?:[0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9])\b"

URL_PATTERN = r'"(?:GET|POST|PUT|DELETE|PATCH|OPTIONS|HEAD) ([^"]+) HTTP/\d\.\d"|https?://[^\s"]+'

RESPONSE_SIZE_PATTERN = r'"(?:GET|POST|PUT|DELETE|PATCH|OPTIONS|HEAD) [^"]*" \d{3} (\d+)'

ERRORS_PATTERN = r'"\s*(?:GET|POST|PUT|DELETE|PATCH|OPTIONS|HEAD)[^"]*"\s+([45]\d{2})'

TIMESTAMP_PATTERN = r"\[\d{2}/[A-Za-z]{3}/\d{4}:\d{2}:\d{2}:\d{2} [+-]\d{4}\]|\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\]"

EMAIL_PATTERN = r"(?<=\s)-\s*(?:[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}|-)"

API_PATTERN = r'"(?:GET|POST|PUT|DELETE|PATCH|OPTIONS|HEAD)\s+([^"]*/api/[^"]*)\s+HTTP/\d\.\d"'

def scan_log(filepath, mode, show_count=False, export_file=None):
    occurrence = 0
    results = []

    if mode == "ip":
        pattern = IP_PATTERN
    elif mode == "url":
        pattern = URL_PATTERN
    elif mode == "errors":
        pattern = ERRORS_PATTERN

    else:
        print("Invalid mode.")
        return

    lines = read_txt(filepath)

    if not lines:
        return

    for i, line in enumerate(lines):
        matches = regex.findall(pattern, line)
        for match in matches:
            occurrence += 1
            line = regex.sub(match, f"\033[1;31m{match}\033[0m", line)
            results.append(f"{i+1}: {line}")

    if show_count:
        print(f"Total matches: {occurrence}")
    else:
        for result in results:
            print(result.strip())

    if export_file:
        content = "".join(results) + "\n"
        write_txt(export_file, content)


def show_stats(filepath, export_file=None):
    results = []
    ips = set()
    endpoints = []
    errors_count = 0
    respond_sizes = []

    lines = read_txt(filepath)

    if not lines:
        return

    for line in lines:
        ip_matches = regex.findall(IP_PATTERN, line)
        for ip_match in ip_matches:
            ips.add(ip_match)

        endpoint_match = regex.search(URL_PATTERN, line)
        if endpoint_match:
            endpoints.append(endpoint_match.group(1))

        if regex.search(ERRORS_PATTERN, line):
            errors_count += 1
        
        respond_size_match = regex.search(RESPONSE_SIZE_PATTERN, line)
        if respond_size_match:
            respond_sizes.append(int(respond_size_match.group(1)))


    endpoint_counter = Counter(endpoints)
    most_requested = endpoint_counter.most_common(1) 

    if lines:
        error_rate = (errors_count / len(lines)) * 100
    else:
        error_rate = 0.00

    if respond_sizes:
        avg_respond_size = sum(respond_sizes) / len(respond_sizes)
    else:
        avg_respond_size = 0.00

    results.append(f"Number of unique IPs: {len(ips)}")

    if most_requested:
        endpoint, count = most_requested[0]
        results.append(f"Most requested endpoint: {endpoint} ({count} requests)")
    else:
        results.append("No endpoints found.")

    results.append(f"Error rate is: {error_rate:.2f}%")

    results.append(f"Average respond size is: {avg_respond_size:.2f} bytes")

    for result in results:
        print(result.strip())

    if export_file:
        content = "\n".join(results) + "\n"
        write_txt(export_file, content)
    

def clean_log(filepath, remove_ip=None, remove_timestamps=None, 
              mask_email=None, extract_api=None, export_file=None):
    results = []

    lines = read_txt(filepath)

    if extract_api:
        for line in lines:
            if regex.search(API_PATTERN, line):
                results.append(line)
    else:
        results = lines
        

    if not lines:
        return

    if remove_ip:
        results = [regex.sub(IP_PATTERN, "", result) for result in results]

    if remove_timestamps:
        results = [regex.sub(TIMESTAMP_PATTERN, "", result) for result in results]

    if mask_email:
        results = [regex.sub(EMAIL_PATTERN, "[REDACTED EMAIL]", result) for result in results]

    for result in results:
        print(result.strip())
    
    if export_file:
        content = "".join(results) + "\n"
        write_txt(export_file, content)


def monitor_log(filepath, contains=None):
    pattern = regex.compile(contains) if contains else None

    try:
        with open(filepath, 'r') as file:
            file.seek(0, 2)
            try:
                while True:
                    line = file.readline()
                    if not line:
                        time.sleep(0.1)
                        continue

                    line = line.rstrip()
                    if pattern:
                        if pattern.search(line):
                            print(line)
                    else:
                        print(line)
            except KeyboardInterrupt:
                print("Quitting monitoring...")
    except FileNotFoundError:
        print(f"File was not found!: '{filepath}'")



def read_txt(filepath):
    try:
        with open(filepath, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"File was not found!: '{filepath}'")
        return
    

def write_txt(filepath, content):
    with open(filepath, 'w') as file:
        file.write(content)
    print(f"Results saved to '{filepath}'")

    

def main():
    parser = argparse.ArgumentParser(description="LogMaster for IPs, URLs, Errors and more!")
    subparsers = parser.add_subparsers(dest="command", required=True)

    scan = subparsers.add_parser("scan", help="Scan a file!")
    scan.add_argument("--file", required=True, help="Path to the file you want to scan!")
    scan.add_argument("--count", action="store_true", help="Print only the count of matches!")
    scan.add_argument("--export", metavar="FILE", help="Save results to a file!")
    scan_group = scan.add_mutually_exclusive_group(required=True)
    scan_group.add_argument("--ip", action="store_true", help="Extract IPs")
    scan_group.add_argument("--url", action="store_true", help="Extract URLs")
    scan_group.add_argument("--errors", action="store_true", help="Extract Errors")

    stats = subparsers.add_parser("stats", help="Generate statistics from a file!")
    stats.add_argument("--file", required=True, help="Path to the file you want to scan!")
    stats.add_argument("--export", metavar="FILE", help="Save results to a file!")

    clean = subparsers.add_parser("clean", help="Cleans up your log a bit!")
    clean.add_argument("--file", required=True, help="Path to the file you want to scan!")
    clean.add_argument("--remove-ip", action="store_true", help="Removes all IPs from log!")
    clean.add_argument("--remove-ts", action="store_true", help="Removes all Timestamps from log!")
    clean.add_argument("--mask-email", action="store_true", help="Maks all Emails from log!")
    clean.add_argument("--extract-api", action="store_true", help="Extracts only /api/ requests!")
    clean.add_argument("--export", metavar="FILE", help="Save results to a file!")
    
    monitor = subparsers.add_parser("monitor", help="Live tail a log file")
    monitor.add_argument("--file", required=True, help="Path to the log file to follow")
    monitor.add_argument("--contains", help="Only print lines matching this regex")


    args = parser.parse_args()

    if args.command == "scan":
        if args.ip:
            scan_log(args.file, "ip", show_count=args.count, export_file=args.export)
        elif args.url:
            scan_log(args.file, "url", show_count=args.count, export_file=args.export)
        elif args.errors:
            scan_log(args.file, "errors", show_count=args.count, export_file=args.export)

    if args.command == "stats":
        show_stats(args.file, export_file=args.export)

    if args.command == "clean":
        clean_log(args.file, remove_ip=args.remove_ip, remove_timestamps=args.remove_ts, 
                  mask_email=args.mask_email, extract_api=args.extract_api, export_file=args.export)

    if args.command == "monitor":
        monitor_log(args.file, contains=args.contains)

if __name__ == "__main__":
    main()