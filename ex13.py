# Importing in the features (modules) you plan to use with your script.
from sys import argv

# This line "unpacks" the arguments from the module importing.
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third