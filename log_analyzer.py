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


