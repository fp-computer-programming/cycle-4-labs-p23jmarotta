# Creator JM 10/19/22
compliments = {'a':'t','t':'a','c':'g','g':'c'}; series = [] # Define compliemnents dictionary and list
for x in range(0,6): series.append(compliments[input('A, C, T, or G?: ').lower()]) # Get all the letters
print(" ".join([str(x) for x in series])) # Print the joined list