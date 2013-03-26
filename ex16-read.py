from sys import argv

script, filename = argv

print "Here is the file you have requested:"
target = open(filename, 'r')
