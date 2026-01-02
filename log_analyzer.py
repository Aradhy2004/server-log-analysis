import re
from collections import Counter

# Counters and data structures
total_logs = 0
unique_ips = set()
code_counter = Counter()
level_counter = Counter()
error_count = 0

# Regex for HTTP error codes (4xx, 5xx)
error_pattern = re.compile(r'^[45]\d{2}$')

# Read and analyze log file
with open("server_log.txt", "r") as infile:
    infile.readline()  # skip header

    for line in infile:
        parts = [p.strip() for p in line.split("|")]
        if len(parts) != 5:
            continue

        _, level, _, ip, code = parts

        total_logs += 1
        unique_ips.add(ip)
        code_counter[code] += 1
        level_counter[level] += 1

        if error_pattern.match(code):
            error_count += 1

# Write final summary ONCE
with open("log_summary.txt", "w") as outfile:
    outfile.write("SERVER LOG SUMMARY\n")
    outfile.write("=================\n\n")

    outfile.write(f"Total log entries: {total_logs}\n")
    outfile.write(f"Unique IPs: {len(unique_ips)}\n")
    outfile.write(f"Error responses (4xx & 5xx): {error_count}\n\n")

    outfile.write("HTTP Code Frequency:\n")
    for code, count in code_counter.items():
        outfile.write(f"{code}: {count}\n")

    outfile.write("\nLog Level Frequency:\n")
    for level, count in level_counter.items():
        outfile.write(f"{level}: {count}\n")

print("Log analysis complete. Summary written to log_summary.txt")



