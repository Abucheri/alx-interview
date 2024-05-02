#!/usr/bin/python3

import sys
import re
from collections import OrderedDict
from datetime import datetime


# Initialize variables to store metrics
total_file_size = 0
status_code_counts = OrderedDict.fromkeys(
        [200, 301, 400, 401, 403, 404, 405, 500], 0)
line_count = 0


def print_statistics():
    """Prints current totals of file size and status code counts."""
    print("File size:", total_file_size)
    for code, count in status_code_counts.items():
        if count > 0:
            print("{}: {}".format(code, count))


try:
    for line in sys.stdin:
        line_count += 1

        # Parse log entry using regular expression
        match = re.match(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\]'
                         r'"GET /projects/260 HTTP/1\.1" (\d+) (\d+)$',
                         line.strip())
        if match:
            # Extract relevant information from the log entry
            ip_address, timestamp, status_code, file_size = match.groups()

            # Check timestamp format
            try:
                datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')
            except ValueError:
                sys.stderr.write("{}: {}: invalid timestamp format\n"
                                 .format(sys.argv[0], line_count))

            # Check URL
            if status_code != '200':
                sys.stderr.write("{}: {}: unexpected HTTP status code\n"
                                 .format(sys.argv[0], line_count))

            # Update metrics
            total_file_size += int(file_size)
            status_code = int(status_code)
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

            if line_count % 10 == 0:
                print_statistics()
except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print_statistics()
