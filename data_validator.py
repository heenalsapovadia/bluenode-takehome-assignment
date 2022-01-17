import os.path
import logging

from validations import *
from file_ops import *
from config import *

class DataValidator:

    def __init__(self):
        logging.basicConfig(level = LOGGING_LEVEL)

        # Loading jsons into dictionary
        self.def_dict = load_json(STANDARD_DEFINITIONS_FILE, 'key', 'sub_sections')
        self.err_dict = load_json(ERROR_CODES_FILE, 'code', 'message_template')
        logging.info("JSON files loaded")

        # Loading Input data
        self.input = load_input(INPUT_FILE)
        logging.info("INPUT file loaded")

    def create_summary_record (self, message_template, sub_section, section, data_type, max_length) :
        return message_template.replace("LXY", sub_section).replace("LX", section).replace("{", "").replace("}", "").replace("data_type", data_type).replace("max_length", str(max_length))

    def validate_data (self):
        report_data = []
        summary_lines = []

        # Iterating over the input file data line by line
        for line in self.input:
            if len(line) == 0:
                continue
            sections = line.split("&")
            section = sections[0]

            if section not in self.def_dict:
                continue
            rules = self.def_dict[section]
            summary_line = ""

            # Iterating over all the rules for the section
            for r in range(0, len(rules)):
                rule = rules[r]
                sub_section_key = rule['key']
                data_type = rule['data_type']
                max_length = int(rule['max_length'])
                err_code = ''
                given_dt = ''

                # When there is no section in input string for the given rule
                if len(sections)-1 <= r:
                    err_code = 'E05'
            
                    # Creating the csv record for current rule and section
                    report_data.append([section,sub_section_key,given_dt,data_type,'',str(max_length),err_code])
                    msg_template = self.err_dict[err_code]

                    # Creating the summary record for current rule and section
                    summary_line = self.create_summary_record(msg_template, sub_section_key, section, data_type, max_length)
                    if r == len(rules)-1:
                        summary_line = summary_line + "\n"
                    summary_lines.append(summary_line)
                    continue

                sub_section = sections[r+1]

                # Fetching validation values for the input
                dtCheck, given_dt = dataTypeCheck(data_type, sub_section)
                maxLCheck = maxLengthCheck(max_length, sub_section)
                err_code = findErrorCode(dtCheck, maxLCheck)
                
                # Creating the csv record for current rule and section
                report_data.append([section,sub_section_key,given_dt,data_type,str(len(section)),str(max_length),err_code])
                msg_template = self.err_dict[err_code]

                # Creating the summary record for current rule and section
                summary_line = self.create_summary_record(msg_template, sub_section_key, section, data_type, max_length)
                if r == len(rules)-1:
                    summary_line = summary_line + "\n"
                summary_lines.append(summary_line)
        return report_data, summary_lines

    def main(self):
        
        report_data, summary_lines = self.validate_data()
        logging.info("Completed Data Validation")

        # Constructing the output file path
        if not os.path.isdir(OUTPUT_DIR):
            output_dir = os.path.join(os.getcwd(), OUTPUT_DIR)
            logging.info("Creating the OUTPUT DIRECTORY at : %s", output_dir)
            os.mkdir(output_dir)
        output_dir_path = os.path.join(os.getcwd(), OUTPUT_DIR)

        # Writing to report csv file
        output_report_csv_file_path = os.path.join(output_dir_path, OUTPUT_REPORT_CSV_FILE)
        generate_output_report_csv(output_report_csv_file_path, report_data)
        logging.info("Output Report CSV generated at : %s", output_report_csv_file_path)

        # Writing to summary text file
        output_summary_txt_file_path = os.path.join(output_dir_path, OUTPUT_SUMMARY_TEXT_FILE)
        generate_output_summary_text(output_summary_txt_file_path, summary_lines)
        logging.info("Output Summary text generated at : %s", output_summary_txt_file_path)

if __name__=='__main__':
    data_validator = DataValidator()
    data_validator.main()