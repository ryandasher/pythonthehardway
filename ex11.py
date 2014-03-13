print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r years old, %r tall and %r heavy." % (age, height, weight)

# Study drill 1: raw_input() will read a line from input and convert it into a string.

# Study drill 2:
name = raw_input('What is your name?\n')
print 'Hi, %s.' % name

# Study drill 3:
print "What is your favorite videogame?",
videogame = raw_input()
print "Who is your favorite videogame character?",
character = raw_input()
print "Who is your favorite videogame villain?",
villain = raw_input()

print """So, your favorite game is %r, your favorite character is %r, and your 
favorite villain is %r?""" % (videogame, character, villain)