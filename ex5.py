name = 'Zed A. Shaw'
age = 27 # not a lie
height_in_inches = 5 * 12 + 8 # Feet times inches plus remainder
height_in_centimeters = height_in_inches * 2.54 # inches to centimeters
weight = 140 * 0.453592 # lbs. to kilos
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %r." % name
print "He's %r centimeters tall." % height_in_centimeters
print "He's %r kilos heavy." % weight
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %r, %r, and %r I get %r." % (
    age, height_in_centimeters, weight, age + height_in_centimeters + weight)