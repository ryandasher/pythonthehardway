tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* 'Cat food'
\t* Fishies
\t* Catnip\n\t* Grass
'''

test_cat = "You're a \"dumb\" cat with a \"silly\" face. \\ Don't mess with me.\n I'm on a new line!"

test_r_cat = "Hey man, don't be bothering me with that \"stuff\""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print test_cat
print "Hey, you. %r" % test_r_cat
print "Hey, you. %s" % test_r_cat