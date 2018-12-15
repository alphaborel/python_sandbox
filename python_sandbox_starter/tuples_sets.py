# Definition: A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Tuples can have any number of items but they cannot be reordered, sorted or changed. Tuples are faster than lists.

# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')

# Using a constructor to create tuple
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# To create a tuple with a single value, you need a trailing comma. Otherwise Python will not recognize it as a tuple
fruits3 = ('Apples',)

# Get value
print(fruits[1])

# Can't change value. This will throw an error.
fruits[0] = 'Pears'

# Delete tuple
del fruits2

# Get length
print(len(fruits))


# Definition: A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set. Returns True or False.
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')

# Remove from set
fruits_set.remove('Grape')

# Add duplicate. Fails silently. Apples is not added twice to set.
fruits_set.add('Apples')

# Clear set. Leaves you with an empty set.
fruits_set.clear()

# Delete. Removes the set all together.
del fruits_set

print(fruits_set)
