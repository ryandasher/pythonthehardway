# Importing the argv module from the sys library
from sys import argv

# Setting the arguments for argv
script, input_file = argv

# Defining the print_all function, which reads the file argument
def print_all(f):
    print f.read()
    
# Defining the rewind function, which moves back to the start of file unless
# otherwise specified
def rewind(f):
    f.seek(0)
    
# Defining the print_a_line function, which prints a line and an integer
def print_a_line(line_count, f):
    print line_count, f.readline()
    
# Sets the variable current_file to the input_file and opens it
current_file = open(input_file)

# Prints a string
print "First let's print the whole file:\n"

# Prints the contents of current_file, using print_all function
print_all(current_file)

# Prints a string
print "Now let's rewind, kind of like a tape."

# Sets the file position for current_file at zero
rewind(current_file)

# Prints a string
print "Let's print three lines:"

# Sets the current_line variable to 1
current_line = 1
# Runs print_a_line function
print_a_line(current_line, current_file)

# Sets the current_line variable to 2
current_line += 1
print_a_line(current_line, current_file)

# Sets the current_line variable to 3
current_line += 1
print_a_line(current_line, current_file)