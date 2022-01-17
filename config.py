import logging

# Logging level
LOGGING_LEVEL = logging.INFO

# Input files
INPUT_DIR = "input"
INPUT_FILE = "input_file.txt"
JSON_DIR = "json"
STANDARD_DEFINITIONS_FILE = "standard_definition.json"
ERROR_CODES_FILE = "error_codes.json"

# Output files
OUTPUT_DIR = "out"
OUTPUT_REPORT_CSV_FILE = "report.csv"
OUTPUT_SUMMARY_TEXT_FILE = "summary.txt"

# Header containing the columns for the output report csv file
OUTPUT_CSV_HEADER = ["Section","Sub-Section","Given DataType","Expected DataType","Given Length","Expected MaxLength","Error Code"]
