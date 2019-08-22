from sys import argv

from os.path import exists

script, copy_from, copy_to = argv

#copying contents from one file (sample.txt)
content = open(copy_from).read()

#now pasting the copied content in to another file (sample1.txt)
open(copy_to, 'w').write(content)

fileContentLenght = len(open(copy_to).read())

if exists(copy_to) and fileContentLenght == len(content):
     
    print("Contents were successfully copied") 