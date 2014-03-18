# Imports argv from the sys library
from sys import argv

# Gives the arguments you need to pass a variable name
script, filename = argv

# Opens a file and assigns to variable txt
txt = open(filename)

# Prints a line with your filename
print "Here's your file %r:" % filename
# Prints the contents of your file with the read function
print txt.read()

txt.close()

# Prints a line
print "Type the filename again:"
# Asks for user input, and assigns to variable file_again
file_again = raw_input("> ")

# Open your new file and assign to variable txt_again
txt_again = open(file_again)

# Print the contents of your file
print txt_again.read()

txt_again.close()