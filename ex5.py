import sys

#get scrit, encoding and errors from commandline before the script runs
script, input_encoding, error = sys.argv

#define function main with actual params
def main(language_file, encoding, errors):
    
    #read language file by line
    line = language_file.readline()


    #return false if line is empty(ie, end of the file) else true    
    if line:

        #call function function print_line with gven args
        print_Line(line, encoding, errors)

        #return a value from main
        return main(language_file, encoding, errors)

#defining function print_line with actual params
#encoding = condec ie changing the encoding requires a codec to use in place of the default
def print_Line(line, encoding, errors):

    #strip off '\n\    
    next_lang = line.strip();

    #encode the strings (languages into raw bytes)
    raw_bytes = next_lang.encode(encoding, errors=errors)

    #decode the raw bytes into strings  (which is also equal to next_lang)   
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    #print the raw_codes with tthe equivalent strings    
    print(raw_bytes, "<===>", next_lang)#cooked_string)

#opening language.txt file for reading
languages = open('language.txt', encoding="utf-8")

#execute main function
main(languages, input_encoding, error)