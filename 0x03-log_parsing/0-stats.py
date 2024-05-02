#!/usr/bin/python3

import sys
import re
import signal


# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0


def print_statistics():
    """Prints the computed statistics."""
    print("File size:", total_file_size)
    for status_code, count in sorted(status_code_counts.items()):
        if count > 0:
            print("{}: {}".format(status_code, count))


def signal_handler(sig, frame):
    """Handler for keyboard interruption (CTRL + C)."""
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    # Parse log entry using regular expression
    match = re.match(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[([^]]*)\]'
                     r'"GET \/projects\/260 HTTP\/1\.1" (\d+) (\d+)$',
                     line.strip())
    if not line:
        # Break out of the loop if end of input stream is reached
        break
    if match:
        # Extract relevant information from the log entry
        ip_address, _, _, status_code, file_size = match.groups()

        # Update metrics
        total_file_size += int(file_size)
        status_code = int(status_code)
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        line_count += 1
        if line_count % 10 == 0:
            print_statistics()
