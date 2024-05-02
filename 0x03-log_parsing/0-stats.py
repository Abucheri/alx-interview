#!/usr/bin/python3

import sys


def print_statistics(status_code_counts, total_file_size):
    """Prints current totals of file size and status code counts."""
    print("File size: {}".format(total_file_size))
    for key, val in sorted(status_code_counts.items()):
        if val != 0:
            print("{}: {}".format(key, val))


# Initialize variables to store metrics
total_file_size = 0
status_code = 0
line_count = 0
status_code_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        read_line = line.split()
        read_line = read_line[::-1]

        if len(read_line) > 2:
            line_count += 1

            if line_count <= 10:
                total_file_size += int(read_line[0])
                status_code = read_line[1]

                if (status_code in status_code_counts.keys()):
                    status_code_counts[status_code] += 1

            if (line_count == 10):
                print_statistics(status_code_counts, total_file_size)
                line_count = 0

finally:
    # Handle keyboard interruption (CTRL + C)
    print_statistics(status_code_counts, total_file_size)
