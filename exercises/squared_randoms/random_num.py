import random

number = random.randint(0,49)
random_numbers = [random.randint(0,49) for _ in range(20)]
print(random_numbers)

squared = [ num**2 for num in random_numbers ]
print(squared)