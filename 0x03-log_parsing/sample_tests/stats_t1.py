#!/usr/bin/python3

import sys


if __name__ == "__main__":
    # Initialize variables to store metrics
    file_size = 0
    status_codes = {}
    codes_list = [
        "200", "301", "400", "401", "403", "404", "405", "500"]

    for status in codes_list:
        status_codes[status] = 0

    line_count = 0

    try:
        for line in sys.stdin:
            try:
                inputs = line.split(" ")
                if len(inputs) != 9:
                    pass

                if inputs[-2] in codes_list:
                    status_codes[inputs[-2]] += 1

                if inputs[-1][-1] == '\n':
                    inputs[-1][:-1]

                file_size += int(inputs[-1])
            except Exception:
                pass

            line_count += 1

            if line_count % 10 == 0:
                print("File size: {}".format(file_size))
                for status in sorted(status_codes.keys()):
                    if status_codes[status] != 0:
                        print("{}: {}".format(status, status_codes[status]))

        print("File size: {}".format(file_size))

        for status in sorted(status_codes.keys()):
            if status_codes[status] != 0:
                print("{}: {}".format(status, status_codes[status]))

    except KeyboardInterrupt as e:
        # Handle keyboard interruption (CTRL + C)
        print("File size: {}".format(file_size))

        for status in sorted(status_codes.keys()):
            if status_codes[status] != 0:
                print("{}: {}".format(status, status_codes[status]))
        raise
