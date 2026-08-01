# task1 : print the string
print("hello world!")


# task2 :print the strings in the new lines
print("Hello world!\nHello world!\nHello world!")

print("Hello"+" "+"praveen")


# task3 :print statement with User input
print("Hello "+ input("what is your name?")+"!")

# task4 :Print string length in one line
print(len(input("What is your name?")))

# Print string length using variables
username=input("What is your name?")
length=len(username)
print(length)

# task5 :Print string length in one line using typecast
user_name = "Praveen"
length = len(user_name)
print("Length of the user name is "+ str(length))

# task6 : combine and print the user inputs
print("Welcome to the Band name generator.")
city=input("which city did you grown up in?\n")
pet_name=input("which is your favorite pet?\n")
print("your band name could be: " + city + " " + pet_name)
