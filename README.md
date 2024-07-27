# veridian-api-python-sdk

A simple SDK to clean tabular data using Veridian's remote API.

## Installation

```bash
pip install cleaning_sdk
```

## Usage

```python
from cleaning_sdk import clean

api_key = "your_api_key"
file_path = "path_to_your_file.csv"
result = clean(file_path, api_key)

print(result)
```
