# Creator JM 10/18/22

# Get beast and dish
beast = input('Beast: ').lower()
dish = input('Dish: ').lower()

# Conditional
if beast[0] == dish[0] and beast[0] == dish[len(dish) - 1]:
    print('True')
else:
    print('False')
