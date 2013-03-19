# Imports the argument variable as a module or library.
from sys import argv

# The argument variable names.
script, filename = argv

# The text variable opens the filename specified.
txt = open(filename)

# Prints a string specifying the filename.
print "Here's your file %r:" % filename
# Reads the filename specified in the text variable.
# This is a function of the txt variable.
print txt.read()

# A string that requests the user to type in the filename.
print "Type the filename again:"
# The user's raw input for the filename.
file_again = raw_input("> ")

# Simply opening the file specified in the file_again variable.
txt_again = open(file_again)

# Reads the file specified in the file_again variable.
# This is a function of the txt_again variable.
print txt_again.read()