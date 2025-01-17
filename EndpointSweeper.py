import os
import sys
import time

def filter_vulnerable_endpoints(input_file: str, output_file: str, keywords: list, threads: int = 1):
    """
    Filters potentially vulnerable endpoints from a given text file based on keywords.

    Args:
        input_file (str): Path to the input text file containing endpoints.
        output_file (str): Path to save the filtered endpoints.
        keywords (list): List of keywords to identify vulnerable endpoints.
        threads (int): Number of threads to use for processing (currently unused, placeholder for future enhancements).

    Returns:
        int: The number of vulnerable endpoints found.
    """
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file '{input_file}' does not exist.")

    with open(input_file, 'r') as file:
        lines = file.readlines()

    total_lines = len(lines)
    filtered_endpoints = []

    print("\nProcessing...")
    for idx, line in enumerate(lines, start=1):
        if any(keyword in line for keyword in keywords):
            filtered_endpoints.append(line.strip())
        progress = (idx / total_lines) * 100
        sys.stdout.write(f"\rProgress: {progress:.2f}% ({idx}/{total_lines})")
        sys.stdout.flush()

    print("\nFiltering complete.")

    # Save the filtered endpoints to the output file
    with open(output_file, 'w') as output:
        output.write('\n'.join(filtered_endpoints))

    return len(filtered_endpoints)

if __name__ == "__main__":
    print(r"""
     ____|_ __   __| |_ __   ___ (_)_ __ | |_/ ___|_      _____  ___ _ __   ___
    |  _| | '_ \ / _` | '_ \ / _ \| | '_ \| __\___ \ \ /\ / / _ \/ _ \ '_ \ / _ \
    | |___| | | | (_| | |_) | (_) | | | | | |_ ___) \ V  V /  __/  __/ |_) |  __/
    |_____|_| |_|\__,_| .__/ \___/|_|_| |_|\__|____/ \_/\_/ \___|\___| .__/ \___|
                      |_|                                    |_|               
    """)

    import argparse

    parser = argparse.ArgumentParser(description="Filter potentially vulnerable endpoints from a text file.")
    parser.add_argument("input_file", type=str, help="Path to the input text file containing endpoints.")
    parser.add_argument("threads", type=int, help="Number of threads to use for processing.")
    parser.add_argument("output_file", type=str, help="Path to save the filtered endpoints.")
    parser.add_argument(
        "--keywords", 
        type=str, 
        nargs='+', 
        default=["login", "admin", "test", "debug", "config", "query", "?", "http://", "mailto:", "/test", "/debug", "env"],
        help="List of keywords to identify vulnerable endpoints (default keywords are provided)."
    )

    args = parser.parse_args()

    try:
        count = filter_vulnerable_endpoints(args.input_file, args.output_file, args.keywords, args.threads)
        print(f"\nSuccessfully filtered {count} potentially vulnerable endpoints.")
        print(f"Filtered endpoints saved to '{args.output_file}'.")
    except Exception as e:
        print(f"Error: {e}")
