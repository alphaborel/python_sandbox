# Definition: A List is a collection which is ordered and changeable. Allows duplicate members.

# ***** Create list *****
# Shorthand way
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor to create a list
# numbers2 = list((1, 2, 3, 4, 5))

# Get a value (lists start at 0)
print(fruits[1])

# Get length
print(len(fruits))

# Append to list (adds to the end of the list)
fruits.append('Mangos')

# Remove from list (this will find the item anywhere in the list)
fruits.remove('Grapes')

# Remove with pop. Removes an item at the given position.
fruits.pop(2)

# Insert into position (easy enough, put 'Strawberries' in the second position)
fruits.insert(2, 'Strawberries')

# Change value at a certain position
fruits[0] = 'Blueberries'

# Reverse list
fruits.reverse()

# Sort list (and reverse sort too)
fruits.sort()
fruits.sort(reverse=True)

print(fruits)
