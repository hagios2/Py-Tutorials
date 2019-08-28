""" print("Hello World!")
print("Hello Again")
print("I like typing this.")
print("This is fun.")
print('Yay! Printing.')
print('\n')
print("I'd much rather you 'not'.")
print('I "said" do not touch this.')

print("Roosters", 100 - 25 * 3 % 4)

print(3+2 < 5-7)
 """
""" 
types_of_people = 20

x = f"there are {types_of_people} types of people in this nation"

binary = "binary"

doNot = "don't"

y = f"those who know {binary} and those who {doNot}"

print(x)

print(y)

print(f"I said: {x}")

print(f"I also said: {y}")

hilarious = True

joke_elavation = "Isn't that joke so funny?! {}" # {} is used to echo a variable in a string
 """
""" print(joke_elavation.format(hilarious)) """ #formart the already formated string

""" end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1 + end2 + end3 + end4 + end5 + end6, end=' ') #end=" " changes the defualt newline to string space

print(end7 + end8 + end9 + end10 + end11 + end12) """
""" 
formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))

print(formatter.format('one', 'two', "three", "four"))

print(formatter.format(formatter, formatter, formatter, formatter))

print(formatter.format(

    "Try your", 
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
)) """
x = '''
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
'''
""" print(x) """
#use print with (""" """) to span a string on multiple lines as typed

""" 
age = input('How old are you? ')

age_in_10_years = int(age) + 10

future_age = f"age in 10 years will be {age_in_10_years}"

print(future_age) """

""" from sys import argv #module or library

script, first, second = argv

third = input("Enter third value:\n")

print("The script is called ", script)

print('Your first variable is: ', first)

print('Your second variable is: ', second)

print('Your third variable is: ', third) """

a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b