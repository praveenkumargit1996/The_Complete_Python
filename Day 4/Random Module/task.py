import random

# Random numbers of integers from 1 to 10
random_integer = random.randint(1, 10)
print(random_integer)

# Random numbers of float from 1 to 10
random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

# Random numbers of float from 1 to 10
random_float = random.uniform(1, 10)
print(random_float)

# Random numbers of integers for Heads & tails
random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")


