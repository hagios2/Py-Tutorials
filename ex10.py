ten_things = "Apples Oranges Crows Telephon Light Sugar";

print("Wait there are not 10 things in that list. let's fix that.")

stuff = ten_things.split(' ');

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()

    print("Adding: ", next_one)

    stuff.append(next_one)

    print(f"There are {len(stuff)} items now")


print("There we go: ", stuff)

print("Let's do some things with stuff")

#print the second item in the list
print(stuff[1])

#print the last itme in the list
print(stuff[-1])

#the first on the stack which is actually the last in the list
print(stuff.pop())

print(' '.join(stuff))

print('#'.join(stuff[3:5]))