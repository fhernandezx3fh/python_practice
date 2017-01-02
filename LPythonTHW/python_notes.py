
# ********** Python Notes *****************************************************
# Reading documentation
# python -m pydoc raw_input    [-m runs library module as script.
#                               pydoc in this case]
# Max line length = 79
#
#
# Useful Exercises: 16, 
# 
#
#
#

# ********** Useful Imports ***************************************************
from sys import argv
from os.path import exists
# Check to see if file exists
exists(file_name)

from sys import exit
exit(0) # good exit
from random import randint


# ********** Printing *********************************************************
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# We can print these strings a few different ways:
print "Here are the days: ", days
print "Here are the months: ", months

# You can also use format characters
print "Here are the days: %s" % days
# You can also print the string variable directly
print months

# Here is how you print multiple variables on the same print command
print "Here are the days: %s\nHere are the months: %s" % (days, months)

# ********** Prompting ********************************************************
prompt = '> '
print "What kind of computer do you have?"
# Prompt the user to input a computer name and assign to computer variable.
# the prompt variable is the string that the user sees as their prompt string
computer = raw_input(prompt)

# ********** Arguments ********************************************************
from sys import argv
# The first imported argument is always the called python script
script, filename = argv

# ********** Working with Files ***********************************************
# Opening file in write mode
# You can also ope the file in
# Append Mode   'a'
# Read Mode     'r'
target = open(filename, 'w')
target.read()
# Prompt user for a line to input to file
line1 = raw_input("line 1: ")
target.write(line1)

# ********** Dictionaries *****************************************************
# key:value
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# ********** Nested Dictionaries **********************************************
>>> section[4] = {'Title':''},{'Description':''},{'Subsections':[]}
>>> section
{4: ({'Title': ''}, {'Description': ''}, {'Subsections': []})}

# accessing members
>>> section[4][0]
{'Title': ''}
>>> section[4][1]
{'Description': ''}
>>> section[4][2]
{'Subsections': []}

# Unerstanding types
>>> type(section)
<type 'dict'>
>>> type(section[4])
<type 'tuple'>
>>> type(section[4][0])
<type 'dict'>
>>> type(section[4][0]['Title'])
<type 'str'>



# ********** Classes **********************************************************
class X(Y)
"Make a class named X that is-a Y."
class X(object): def __init__(self, J)
"class X has-a __init__ that takes self and J parameters."
class X(object): def M(self, J)
"class X has-a function named M that takes self and J parameters."
foo = X()
"Set foo to an instance of class X."
foo.M(J)
"From foo get the M function, and call it with parameters self, J."
foo.K = Q
"From foo get the K attribute and set it to Q."


# ********** Modules **********************************************************
# When a script is run from python directly, it first assigns __name__ to "__main__"
# This will check to see if the module running is directly.
# If it is, then __name__ == "__main__"

# but if the module is running from an import, then it will assume the module name
# and will not be named "__main__"
# this means that anything in the imported script under a def main() function will not run.
if __name__ == "__main__":

# see first_module / second_module for examples.
