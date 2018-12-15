# A module is basically a file containing a set of functions to include in your application. 
# There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules.

# Core modules
import datetime
# if you don't need everything in a module (datetime), you can import specific methods (just date)
from datetime import date 
# today = datetime.date.today() since we imported only the method we wanted we can shorten the statement
today = date.today()
print(today)

# more core modules
import time
from time import time

timestamp = time()

# Pip module (pip is a python package manager, similar to npm). These need to be installed separately.
from camelcase import CamelCase
c = CamelCase()
print(c.hump('hello there world'))

# Import custom module. This is a custom file (validator.py) with one or more functions available to import.
# Again, you can import the whole file or just the specific methods you want (validate_email)
import validator
from validator import validate_email

email = 'test#test.com'
if validate_email(email):
  print('Email is valid')
else:
  print('Email is bad')