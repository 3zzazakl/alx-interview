#!/usr/bin/python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""
import sys


def parse_log_line(line):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    try:
        parts = line.split('"')
        if len(parts) < 3:
            return None

        status_code = int(parts[2].split()[-2])
        file_size = int(parts[2].split()[-1])
        return status_code, file_size
    except (IndexError, ValueError):
        return None


def print_stats(total_size, status_codes):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    print(f"File size: {total_size}")
    for status_code in sorted(status_codes.keys()):
        print(f"{status_code}: {status_codes[status_code]}")


def main():
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            result = parse_log_line(line)
            if result is None:
                continue

            status_code, file_size = result
            if status_code in status_codes:
                status_codes[status_code] += 1
                total_size += file_size

            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
