import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇



print(type(names))

names_length = len(names)
print(names_length)

random_payer = random.randint(0, names_length - 1)

print(random_payer)

random_human = names[random_payer]

print(f'{random_human} is going to byu the meal today!')