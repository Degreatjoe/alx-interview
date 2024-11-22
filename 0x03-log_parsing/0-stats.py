#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics:
- Total file size
- Count of lines by status code
"""

import sys


def print_stats(total_size, status_counts):
    """
    Prints the current statistics.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def main():
    """
    Reads stdin line by line and computes metrics.
    """
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
                     404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            try:
                # Parse the line
                parts = line.split()
                if len(parts) < 7:
                    continue
                ip, _, _, date, request, status, size = parts[0],
                parts[1], parts[2], parts[3], parts[4:6],
                parts[-2], parts[-1]

                # Ensure valid status code and size
                status = int(status)
                size = int(size)

                # Update metrics
                total_size += size
                if status in status_counts:
                    status_counts[status] += 1

                line_count += 1

                # Print stats every 10 lines
                if line_count % 10 == 0:
                    print_stats(total_size, status_counts)

            except (ValueError, IndexError):
                # Skip lines with unexpected format
                continue

    except KeyboardInterrupt:
        # Print stats on keyboard interruption
        print_stats(total_size, status_counts)
        raise

    # Print stats at the end of input
    print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
