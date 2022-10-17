# Creator JM 10/11/22

# Get 2 strings from the user
string1 = input('First word: ')
string2 = input('Second word: ')

# Compare the strings
if string1 < string2: # s1 greater than s2
    print(f'{string1} comes before {string2}')
elif string1 > string2: # s2 greater than s1
    print(f'{string1} comes after {string2}')
else:
    print('Both words are equal')