# Setting the variable x as a string and string formatter with integer.
x = "There are %d types of people." % 10
# Setting the variable binary as a string.
binary = "binary"
# Setting the variable do_not as a string.
do_not = "don't"
# Setting the variable y as a string and string formatter.
y = "Those who know %s and those who %s." % (binary, do_not)

# Printing variables x and y.
print x
print y

# Printing strings with variables x and y using string formatters.
print "I said: %r." % x
print "I also said: '%s'." % y

# Setting the variable hilarious to boolean false.
hilarious = False
# Setting the variable joke_evaluation as a string and string format.
joke_evaluation = "Isn't that joke so funny?! %r"

# Printing variables joke_evaluation and hilarious.
print joke_evaluation % hilarious

# Setting the variables w and e as strings.
w = "This is the left side of..."
e = "a string with a right side."

# Printing the variables w and e as a combined string.
print w + e

# Study drill 3: I believe there are only four places. The first instance where string formatting is used is for an integer, and not a string.

# Study drill 4: The + is the and operator.