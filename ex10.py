tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Extra bit of code to try.
# while True:
#     for i in ["/","-","|","\\","|"]:
#         print "%s\r" % i,
        
# Study drill #3:

niko_dog = """
Things for a Niko dog:
1 - Medicine: \tTrazodone \\ Fluoxetine
2 - Treats: \tChicken Stix \\ Peanut Butter bone \\ Sausage things
3 - Food: \tBlue Buffalo
"""

print "Where is my list for Niko? Oh, it's below this line... \n%s" % niko_dog

# Study drill #4:

single_quote_escape = 'I\'m 5\'8"'
double_quote_escape = "I'm 5'8\""

print "How tall are you? %r" % single_quote_escape
print "How tall are you? %r" % double_quote_escape
print "How tall are you? %s" % single_quote_escape
print "How tall are you? %s" % double_quote_escape