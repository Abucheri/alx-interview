#!/usr/bin/python3


def print_statistics(total_file_size, code_counts):
    """Prints current totals of file size and status code counts."""
    print("File size:", total_file_size)
    for code in code_counts:
        if code_counts[code] > 0:
            print("{}: {}".format(code, code_counts[code]))


if __name__ == "__main__":
    from sys import argv, stdin, stderr
    from collections import OrderedDict
    from datetime import datetime

    # Initialize variables to store metrics
    total_file_size = 0
    status_code_counts = OrderedDict.fromkeys([200, 301, 400, 401, 403,
                                              404, 405, 500], 0)
    line_count = 0

    try:
        for line in stdin:
            line_count += 1

            line_input = line.split('-', 1)
            if len(line_input) != 2:
                continue

            # Check timestamp format
            time_format = line_input[1].split(']')
            time_code = time_format[0].lstrip(' [')
            try:
                datetime.strptime(time_code, '%Y-%m-%d %H:%M:%S.%f')
            except ValueError:
                stderr.write("{}: {}: invalid timecode\n".format(
                             argv[0], line_count))
                pass

            # Check URL
            url_check = time_format[1].split('"')
            url_check = url_check[1:]
            if url_check[0] != 'GET /projects/260 HTTP/1.1':
                stderr.write("{}: {}: unexpected HTTP request\n".format(
                             argv[0], line_count))

            # Update metrics
            metrics = url_check[1].lstrip(' ')
            metrics = metrics.rstrip('\n')
            metrics = metrics.split(' ')

            # Check status codes
            if metrics[0].isdecimal():
                status_code = int(metrics[0])
                status_code_counts[status_code] += 1

            # Check file size
            if metrics[1].isdecimal():
                total_file_size += int(metrics[1])

            if line_count % 10 == 0:
                print_statistics(total_file_size, status_code_counts)
        print_statistics(total_file_size, status_code_counts)
    except (KeyboardInterrupt):
        # Handle keyboard interruption (CTRL + C)
        print_statistics(total_file_size, status_code_counts)
        raise
