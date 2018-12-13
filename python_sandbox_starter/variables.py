# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""
# Note: No semicolins for statements in Python

# x = 1           # int
# y = 2.5         # float
# name = 'tony'   # str
# is_cool = True  # bool

# Multiple assignment
x, y, name, is_cool = (1, 2.5, 'Tony', True)

# Basic math
a = x + y
print(a)

# casting (changing variable type)
x = str(x)
y = int(y)

print(type(y), y)