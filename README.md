# CSV Data Cleaner

Small Python utility that cleans CSV files by:
- removing empty rows,
- trimming whitespace from string columns,
- removing exact duplicate rows,
- filtering out rows missing an `id` column (if present).

## Usage

Install dependency:
```bash
python3 -m pip install --user pandas