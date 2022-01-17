# file_ops.py
# all functions related to reading files and loading data
import json
import csv

from config import *

# Function to load json file in a dictionary
def load_json (file, key, value) :
    file_data = open('./json/'+file)
    file_data = json.load(file_data)
    dictionary = {}
    for obj in file_data:
        dictionary[obj[key]] = obj[value]
    return dictionary

# Function to load the input text file
def load_input (file) :
    with open('./input/'+file) as f:
        file_data = f.read()
    lines = file_data.split("\n")
    return lines

# Function to Write output to Report csv file
def generate_output_report_csv (output_file_path, report_data) :
    with open(output_file_path, 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(OUTPUT_CSV_HEADER)
            writer.writerows(report_data)

# Function to Write output to Summary text file
def generate_output_summary_text (output_file_path, summary_data) :
    with open(output_file_path, 'w') as f:
            f.write('\n'.join(summary_data))