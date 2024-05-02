#!/usr/bin/python3


import sys


if __name__ == "__main__":
    # Initialize variables to store metrics
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
    line_count = 1
    total_file_size = 0

    def parse_line(args):
        """read abd get data"""
        try:
            parsed_line = args.split()
            status_code = parsed_line[-2]
            if status_code in status_code_counts.keys():
                status_code_counts[status_code] += 1
            return int(parsed_line[-1])
        except Exception:
            return 0

    def print_statistics():
        """Prints current totals of file size and status code counts."""
        print("File size: {}".format(total_file_size))
        for key in sorted(status_code_counts.keys()):
            if status_code_counts[key]:
                print("{}: {}".format(key, status_code_counts[key]))

    try:
        for line in sys.stdin:
            total_file_size += parse_line(line)
            if line_count % 10 == 0:
                print_statistics()
            line_count += 1
    except KeyboardInterrupt:
        print_statistics()
        raise
    print_statistics()
