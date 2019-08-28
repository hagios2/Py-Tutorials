import sys

#get scrit, encoding and errors from commandline before the script runs
script, input_encoding, error = sys.argv

#define function main with actual params
def main(language_file, encoding, errors):
    
    #read language fie by line
    line = language_file.readline()

    if line:

        #call function function print_line with gven args
        print_Line(line, encoding, errors)

        #return a value from main
        return main(language_file, encoding, errors)

#defining function print_line with actual params
def print_Line(line, encoding, errors):

    next_lang = line.strip();

    #get the a
    raw_bytes = next_lang.encode(encoding, errors=errors)

    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open('languages.txt', encoding="utf-8")

main(languages, input_encoding, error)