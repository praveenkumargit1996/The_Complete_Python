
# defining user-defined functions
def my_function():
    print("Hello")
    print("Praveen")

# calling the function
my_function()

# for loops
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for n in range(1,6):
    print(n)

# while loop
num_of_hurdals =6

def jump():
    print("jump")

while not num_of_hurdals>0:
    jump()
    num_of_hurdals -= 1

#Robot hardle challenge Hadle 1- https://reeborg.ca/reeborg.html?
# def turn_around():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_around()
#     move()
#     turn_around()
#     move()
#     turn_left()
#
# for step in range(6):
#  jump()

#Robot hardle challenge Hadle 3- https://reeborg.ca/reeborg.html?

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# while not at_goal():
#   if wall_in_front():
#      jump()
#   else :
#     move()

#Robot hardle challenge Hadle 4- https://reeborg.ca/reeborg.html?
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#          move()
#     turn_left()
#
# while not at_goal():
#   if wall_in_front():
#      jump()
#   else :
#     move()


#Robot hardle challenge hard level maze - https://reeborg.ca/reeborg.html?
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def moveforward():
#     while front_is_clear() and not at_goal():
#         move()
#         if not wall_on_right():
#             turn_right()
#
#
# while not at_goal():
#     if wall_in_front():
#         turn_left()
#     elif front_is_clear():
#         moveforward()