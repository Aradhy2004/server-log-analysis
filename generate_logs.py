from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

LOG_FILE = "server_log.txt"
ROWS = 1000

levels = ["INFO", "WARNING", "ERROR", "DEBUG"]
codes = {
    "INFO": [200, 201],
    "WARNING": [400, 404],
    "ERROR": [500, 503],
    "DEBUG": [200]
}

start_time = datetime.now() - timedelta(days=1)

with open(LOG_FILE, "w") as f:
    f.write("DateTime | Level | Message | IP | Code\n")

    for i in range(ROWS):
        level = random.choice(levels)
        timestamp = start_time + timedelta(seconds=i)

        f.write(
            f"{timestamp} | "
            f"{level} | "
            f"Sample log message | "
            f"{fake.ipv4()} | "
            f"{random.choice(codes[level])}\n"
        )

print("server_log.txt generated")
