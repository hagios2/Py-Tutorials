from sys import argv

script, fileName = argv

def myfucn(inputFile):
    
    print(inputFile.read()+"\n")

def rewind(inputFile):
    
    inputFile.seek(0)
    
def print_by_line(line, inputFile):
    print(line, inputFile.readline())

print(f"Displaying the content of {fileName}")

user_input_file = open(fileName)

myfucn(user_input_file)

print("Rewinding the file\n")

rewind(user_input_file)

print("Displaying file content by line\n")

print_by_line(1, user_input_file)

print("Displaying file content by line\n")

print_by_line(2, user_input_file)

print("Displaying file content by line\n")

print_by_line(3, user_input_file)

print("Closing file .....\n")

user_input_file.close()

print("file closed")