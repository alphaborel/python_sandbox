# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Tony'
age = 37

# Concatenate (you can only concat string variables)
print('Hello, my name is ' + name + ' and I am ' + str(age))

# **** String Formatting ****
# Arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-String (python 3.6+)
print(f'Howdy, my name is {name} and I am {age}')

# ***** 14 String Methods (there are more) ******

s = 'hello world'

# Capitalize string
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower case
print(s.lower())

# Swap case
print(s.swapcase())

# Get length. Note: len() can be used on strings, lists, etc to get the length
list = [1,5,6,'hello']
print(len(list))

print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count. Counts the sub-string you put in. In this case it counts all the "h" letters
sub = 'h'
print(s.count(sub))

# Starts with. Returns true or false.
print(s.startswith('hello'))

# Ends with. Returns true or false.
print(s.endswith('d'))

# Split into a list. The default parameter split at the whitespace.
print(s.split())

# Find position. Finds the position of the first character then stops.
print(s.find('r'))

# Is all alphanumeric. Returns True or False. Note that any spaces will make this return False.
print(s.isalnum())

# Is all alphabetic. Returns True or False. Note that any spaces will make this return False.
print(s.isalpha())

# Is all numeric. Returns True or False.
print(s.isnumeric())