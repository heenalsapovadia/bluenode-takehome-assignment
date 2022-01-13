# file_ops.py
# all functions related to reading files and loading data
import json

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