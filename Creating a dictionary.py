#Creating a dictionary of my personal information.
bio={
    "name": "Mariyam Naeem",
    "hometown": "Ajman",
    "age": 17
}

print(bio["name"], bio["hometown"], bio["age"], sep="\n")
 #Handling user input.
name = input("Enter your full name: ")
hometown = input("Enter your hometown: ")

#Handling age input to prevent non-integer errors.
while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("It is not an integer. Try again! ")

bio = {"name": name, "hometown": hometown, "age": age}
print(bio["name"], bio["hometown"], bio["age"], sep="\n")