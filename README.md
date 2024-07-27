# veridian-api-python-sdk

A simple SDK to clean tabular data using Veridian's remote API. This SDK allows you to clean CSV and Excel files by calling a remote API that processes the data and returns cleaned data in JSON format.

## Features

- Supports CSV and XLS/XLSX files.
- Simple and easy-to-use interface.
- Integration with our remote data cleaning API.
- Handles various data cleaning tasks such as handling missing data, outliers, normalization, and intelligent, agentic data cleaning.

## Installation

You can install the Veridian package via pip:

```bash
pip install veridian
```

## Usage

### Basic Usage

Here’s a basic example of how to use the `clean` function provided by the `cleaning_sdk` package:

```python
from veridian import clean

# Your API key
api_key = "your_api_key"

# Path to your CSV or Excel file
file_path = "path_to_your_file.csv"

# Call the clean function
result = clean(file_path, api_key)

# Print the cleaned data
print(result)
```

### Parameters

- `file_path` (str): The path to the CSV or Excel file you want to clean.
- `api_key` (str): Your API key for authentication.
- `additional_param` (optional): Any additional parameter that your API might require.

### Response

The `clean` function returns a JSON object containing the cleaned data and any other relevant information provided by the API.

## Error Handling

If the API call fails, the `clean` function raises an exception with the error message returned by the API. Make sure to handle exceptions appropriately in your code.

```python
try:
    result = clean(file_path, api_key)
    print(result)
except Exception as e:
    print(f"Error: {e}")
```

## License

This project is licensed under the BSD 3-Clause License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

Thanks to all contributors and supporters of this project.
