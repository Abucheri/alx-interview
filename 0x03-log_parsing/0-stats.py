#!/usr/bin/python3
"""
This script continuously reads from sys.stdin, processes each line,
and prints statistics for every 10 lines or upon receiving a
keyboard interrupt signal (CTRL + C).
"""

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
    # Process each line from sys.stdin
    for line in sys.stdin:
        # split line into words using split() method, and then reverse
        # using [::-1] so that the last word appears first.
        read_line = line.split()
        read_line = read_line[::-1]

        # If the number of words in the line is greater than 2,
        # it means it's a valid log entry
        if len(read_line) > 2:
            line_count += 1  # Then increment by 1

            # If line_count is less than or equal to 10
            # file size and status code of the current line are updated in
            # total_file_size and status_code_counts dictionary respectively
            if line_count <= 10:
                total_file_size += int(read_line[0])
                status_code = read_line[1]

                if (status_code in status_code_counts.keys()):
                    status_code_counts[status_code] += 1

            # If line_count becomes 10, the current statistics are printed
            # using the print_statistics function, and line_count
            # is reset to 0.
            if (line_count == 10):
                print_statistics(status_code_counts, total_file_size)
                line_count = 0

finally:
    # Handle keyboard interruption (CTRL + C)
    print_statistics(status_code_counts, total_file_size)
