import csv

from validations import *
from file_ops import *

class DataValidator ():
    def main():
        # Loading jsons into dictionary
        def_dict = load_json('standard_definition.json', 'key', 'sub_sections')
        err_dict = load_json('error_codes.json', 'code', 'message_template')

        # Loading Input data
        lines = load_input('test_input_file.txt')

        report_data = []
        summary_lines = []

        # Iterating over the input file data line by line
        for line in lines:
            if len(line) == 0:
                continue
            sections = line.split("&")
            l = sections[0]

            if l not in def_dict:
                continue
            rules = def_dict[l]
            summary_line = ""

            # Iterating over all the rules for the section
            for r in range(0, len(rules)):
                rule = rules[r]
                sub_section = rule['key']
                data_type = rule['data_type']
                max_length = int(rule['max_length'])
                err_code = ''
                given_dt = ''

                # When there is no section in input string for the given rule
                if len(sections)-1 <= r:
                    err_code = 'E05'
            
                    # Creating the csv record for current rule and section
                    report_data.append([l,sub_section,given_dt,data_type,'',str(max_length),err_code])
                    msg_template = err_dict[err_code]

                    # Creating the summary record for current rule and section
                    summary_line = msg_template.replace("LXY", sub_section).replace("LX", l).replace("{", "").replace("}", "").replace("data_type", data_type).replace("max_length", str(max_length))
                    if r == len(rules)-1:
                        summary_line = summary_line + "\n"
                    summary_lines.append(summary_line)
                    continue

                section = sections[r+1]

                # Fetching validation values for the input
                dtCheck, given_dt = dataTypeCheck(data_type, section)
                maxLCheck = maxLengthCheck(max_length, section)
                err_code = findErrorCode(dtCheck, maxLCheck)
                
                # Creating the csv record for current rule and section
                section_len_str = "" if (len(section)==0) else str(len(section))
                report_data.append([l,sub_section,given_dt,data_type,str(len(section)),str(max_length),err_code])
                msg_template = err_dict[err_code]

                # Creating the summary record for current rule and section
                summary_line = msg_template.replace("LXY", sub_section).replace("LX", l).replace("{", "").replace("}", "").replace("data_type", data_type).replace("max_length", str(max_length))
                if r == len(rules)-1:
                    summary_line = summary_line + "\n"
                summary_lines.append(summary_line)

        # Header containing the columns for the report csv file
        header = ["Section","Sub-Section","Given DataType","Expected DataType","Given Length","Expected MaxLength","Error Code"]

        # Writing to report csv file
        with open('./output/report.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(report_data)

        # Writing to summary text file
        with open('./output/summary.txt', 'w') as f:
            f.write('\n'.join(summary_lines))

if __name__=='__main__':
    DataValidator.main()