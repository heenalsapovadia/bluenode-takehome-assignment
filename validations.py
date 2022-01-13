# validations.py
# contains all functions for validations

# Validation function to check the data_type and return the data type of the given input string
def dataTypeCheck (exp_dtype, string) :
    string = string.replace(" ", "")
    string_type = 'digits' if string.isdigit() else 'word_characters' if string.isalpha() else ''
    digits = string.isdigit() and (exp_dtype == 'digits')
    chars = string.isalpha() and (exp_dtype == 'word_characters')
    if digits or chars:
        return True,string_type
    else:
        return False,string_type

# Validation function to check the length of the input string
def maxLengthCheck (exp_length, string) :
    return True if (len(string) <= exp_length) else False

# Function to find the appropriate error code
def findErrorCode (dtCheck, maxlCheck) :
    if dtCheck and maxlCheck:
        return 'E01'
    elif (not dtCheck) and maxlCheck:
        return 'E02'
    elif dtCheck and (not maxlCheck):
        return 'E03'
    elif (not dtCheck) and (not maxlCheck):
        return 'E04'
    return ''
