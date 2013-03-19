from sys import argv

script, user_name, year = argv
response = '... '

print "Hi %s, I'm the %s script and it is the year %s" % (user_name, script, year)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(response)

print "Where do you live %s?" % user_name
lives = raw_input(response)

print "What kind of computer do you have?"
computer = raw_input(response)

# Using the triple-quotes allows you to write as many lines
# as you want.
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)