from sys import argv

script, copy_from, copy_to = argv

#copying contents from one file (sample.txt)
content = open(copy_from).read()

#now pasting the copied content in to another file (sample1.txt)
newFile = open(copy_to, 'w').write("Copied Content\n" + content)

if newFile:

    print("Contents were successfully copied") 