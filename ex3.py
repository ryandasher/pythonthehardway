print "I will now count my chickens:"

# This formula counts my hens, you divide 30 by 6 and then add 25.
print "Hens", 25.0 + 30.0 / 6.0
# This formula counts my roosters by multiplying 25 and 3, to get 75.
# Then 75 % 4 is 3, because 3 is the remainder in that equation.
# Then you subtract 100 by 3.
print "Roosters", 100.0 - 25.0 * 3.0 % 4.0

print "Now I will count the eggs:"

# This formula gives you a remainder of 0 for 4 % 2.
# Then you get 0 for 1 divided by 4 because you round down in Python.
# Then do your addition and subtraction and get 7.
print 3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0

print "Is it true that 3.0 + 2.0 < 5.0 - 7.0?"

# This formula returns false because 5 is not less than -2.
print 3.0 + 2.0 < 5.0 - 7.0

# This formula adds 3 and 2, and returns 5.
print "What is 3.0 + 2.0?", 3.0 + 2.0
# This formula subtracts 5 and 7, and returns -2.
print "What is 5.0 - 7.0?", 5.0 - 7.0

print "Oh, that's why it's False."

print "How about some more."

# The following formulas return true or false, depending on the statement.
print "Is it greater?", 5.0 > -2.0
print "Is it greater or equal?", 5.0 >= -2.0
print "Is it less or equal?", 5.0 <= -2.0