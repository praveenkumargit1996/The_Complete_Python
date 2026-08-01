len("Hello")

# to check the Data type
print(type("abc"))
print(type(123))
print(type(3.14159))
print(type(True))

# Type casting
int("123")
print (int("123")+int("456"))

# print (int("abc")+int("456")) ,we can't type caste this different types
# we can type caste of below types
int()
float()
str()
bool()

# run with out error
# print("Number of letters in your name: " + len(input("Enter your name"))
name_of_the_user=input("Enter your name")
length_of_name=len(name_of_the_user)

print(type("Number of letters in your name: ")) #str
print(type(length_of_name)) #int

print("Number of letters in your name: " + str(length_of_name))