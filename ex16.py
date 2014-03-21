from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1 + '\n' + line2 + '\n' + line3 + '\n')

print "Now we're going to show you what you wrote:"

target = open(filename)
print target.read()

print "And finally, we close it."
target.close()

# Study drill 4: You presumably have to pass the 'w' manually because opening the file in write mode will truncate it.

# Study drill 5: Yes, opening the file in write mode will truncate it.