# Creator JM 10/11/22

# Initial Variable
school = 'Fairfield Prep'

# Using .split
first_half, second_half = school.split(' ')

# Or with slicing
first_half = school[:9]
second_half = school[9:]

# print the halves
print(first_half)
print(second_half)

# joined result
print(first_half + second_half)