bmi = 84 / 1.65 ** 2
print(bmi)

# rounding of the int values
print(int(bmi))
print(round(bmi))
print(round(bmi,2))

score = 0

# user scores a point , need to add-on to previous
score += 1
print(score)

# normal printing  without f-string
print("your score is: " + str(score))

# f- strings (means mix string with different data)
print(f"your score is = {score}")

score = 6
height = 1.8
is_winning = True

print(f"Your score is = {score},your height is {height},you are winning is {is_winning} ")
