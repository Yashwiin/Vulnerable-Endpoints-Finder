# Vulnerable Endpoints Filter Tool

This repository contains a Python tool for filtering potentially vulnerable endpoints from a text file. It identifies URLs or paths containing specific keywords that may indicate vulnerability, such as `login`, `admin`, or `debug`. The tool is simple, extensible, and designed to be a starting point for enhancing endpoint security analysis.

## Features

- Filters endpoints based on user-defined or default keywords.
- Supports input and output files for flexible use.
- Provides a command-line interface (CLI) for easy integration into workflows.
- Validates file paths to prevent errors.

## Requirements

- Python 3.6+

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/vulnerable-endpoints-filter.git
   cd vulnerable-endpoints-filter
   ```

2. Install any required dependencies (if applicable).

## Usage

Run the tool using the following command:

```bash
python3 EndpointSweeper.py <input_file> <threads> <output_file> [--keywords <keyword1> <keyword2> ...]
```

### Positional Arguments:
- `<input_file>`: Path to the input text file containing endpoints.
- `<threads>`: Number of threads to use (currently unused, placeholder for future enhancements).
- `<output_file>`: Path to save the filtered endpoints.

### Optional Arguments:
- `--keywords`: List of keywords to identify vulnerable endpoints. Defaults are provided:
  ```
  ["login", "admin", "test", "debug", "config", "query", "?", "http://", "mailto:", "/test", "/debug", "env"]
  ```

### Example:

```bash
python3 EndpointSweeper.py endpoints.txt 10 filtered_endpoints.txt --keywords login admin test
```

This will filter the endpoints in `endpoints.txt`, identifying any containing the keywords `login`, `admin`, or `test`. The results will be saved to `filtered_endpoints.txt`.

## Future Enhancements

- Implement multithreading for faster processing of large files.
- Add support for regular expression-based filtering.
- Integrate with vulnerability scanners for automated analysis.
- Add a web-based interface for easier use by non-technical users.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## Disclaimer

This tool is intended for educational and informational purposes only. The authors are not responsible for any misuse or damages caused by this tool.
