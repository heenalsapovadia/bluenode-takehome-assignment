# file_ops.py
# all functions related to reading files and loading data
import os
import json
import csv
import logging

from config import *

# Function to load json file in a dictionary
def load_json (file, key, value) :
    if not os.path.isdir(JSON_DIR):
        logging.error('Could not find the JSON DIRECTORY : %s', JSON_DIR)
        exit()
    
    file_data_path = os.path.join(JSON_DIR, file)
    if not os.path.exists(file_data_path):
        logging.error('Could not find the JSON FILE at : %s', file_data_path)
        exit()

    file_data = open(file_data_path)
    file_data = json.load(file_data)
    dictionary = {}
    for obj in file_data:
        dictionary[obj[key]] = obj[value]
    return dictionary

# Function to load the input text file
def load_input (file) :
    if not os.path.isdir(INPUT_DIR):
        logging.error('Could not find the INPUT DIRECTORY : %s', INPUT_DIR)
        exit()

    input_file_path = os.path.join(INPUT_DIR, file)
    if not os.path.exists(input_file_path):
        logging.error('Could not find the INPUT FILE at : %s', input_file_path)
        exit()

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