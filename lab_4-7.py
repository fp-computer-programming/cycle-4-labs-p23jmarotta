# Creator JM 10/18/22

# Hold the numbers
list = []

# Get all five numbers (make them integers too)
for i in range(0,5):
    list.append(int(input('Insert a number: ')))

# Convert each number to a string, join, then print
numbers_string = " ".join([str(x) for x in list])
print(numbers_string)

# Sort the numbers
list.sort()

# Print the smallest the largest
print(f'Smallest: {list[0]}')
print(f'Largest {list[len(list) - 1]}')