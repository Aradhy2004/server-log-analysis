print("Log analyzer initialized")

print("Log analyzer initialized")

with open("server_log.txt", "r") as infile, open("log_summary.txt", "w") as outfile:
    lines = infile.readlines()
    outfile.write(f"Total log entries: {len(lines) - 1}\n")

with open("server_log.txt", "r") as f:
    f.readline()  # skip header

    for line in f:
        parts = [p.strip() for p in line.split("|")]
        if len(parts) != 5:
            continue

        datetime, level, message, ip, code = parts

import re

ip_pattern = re.compile(r'(?:\d{1,3}\.){3}\d{1,3}')
error_pattern = re.compile(r'^[45]\d{2}$')

error_count = 0

with open("server_log.txt", "r") as f:
    f.readline()

    for line in f:
        parts = [p.strip() for p in line.split("|")]
        if len(parts) != 5:
            continue

        ip = parts[3]
        code = parts[4]

        if error_pattern.match(code):
            error_count += 1

from collections import Counter

unique_ips = set()
code_counter = Counter()
level_counter = Counter()

with open("server_log.txt", "r") as f:
    f.readline()

    for line in f:
        parts = [p.strip() for p in line.split("|")]
        if len(parts) != 5:
            continue

        _, level, _, ip, code = parts

        unique_ips.add(ip)
        code_counter[code] += 1
        level_counter[level] += 1




