print("Log analyzer initialized")

print("Log analyzer initialized")

with open("server_log.txt", "r") as infile, open("log_summary.txt", "w") as outfile:
    lines = infile.readlines()
    outfile.write(f"Total log entries: {len(lines) - 1}\n")

