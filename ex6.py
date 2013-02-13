# The string for variable x. The format variable calls the variable 10.
x = "There are %d types of people." % 10
# The string for the binary variable.
binary = "binary"
# The string for the do_not variable.
do_not = "don't"
# The string for the y variable. The format variables call the variables binary and do_not
y = "Those who know %s and those who %s." % (binary, do_not)

# Printing the x variable.
print x
# Printing the y variable.
print y

# Print a string containing the x variable.
print "I said: %r." % x
# Print a string containing the y variable.
print "I also said: '%s'." % y

# The string for the hilarious variable.
hilarious = False
# The string for the joke_evaluation variable.
joke_evaluation = "Isn't that joke so funny?! %r"

# Print the joke_evaluation variable and the format variable it contains.
print joke_evaluation % hilarious

# The string for the w variable.
w = "This is the left side of..."
# The string for the e variable.
e = "a string with a right side."

# Print the w and e variable together.
print w + e