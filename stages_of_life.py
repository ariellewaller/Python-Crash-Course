#   Exercise 5-6. Stages of Life: Write an if-elif-else chain that determines a
#   person’s stage of life. Set a value for the variable age, and then: 


#   If the person is less than 2 years old, print a message that the person is a
#   baby.

#   If the person is at least 2 years old but less than 4, print a message
#   that the person is a toddler.

#   If the person is at least 4 years old but less than 13, print a message that
#   the person is a kid.

#   If the person is at least 13 years old but less than 20, print a message
#   that the person is a teenager.

#   If the person is at least 20 years old but less than 65, print a essage that
#   the person is an adult.

#   If the person is age 65 or older, print a message that the person is an
#   elder.


age = 26

#   Version 1: 

print('Version 1')
if age < 2:
    stage = 'baby'
    print(f"You are a {stage}")
if age >= 2 and age < 4:
    stage = 'toddler'
    print(f"You are a {stage}")
if age >= 4 and age < 13:
    stage = 'kid'
    print(f"You are a {stage}")
if age >= 13 and age < 20: 
    stage = 'teenager'
    print(f"You are a {stage}")
if age >= 20 and age < 65:
    stage = 'adult'
    print(f"You are an {stage}")
if age >= 65:
    stage = 'elder'
    print(f"You are an {stage}")

#   Version 2: 

print('\nVersion 2')
if age < 2:
    stage = 'baby'
    print(f"You are a {stage}")
elif age < 4:
    stage = 'toddler'
    print(f"You are a {stage}")
elif age < 13:
    stage = 'kid'
    print(f"You are a {stage}")
elif age < 20: 
    stage = 'teenager'
    print(f"You are a {stage}")
elif age < 65:
    stage = 'adult'
    print(f"You are an {stage}")
else:
    stage = 'elder'
    print(f"You are an {stage}")





