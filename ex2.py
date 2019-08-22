from sys import argv
""" 
script, userName, school = argv

prompt = '> '

print(f"Hi {userName}, I'm the {script} script.")

print("I'd like ask you a few questions.")

print(f"Do you like me {userName}?")

likes = input(prompt)

print(f"Where do you live {userName}?")
lives = input(prompt)

print(f"What kind of computer do you have?")

computer = input(prompt)

print(f"""
#Alright, so you said {likes} about liking me.
#You live in {lives} and you're a student of {school}. Not sure where that is.
#And you have a {computer}. Nice.
#""") """

script, fileName = argv

prompt = ">> "

print('Do you want to clear content of the file?')
reply = input(prompt)

if reply == "Yes" or reply == "yes":
    #open the file
    fileToOpen = open(fileName, 'w')
    
    fileToOpen.truncate()
    fileToOpen.close()
    
    print("File content was cleared successfully")

else:
    print('Do you want to write to the file?')
    reply = input(prompt)

    if reply == "Yes" or reply == "yes":
        
        print('Enter the content for the file')
        
        content = input(prompt)
        
        fileToOpen = open("sample.txt", 'a')

        fileToOpen.write("\n"+content)

        fileToOpen.close()

        print("Your contents have been saved to file")

    else:

        print("Nothing happened to file")        


